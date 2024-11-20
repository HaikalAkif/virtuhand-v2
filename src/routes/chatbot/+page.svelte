<script lang="ts">
    import { onMount } from 'svelte';
    import Sidebar from './sidebar.svelte';
    import type { ChatMessage } from './types';
    import { DocumentAttachOutline, Send } from 'svelte-ionicons';
    
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
      return Math.random().toString(36).substr(2, 9);
    };
  
    const handleSendMessage = () => {
      if (message.trim()) {
        const newMessage: ChatMessage = {
          id: generateId(),
          content: message.trim(),
          type: 'text',
          timestamp: new Date(),
          sender: 'user'
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
            sender: 'bot'
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
              sender: 'user'
            };
            
            chatMessages = [...chatMessages, newMessage];
            scrollToBottom();
          };
          
          reader.readAsDataURL(file);
        }
        
        target.value = '';
      }
    };
  
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
                  alt="Uploaded image"
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