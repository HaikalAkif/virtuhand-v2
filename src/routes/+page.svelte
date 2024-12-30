<script lang="ts">
  import { ChatboxOutline, Menu, Bug } from 'svelte-ionicons';
  import MobileNav from './mobileNavPanel.svelte';
  import toast, { Toaster } from 'svelte-french-toast';
	import ThemeButton from './ThemeButton.svelte';
  import Particles from "./Particles.svelte";

  const handleSubscribeClick = () => {
    toast.error('This feature is not available yet', {
      position: 'bottom-center',
    });
  };

  let isDialogOpen = false;
  let isMenuOpen = false;
  $: feedbackContent= '';

  const openDialog = () => {
    isDialogOpen = true;
  };

  const closeDialog = () => {
    isDialogOpen = false;
    feedbackContent = '';
  };

  const submitFeedback = async() => {

    const formdata = new FormData()
    formdata.append('message', feedbackContent)

    const response = await fetch('?/submitFeedback', {
      method: 'POST',
      body: formdata
    })

    console.log(response)

    if (feedbackContent.trim()) {
      toast.success('Feedback submitted! Thank you!', {
        position: 'bottom-center',
      });
      closeDialog();
    } else {
      toast.error('Please write something before submitting.', {
        position: 'bottom-center',
      });
    }
  };

  function navigateToChatbot() {
    window.location.href = "/chatbot";
  }

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }
</script>

<div class="overflow-hidden bg-gradient-to-b from-gray-900 to-gray-800">
  <Particles className="absolute inset-0" refresh={true} />
  <div class="flex flex-col items-center justify-start min-h-screen bg-overlay">
    <div class="px-[5%] pt-[20px] w-full min-h-screen overflow-hidden">
      <nav class="flex items-center justify-between w-full px-6 py-3 relative text-Twhite">
        <a href="/" class="text-2xl text-lime-500 font-iGro">VirtuHand</a>
        
        <div class="hidden md:flex items-center gap-10 justify-center bg-transparent px-8 py-2">
          <h3 class="text-white"><a href="/tools" class="link">Tools</a></h3>
          <h3 class="text-white"><a href="#" onclick={handleSubscribeClick} class="link">Pricing</a></h3>
          <h3 class="text-white"><a href="/faqs" class="link">FAQs</a></h3>
          <h3 class="text-white"><a href="/about" class="link">About</a></h3>
        </div>
        
        <ThemeButton />

        <button 
          class="md:hidden text-white p-2"
          onclick={toggleMenu}
        >
          <Menu class="h-6 w-6" />
        </button>
      </nav>

      <div class="flex flex-col items-center md:items-center justify-center mt-10 gap-6 p-8 md:px-0">
        <h1 class="text-4xl md:text-6xl font-bold text-center md:text-center leading-[1.2] md:leading-[72px] text-white font-iGro">
          Making Text Accessible<br>For Everyone!
        </h1>
        <h5 class="text-Twhite drop-shadow-xl text-center md:text-center">
          Effortlessly convert handwritten notes into clear, readable digital text and accessible to everyone.
        </h5>
        <button 
          class="flex flex-row items-center justify-center mt-6 gap-2 px-6 py-2 w-fit text-lg text-Tblack bg-Twhite rounded-md active:scale-90"
          onclick={navigateToChatbot}
        >
          <ChatboxOutline class="text-Tblack h-6 w-6" />
          CHAT NOW
        </button>
      </div>

      <button 
    class="absolute bottom-0 right-0 z-10 m-[30px] p-3 w-fit h-fit bg-lime-500 rounded-md"
    onclick={openDialog}
  >
    <div class="flex flex-row items-center justify-center gap-4">
      <Bug />
      Feedback
    </div>
  </button>

  {#if isDialogOpen}
    <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div class="bg-Twhite rounded-lg shadow-lg p-6 w-96">
        <h2 class="text-lg text-Tblack font-bold mb-4">Feedback</h2>
        <textarea 
          class="w-full p-2 border border-gray-300 text-Tblack rounded-md focus:outline-none focus:ring-2 focus:ring-lime-500"
          rows="4"
          bind:value={feedbackContent}
          placeholder="Write your feedback here..."
        ></textarea>
        <div class="flex justify-end gap-2 mt-4">
          <button 
            class="px-4 py-2 bg-gray-300 text-gray-700 rounded-md hover:bg-gray-400"
            onclick={closeDialog}
          >
            Cancel
          </button>
          <button 
            class="px-4 py-2 bg-lime-500 text-white rounded-md hover:bg-lime-600"
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
<MobileNav isOpen={isMenuOpen} onClose={() => isMenuOpen = false} />

<style>
  :global(html), :global(body) {
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
    background: linear-gradient(to right, #EFEFEF, #EFEFEF);
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