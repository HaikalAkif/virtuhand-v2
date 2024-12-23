<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './sidebar.svelte';
  import { type ChatMessage } from './types';
  import { DocumentAttachOutline, Send, CameraOutline } from 'svelte-ionicons';
  import { jsonrepair } from 'jsonrepair';
  
  let message: string = '';
  let isSidebarOpen: boolean = true;
  let fileInput: HTMLInputElement;
  let videoElement: HTMLVideoElement;
  let canvasElement: HTMLCanvasElement;
  let cameraModal: HTMLDivElement;
  let chatMessages: ChatMessage[] = [];
  let chatContainer: HTMLDivElement;
  let isMobile: boolean = false;
  let isCameraActive: boolean = false;
  let mediaStream: MediaStream | null = null;

  onMount(() => {
    // Check if it's a mobile device
    isMobile = window.innerWidth <= 720;
    
    // Add resize listener to update mobile status
    const checkMobile = () => {
      isMobile = window.innerWidth <= 720;
    };
    
    window.addEventListener('resize', checkMobile);
    scrollToBottom();
    
    // Cleanup listener on component destroy
    return () => {
      window.removeEventListener('resize', checkMobile);
      stopCamera();
    };
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

  const handleCameraCapture = async () => {
    try {
      // Open camera modal
      isCameraActive = true;
      
      // Request camera access
      mediaStream = await navigator.mediaDevices.getUserMedia({
        video: { 
          facingMode: 'environment' // Prefer back/environment camera
        }
      });
      
      // Set video source to camera stream
      if (videoElement && mediaStream) {
        videoElement.srcObject = mediaStream;
        videoElement.play();
      }
    } catch (error) {
      console.error('Camera access error:', error);
      alert('Could not access camera. Please check permissions.');
      isCameraActive = false;
    }
  };

  const captureImage = () => {
    if (videoElement && canvasElement) {
      // Set canvas dimensions to match video
      canvasElement.width = videoElement.videoWidth;
      canvasElement.height = videoElement.videoHeight;
      
      // Draw current video frame to canvas
      const context = canvasElement.getContext('2d');
      context?.drawImage(videoElement, 0, 0);
      
      // Convert canvas to data URL
      const imageDataUrl = canvasElement.toDataURL('image/jpeg');
      
      // Create message with captured image
      const newMessage: ChatMessage = {
        id: generateId(),
        content: imageDataUrl,
        type: 'image',
        timestamp: new Date(),
        sender: 'user',
      };
      
      chatMessages = [...chatMessages, newMessage];
      scrollToBottom();
      
      // Convert data URL to File for API
      fetch(imageDataUrl)
        .then(res => res.blob())
        .then(blob => {
          const file = new File([blob], 'captured-image.jpg', { type: 'image/jpeg' });
          sendToAPI(file);
        });
      
      // Close camera
      stopCamera();
    }
  };

  const stopCamera = () => {
    if (mediaStream) {
      mediaStream.getTracks().forEach(track => track.stop());
      mediaStream = null;
    }
    isCameraActive = false;
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

      buffer += rawText;

      chatMessages = chatMessages.filter((message) => message.id !== messageID);

      const newMessage: ChatMessage = {
        id: messageID,
        content: buffer,
        type: 'text',
        timestamp: messageTimestamp,
        sender: 'bot',
      };
      chatMessages = [...chatMessages, newMessage];
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
              class="text-gray-400 hover:text-Twhite p-2 rounded-full hover:bg-gray-800"
              on:click={handleFileUpload}
            >
              <DocumentAttachOutline class="text-Twhite" />
            </button>

            <button
              class="text-gray-400 hover:text-Twhite p-2 rounded-full hover:bg-gray-800"
              on:click={handleCameraCapture}
            >
              <CameraOutline class="text-Twhite" />
            </button>

            <button
              class="text-gray-400 hover:text-Twhite p-2 rounded-full hover:bg-gray-800"
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
      </div>
    </div>
  </main>

  {#if isCameraActive}
    <div 
      bind:this={cameraModal}
      class="fixed inset-0 bg-black bg-opacity-90 z-50 flex flex-col items-center justify-center p-4"
    >
      <div class="relative w-full max-w-md">
        <video 
            bind:this={videoElement}
            class="w-full rounded-lg"
            playsinline
          >
            <track kind="captions" src="" default />
          </video>
          <canvas 
            bind:this={canvasElement}
            class="hidden"
          ></canvas>
        <canvas 
          bind:this={canvasElement}
          class="hidden"
        ></canvas>
      </div>
      <div class="mt-4 flex space-x-4">
        <button 
          class="bg-green-500 text-white px-4 py-2 rounded-lg"
          on:click={captureImage}
        >
          Capture
        </button>
        <button 
          class="bg-red-500 text-white px-4 py-2 rounded-lg"
          on:click={stopCamera}
        >
          Cancel
        </button>
      </div>
    </div>
  {/if}
</div>