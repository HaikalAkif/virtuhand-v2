<script lang="ts">
	import { onMount } from 'svelte';
	import Sidebar from './sidebar.svelte';
	import { type ChatMessage } from './types';
	import { DocumentAttachOutline, Send, CameraOutline } from 'svelte-ionicons';
	import { nanoid } from 'nanoid';
	import { parseGeminiMessageResponse, parseGeminiPartsResponse } from './response-parser';

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
	let typingText: string = '';
	let fullText: string = 'Upload an image to be transcript';
	let currentIndex: number = 0;
	let pastedFile: File | null = null;
	let pastedFileName: string = '';

	const handlePaste = async (event: ClipboardEvent) => {
		const items = event.clipboardData?.items;
		if (!items) return;

		for (const item of items) {
			if (item.type.indexOf('image') !== -1) {
				const file = item.getAsFile();
				if (file) {
					pastedFile = file;
					pastedFileName = file.name;
				}
			}
		}
	};

	const typeText = () => {
		if (currentIndex < fullText.length) {
			typingText += fullText[currentIndex];
			currentIndex++;
			setTimeout(typeText, 100);
		}
	};

	onMount(() => {
		isSidebarOpen = false;
		isMobile = window.innerWidth <= 720;

		const checkMobile = () => {
			isMobile = window.innerWidth <= 720;
		};

		window.addEventListener('resize', checkMobile);
		scrollToBottom();
		typeText();

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
		return nanoid();
	};

	const handleSendMessage = async () => {
		if (message.trim() || pastedFile) {
			if (pastedFile) {
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
					sendToAPI(pastedFile!);
					pastedFile = null;
					pastedFileName = '';
				};
				reader.readAsDataURL(pastedFile);
			} else {
				const newMessage: ChatMessage = {
					id: generateId(),
					content: message.trim(),
					type: 'text',
					timestamp: new Date(),
					sender: 'user'
				};
				chatMessages = [...chatMessages, newMessage];
				message = '';
				scrollToBottom();
				await sendMessageToAPI(newMessage.content);
			}
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
			isCameraActive = true;

			// Request camera access
			mediaStream = await navigator.mediaDevices.getUserMedia({
				video: {
					facingMode: 'environment'
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
				sender: 'user'
			};

			chatMessages = [...chatMessages, newMessage];
			scrollToBottom();

			// Convert data URL to File for API
			fetch(imageDataUrl)
				.then((res) => res.blob())
				.then((blob) => {
					const file = new File([blob], 'captured-image.jpg', { type: 'image/jpeg' });
					sendToAPI(file);
				});

			stopCamera();
		}
	};

	const stopCamera = () => {
		if (mediaStream) {
			mediaStream.getTracks().forEach((track) => track.stop());
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
						sender: 'user'
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

	async function sendMessageToAPI(message: string) {
		const messageID = generateId();
		const messageTimestamp = new Date();

		const botResponse: ChatMessage = {
			id: messageID,
			content: '',
			type: 'loading',
			timestamp: messageTimestamp,
			sender: 'bot'
		};

		chatMessages = [...chatMessages, botResponse];

		const payload = {
			message
		};

		const response = await fetch('https://api.virtuhand.icool.my/chat', {
			method: 'POST',
			body: JSON.stringify(payload),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok || !response.body) {
			const responseJson = await response.json();

			const errorResponse: ChatMessage = {
				id: messageID,
				content: responseJson['message'],
				type: 'error',
				timestamp: messageTimestamp,
				sender: 'bot'
			};

			chatMessages = chatMessages.filter((message) => message.id !== messageID);
			chatMessages = [...chatMessages, errorResponse];

			return;
		}

		const reader = response.body.getReader();
		const decoder = new TextDecoder();

		let buffer = ``;

		while (true) {
			scrollToBottom();

			const { done, value } = await reader.read();

			if (done) break;

			const rawText = decoder.decode(value, { stream: true });

			const geminiMessage = parseGeminiMessageResponse(rawText);

			// buffer += rawText;

			chatMessages = chatMessages.filter((message) => message.id !== messageID);

			buffer += geminiMessage.join('');

			const newMessage: ChatMessage = {
				id: messageID,
				content: buffer,
				type: 'text',
				timestamp: messageTimestamp,
				sender: 'bot'
			};
			chatMessages = [...chatMessages, newMessage];
		}

		buffer = '';
	}

	async function sendToAPI(file: File) {
		const messageID = generateId();
		const messageTimestamp = new Date();

		const botResponse: ChatMessage = {
			id: messageID,
			content: '',
			type: 'loading',
			timestamp: messageTimestamp,
			sender: 'bot'
		};

		chatMessages = [...chatMessages, botResponse];

		const fd = new FormData();

		fd.append('image', file);

		const response = await fetch('https://api.virtuhand.icool.my/virtuhand', {
			method: 'POST',
			body: fd
		});

		if (!response.ok || !response.body) {
			const responseJson = await response.json();

			const errorResponse: ChatMessage = {
				id: messageID,
				content: responseJson['message'],
				type: 'error',
				timestamp: messageTimestamp,
				sender: 'bot'
			};

			chatMessages = chatMessages.filter((message) => message.id !== messageID);
			chatMessages = [...chatMessages, errorResponse];

			return;
		}

		const reader = response.body.getReader();
		const decoder = new TextDecoder();

		let buffer = ``;

		while (true) {
			scrollToBottom();

			const { done, value } = await reader.read();

			if (done) break;

			const rawText = decoder.decode(value, { stream: true });

			const geminiMessage = parseGeminiPartsResponse(rawText);

			chatMessages = chatMessages.filter((message) => message.id !== messageID);

			buffer += geminiMessage.join('');

			const newMessage: ChatMessage = {
				id: messageID,
				content: buffer,
				type: 'text',
				timestamp: messageTimestamp,
				sender: 'bot'
			};
			chatMessages = [...chatMessages, newMessage];
		}

		buffer = '';
	}

	const formatTime = (date: Date) => {
		return new Intl.DateTimeFormat('en-US', {
			hour: '2-digit',
			minute: '2-digit'
		}).format(date);
	};

	const isLastMessage = (index: number) => {
		return index === chatMessages.length - 1;
	};
</script>

<div class="flex h-screen overflow-hidden bg-black">
	<Sidebar bind:isOpen={isSidebarOpen} />

	<main class="relative flex w-full flex-1 flex-col">
		<header class="flex-shrink-0 border-b border-gray-800 p-2 sm:p-4">
			<div class="flex items-center gap-4">
				{#if !isSidebarOpen}
					<button class="text-gray-400 hover:text-white" on:click={() => (isSidebarOpen = true)}>
						☰
					</button>
				{/if}
				<h2 class="text-lg text-Twhite sm:text-xl">My Chat</h2>
			</div>
		</header>

		<div
			bind:this={chatContainer}
			class="relative flex-1 space-y-4 overflow-y-auto p-2 pb-24 sm:p-4 {isSidebarOpen
				? 'sm:ml-64'
				: ''}"
		>
			{#if chatMessages.length === 0}
				<div
					class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 transform text-center text-gray-400"
				>
					<p class="typing-text">{typingText}</p>
				</div>
			{/if}
			{#each chatMessages as message, index}
				<div
					class={`flex flex-col gap-1 ${message.sender === 'user' ? 'items-end' : 'items-start'}`}
				>
					{#if message.type === 'text'}
						<div
							class={`relative ${message.sender === 'user' ? 'bg-purple-600' : 'bg-gray-800'} max-w-[80%] break-words rounded-lg p-3 text-white`}
						>
							<div class="max-w-full overflow-x-auto whitespace-pre-wrap">
								{message.content}
							</div>
							{#if isLastMessage(index)}
								<div class="absolute bottom-0 right-0 translate-y-full pt-1">
									<span class="text-xs text-gray-400">
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
								class="w-full max-w-[280px] rounded-lg object-contain sm:max-w-[360px]"
							/>
							{#if isLastMessage(index)}
								<div class="absolute bottom-0 right-0 translate-y-full pt-1">
									<span class="text-xs text-gray-400">
										{formatTime(message.timestamp)}
									</span>
								</div>
							{/if}
						</div>
					{:else if message.type === 'loading'}
						<svg
							class="-ml-1 mr-3 h-5 w-5 animate-spin text-white"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
						>
							<circle
								class="opacity-25"
								cx="12"
								cy="12"
								r="10"
								stroke="currentColor"
								stroke-width="4"
							></circle>
							<path
								class="opacity-75"
								fill="currentColor"
								d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
							></path>
						</svg>
					{:else if message.type === 'error'}
						<div
							class={`relative ${message.sender === 'user' ? 'bg-purple-600' : 'bg-gray-800'} max-w-[80%] break-words rounded-lg p-3 text-red-600`}
						>
							{message.content}
							{#if isLastMessage(index)}
								<div class="absolute bottom-0 right-0 translate-y-full pt-1">
									<span class="text-xs text-gray-400">
										{formatTime(message.timestamp)}
									</span>
								</div>
							{/if}
						</div>
					{/if}
				</div>
			{/each}
		</div>

		<div
			class="fixed bottom-0 {isSidebarOpen
				? 'sm:left-64'
				: 'left-0'} right-0 z-30 border-t border-gray-800 bg-black p-2 sm:p-4"
		>
			<div class="flex gap-2 sm:gap-4">
				<div class="relative flex-1">
					<input
						type="text"
						bind:value={message}
						on:keypress={handleKeyPress}
						on:paste={handlePaste}
						placeholder={pastedFileName || (isMobile ? 'Message...' : 'Type or paste something...')}
						class="w-full truncate rounded-lg bg-gray-900 px-3 py-2 pr-20 text-sm text-white focus:outline-none focus:ring-2 focus:ring-purple-500 sm:px-4 sm:py-3 sm:pr-24 sm:text-base"
					/>
					<div class="absolute right-1 top-1/2 flex -translate-y-1/2 gap-1 sm:right-2 sm:gap-2">
						<button
							class="rounded-full p-1.5 text-gray-400 hover:bg-gray-800 hover:text-white sm:p-2"
							on:click={handleFileUpload}
						>
							<DocumentAttachOutline class="text-Twhite" />
						</button>

						<button
							class="rounded-full p-1.5 text-gray-400 hover:bg-gray-800 hover:text-white sm:p-2"
							on:click={handleCameraCapture}
						>
							<CameraOutline class="text-Twhite" />
						</button>

						<button
							class="rounded-full p-1.5 text-gray-400 hover:bg-gray-800 hover:text-white sm:p-2"
							on:click={handleSendMessage}
						>
							<Send class="h-5 w-5 sm:h-6 sm:w-6" />
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
			class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-black bg-opacity-90 p-4"
		>
			<div class="relative w-full max-w-md">
				<video bind:this={videoElement} class="w-full rounded-lg" playsinline>
					<track kind="captions" src="" default />
				</video>
				<canvas bind:this={canvasElement} class="hidden"></canvas>
				<canvas bind:this={canvasElement} class="hidden"></canvas>
			</div>
			<div class="mt-4 flex space-x-4">
				<button class="rounded-lg bg-green-500 px-4 py-2 text-white" on:click={captureImage}>
					Capture
				</button>
				<button class="rounded-lg bg-red-500 px-4 py-2 text-white" on:click={stopCamera}>
					Cancel
				</button>
			</div>
		</div>
	{/if}
</div>

<style>
	.typing-text {
		border-right: 2px solid #fff;
		animation: blink 0.75s step-end infinite;
		white-space: nowrap;
	}

	@keyframes blink {
		from,
		to {
			border-color: transparent;
		}
		50% {
			border-color: #fff;
		}
	}
</style>
