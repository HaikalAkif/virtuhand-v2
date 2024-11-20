<script lang="ts">
    import { onMount } from 'svelte';
    import Sidebar from './sidebar.svelte';
    import { type ChatMessage } from './types';
    import { DocumentAttachOutline, Send } from 'svelte-ionicons';
	import { jsonrepair } from 'jsonrepair';
    
    let message: string = '';
    let isSidebarOpen: boolean = true;
    let fileInput: HTMLInputElement;
    let chatMessages: ChatMessage[] = [];
    let chatContainer: HTMLDivElement;
  
    onMount(() => {
      scrollToBottom();
    });
  
    const scrollToBottom = () => {
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    };
  
    const generateId = () => {
      return crypto.randomUUID();
    };
  
    const handleSendMessage = () => {
      if (message.trim()) {
        const newMessage: ChatMessage = {
          id: generateId(),
          content: message.trim(),
          type: 'text',
          timestamp: new Date(),
          sender: 'user',
        };
        
        chatMessages = [...chatMessages, newMessage];
        message = '';
        
        // Replace this with actual bot 
        setTimeout(() => {
          const botResponse: ChatMessage = {
            id: generateId(),
            content: "This is a bot response",
            type: 'text',
            timestamp: new Date(),
            sender: 'bot',
          };
          chatMessages = [...chatMessages, botResponse];
          scrollToBottom();
        }, 1000);
        
        scrollToBottom();
      }
    };
  
    const handleKeyPress = (event: KeyboardEvent) => {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        handleSendMessage();
      }
    };
  
    const handleFileUpload = () => {
      fileInput.click();
    };
  
    const onFileSelected = async (event: Event) => {
      const target = event.target as HTMLInputElement;
      const files = target.files;
      
      if (files && files.length > 0) {
        const file = files[0];
        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          
          reader.onload = (e) => {
            const newMessage: ChatMessage = {
              id: generateId(),
              content: e.target?.result as string,
              type: 'image',
              timestamp: new Date(),
              sender: 'user',
            };
            
            chatMessages = [...chatMessages, newMessage];

            scrollToBottom();

            sendToAPI(file);
          };
          
          reader.readAsDataURL(file);
        }
        
        target.value = '';
      }
    };

    async function sendToAPI(file: File) {

      const messageID = generateId()
      const messageTimestamp = new Date()

      const botResponse: ChatMessage = {
        id: messageID,
        content: '',
        type: 'loading',
        timestamp: messageTimestamp,
        sender: 'bot',
      };

      chatMessages = [...chatMessages, botResponse];

      const fd = new FormData();

      fd.append('image', file);

      const response = await fetch('http://localhost:3000/virtuhand', {
        method: 'POST',
        body: fd,
      });

      if (!response.ok || !response.body) {

        const responseJson = await response.json()
        
        const errorResponse: ChatMessage = {
          id: messageID,
          content: responseJson['message'],
          type: 'error',
          timestamp: messageTimestamp,
          sender: 'bot',
        };

        chatMessages = chatMessages.filter((message) => message.id !== messageID);
        chatMessages = [...chatMessages, errorResponse];

        return;

      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      let buffer = ``;

      while (true) {

        scrollToBottom()

        const { done, value } = await reader.read()
        
        if (done) break;

        const rawText = decoder.decode(value, { stream: true });

        const jsonResponse = JSON.parse(jsonrepair(rawText));

        const parts = jsonResponse.parts;

        buffer += parts[0].text;

        chatMessages = chatMessages.filter((message) => message.id !== messageID);

        parts.forEach((part: any) => {
          const newMessage: ChatMessage = {
            id: messageID,
            content: buffer,
            type: 'text',
            timestamp: messageTimestamp,
            sender: 'bot',
          };
          chatMessages = [...chatMessages, newMessage];
        });

        // document.getElementById("response-text").innerText = buffer;

        //   const boundary = buffer.lastIndexOf(`\n`);
        //   if (boundary !== -1) {
        //     const completeData = buffer.substring(0, boundary);
        //     buffer = buffer.substring(boundary + 1);

        //     completeData.split(`\n`).forEach((chunk) => {
        //       if (chunk) {
        //         try {
        //           const jsonObj = JSON.parse(chunk);
        //           // Yay! Do what you want with your JSON here!
        //         } catch (e) {
        //           console.error(`Error parsing JSON:`, e);
        //         }
        //       }
        //     });
        //   }

      }

    }
  
    const formatTime = (date: Date) => {
      return new Intl.DateTimeFormat('en-US', {
        hour: '2-digit',
        minute: '2-digit',
      }).format(date);
    };
  
    const isLastMessage = (index: number) => {
      return index === chatMessages.length - 1;
    };
  </script>
  
  <div class="flex h-screen bg-black">
    <Sidebar bind:isOpen={isSidebarOpen} />
    
    <main class="flex-1 flex flex-col">
      <header class="p-4 border-b border-gray-800">
        <div class="flex items-center gap-4">
          {#if !isSidebarOpen}
            <button 
              class="text-gray-400 hover:text-white"
              on:click={() => isSidebarOpen = true}
            >
              ☰
            </button>
          {/if}
          <h2 class="text-xl text-white">My Chat</h2>
        </div>
      </header>
  
      <div 
        bind:this={chatContainer}
        class="flex-1 overflow-y-auto p-4 space-y-4"
      >
        {#each chatMessages as message, index (message.id)}
          <div class={`flex flex-col gap-1 ${message.sender === 'user' ? 'items-end' : 'items-start'}`}>
            {#if message.type === 'text'}
              <div class={`relative ${message.sender === 'user' ? 'bg-purple-600' : 'bg-gray-800'} text-white p-3 rounded-lg max-w-[80%] break-words`}>
                {message.content}
                {#if isLastMessage(index)}
                  <div class="absolute bottom-0 right-0 translate-y-full pt-1">
                    <span class="text-gray-400 text-xs">
                      {formatTime(message.timestamp)}
                    </span>
                  </div>
                {/if}
              </div>
            {:else if message.type === 'image'}
              <div class="relative max-w-[80%]">
                <img 
                  src={message.content} 
                  alt="Uploaded"
                  class="rounded-lg max-w-[360px] object-contain"
                />
                {#if isLastMessage(index)}
                  <div class="absolute bottom-0 right-0 translate-y-full pt-1">
                    <span class="text-gray-400 text-xs">
                      {formatTime(message.timestamp)}
                    </span>
                  </div>
                {/if}
              </div>
            {:else if message.type === 'loading'}
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            {:else if message.type === 'error'}
              <div class={`relative ${message.sender === 'user' ? 'bg-purple-600' : 'bg-gray-800'} text-red-600 p-3 rounded-lg max-w-[80%] break-words`}>
                {message.content}
                {#if isLastMessage(index)}
                  <div class="absolute bottom-0 right-0 translate-y-full pt-1">
                    <span class="text-gray-400 text-xs">
                      {formatTime(message.timestamp)}
                    </span>
                  </div>
                {/if}
              </div>
            {/if}
          </div>
        {/each}
      </div>
  
      <div class="p-4 border-t border-gray-800">
        <div class="flex gap-4">
          <div class="flex-1 relative">
            <input
              type="text"
              bind:value={message}
              on:keypress={handleKeyPress}
              placeholder="Type something..."
              class="w-full bg-gray-900 text-white rounded-lg px-4 py-3 pr-24 focus:outline-none focus:ring-2 focus:ring-purple-500"
            />
            <div class="absolute right-2 top-1/2 -translate-y-1/2 flex gap-2">
              <button
                class="text-gray-400 hover:text-white p-2 rounded-full hover:bg-gray-800"
                on:click={handleFileUpload}
              >
                <DocumentAttachOutline class="text-Twhite" />
              </button>
              <button
                class="text-gray-400 hover:text-white p-2 rounded-full hover:bg-gray-800"
                on:click={handleSendMessage}
              >
                <Send class="text-Twhite" />
              </button>
            </div>
            <input 
              type="file"
              accept="image/*"
              bind:this={fileInput}
              on:change={onFileSelected}
              class="hidden"
            />
          </div>
          <button
            class="px-6 py-2 bg-purple-600 text-white rounded hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500"
          >
            New Chat
          </button>
        </div>
      </div>
    </main>
  </div>