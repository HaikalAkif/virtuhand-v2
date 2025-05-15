<script lang="ts">
	import { ChatboxOutline, Menu, Bug } from 'svelte-ionicons';
	import MobileNav from './mobileNavPanel.svelte';
	import toast, { Toaster } from 'svelte-french-toast';
	import Particles from './Particles.svelte';

	const handleSubscribeClick = () => {
		toast.error('This feature is not available yet', {
			position: 'bottom-center'
		});
	};

	let isDialogOpen = false;
	let isMenuOpen = false;
	$: feedbackContent = '';

	const openDialog = () => {
		isDialogOpen = true;
	};

	const closeDialog = () => {
		isDialogOpen = false;
		feedbackContent = '';
	};

	const submitFeedback = async () => {
		const formdata = new FormData();
		formdata.append('message', feedbackContent);

		const response = await fetch('?/submitFeedback', {
			method: 'POST',
			body: formdata
		});

		console.log(response);

		if (feedbackContent.trim()) {
			toast.success('Feedback submitted! Thank you!', {
				position: 'bottom-center'
			});
			closeDialog();
		} else {
			toast.error('Please write something before submitting.', {
				position: 'bottom-center'
			});
		}
	};

	function navigateToChatbot() {
		window.location.href = '/chatbot';
	}

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}
</script>

<div class="overflow-hidden bg-gradient-to-b from-gray-900 to-gray-800">
	<Particles className="absolute inset-0" refresh={true} />
	<div class="bg-overlay flex min-h-screen flex-col items-center justify-start">
		<div class="min-h-screen w-full overflow-hidden px-[5%] pt-[20px] relative">
			<nav class="relative flex w-full items-center justify-between px-6 py-3 text-Twhite">
				<a href="/" class="font-iGro text-2xl text-lime-500">VirtuHand</a>

				<div class="hidden items-center justify-center gap-10 bg-transparent px-8 py-2 md:flex">
					<h3 class="text-white"><a href="/tools" class="link">Tools</a></h3>
					<h3 class="text-white">
						<a href="#" onclick={handleSubscribeClick} class="link">Pricing</a>
					</h3>
					<h3 class="text-white"><a href="/faqs" class="link">FAQs</a></h3>
					<h3 class="text-white"><a href="/about" class="link">About</a></h3>
				</div>

				<button class="p-2 text-white md:hidden" onclick={toggleMenu}>
					<Menu class="h-6 w-6" />
				</button>
			</nav>

			<div
				class="mt-10 flex flex-col items-center justify-center gap-6 p-8 md:items-center md:px-0"
			>
				<h1
					class="text-center font-iGro text-4xl font-bold leading-[1.2] text-white md:text-center md:text-6xl md:leading-[72px]"
				>
					Making Text Accessible<br />For Everyone!
				</h1>
				<h5 class="text-center text-Twhite drop-shadow-xl md:text-center">
					Effortlessly convert handwritten notes into clear, readable digital text and accessible to
					everyone.
				</h5>
				<button
					class="mt-6 flex w-fit flex-row items-center justify-center gap-2 rounded-md bg-Twhite px-6 py-2 text-lg text-Tblack active:scale-90"
					onclick={navigateToChatbot}
				>
					<ChatboxOutline class="h-6 w-6 text-Tblack" />
					CHAT NOW
				</button>
			</div>

			<button
				class="fixed md:absolute bottom-4 right-4 z-10 h-fit w-fit rounded-md bg-lime-500 p-3"
				onclick={openDialog}
			>
				<div class="flex flex-row items-center justify-center gap-4">
					<Bug />
					Feedback
				</div>
			</button>

			{#if isDialogOpen}
				<div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
					<div class="w-96 rounded-lg bg-Twhite p-6 shadow-lg">
						<h2 class="mb-4 text-lg font-bold text-Tblack">Feedback & Bug Report</h2>
						<textarea
							class="w-full rounded-md border border-gray-300 p-2 text-Tblack focus:outline-none focus:ring-2 focus:ring-lime-500"
							rows="4"
							bind:value={feedbackContent}
							placeholder="Write your feedback or bug report here..."
						></textarea>
						<div class="mt-4 flex justify-end gap-2">
							<button
								class="rounded-md bg-gray-300 px-4 py-2 text-gray-700 hover:bg-gray-400"
								onclick={closeDialog}
							>
								Cancel
							</button>
							<button
								class="rounded-md bg-lime-500 px-4 py-2 text-white hover:bg-lime-600"
								onclick={submitFeedback}
							>
								Submit
							</button>
						</div>
					</div>
				</div>
			{/if}
		</div>
	</div>
</div>

<Toaster />
<MobileNav isOpen={isMenuOpen} onClose={() => (isMenuOpen = false)} />

<style>
	:global(html),
	:global(body) {
		margin: 0;
		padding: 0;
		height: 100vh;
	}

	.link {
		position: relative;
		text-decoration: none;
		font-size: 1.125rem;
		line-height: 1.75rem;
	}

	.link::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 2px;
		background: linear-gradient(to right, #efefef, #efefef);
		background-size: 0% 100%;
		background-repeat: no-repeat;
		transition: background-size 0.45s ease;
	}

	.link:hover::after {
		background-size: 100% 100%;
	}

	.bg-overlay > * {
		position: relative;
		z-index: 0;
	}

	@media (max-width: 768px) {
		.bg-overlay {
			background-position: center center;
		}
	}
</style>
