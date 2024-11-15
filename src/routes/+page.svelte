
<script>
  import { ChatboxOutline } from 'svelte-ionicons';
  import { Menu } from 'svelte-ionicons';
  import MobileNav from './mobileNavPanel.svelte';

  import SignupDialog from './SignupDialog.svelte';
  let isDialogOpen = false;

  const openDialog = () => {
    isDialogOpen = true;
  };

  const closeDialog = () => {
    isDialogOpen = false;
  };

  let isMenuOpen = false;

  function navigateToChatbot() {
    window.location.href = "/chatbot";
  }

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }
</script>

<div class="overflow-hidden" id="land">
  <div class="flex flex-col items-center justify-start min-h-screen bg-overlay">
    <div class="px-[5%] pt-[20px] w-full min-h-screen overflow-hidden">
      <nav class="glass flex items-center justify-between w-full px-6 py-3 relative text-Twhite backdrop-blur-lg rounded-full">
        <a href="/" class="text-2xl text-lime-500 font-iGro">VirtuHand</a>
        
        <div class="hidden md:flex items-center gap-10 justify-center bg-transparent px-8 py-2">
          <h3 class="text-white"><a href="/tools" class="link">Tools</a></h3>
          <h3 class="text-white"><a href="/pricing" class="link">Pricing</a></h3>
          <h3 class="text-white"><a href="/faqs" class="link">FAQs</a></h3>
          <h3 class="text-white"><a href="/about" class="link">About</a></h3>
        </div>
        
        <div class="hidden md:flex items-center gap-4">
          <button class="px-4 py-2 text-slate-100 hover:scale-95">Log In</button>
          <button on:click={openDialog} class="px-4 py-2 text-Tblack bg-Twhite border-2 rounded-full hover:scale-95">Sign Up</button>
        </div>

        <button 
          class="md:hidden text-white p-2"
          on:click={toggleMenu}
        >
          <Menu class="h-6 w-6" />
        </button>
      </nav>

      <div class="flex flex-col items-center md:items-start justify-center mt-20 gap-4 px-4 md:px-0">
        <h1 class="text-4xl md:text-6xl font-bold text-center md:text-start leading-[1.2] md:leading-[72px] text-white font-iGro">
          Making Text Accessible<br>For Everyone!
        </h1>
        <h5 class="text-Twhite drop-shadow-xl text-center md:text-start">
          Effortlessly convert handwritten notes into clear, readable digital text and accessible to everyone.
        </h5>
        <button 
          class="flex flex-row items-center justify-center gap-2 px-6 py-2 w-fit text-lg text-Tblack bg-Twhite rounded-full"
          on:click={navigateToChatbot}
        >
          <ChatboxOutline class="text-Tblack h-6 w-6" />
          Chat Now
        </button>
      </div>
    </div>
  </div>

  <div class="absolute bottom-0 right-0 m-[30px] p-3 w-[300px] h-fit bg-white rounded-xl hidden md:block">
    <h2 class="my-2 font-iGro font-bold">Virtuhand</h2>
    <h4 class="mb-2">Your go-to tool for clear, digital<br>text conversion.</h4>
    <img
      src="../../src/images/landing-bg.webp"
      alt="Preview"
      class="w-full rounded-md object-fit"
    />
  </div>
</div>

<SignupDialog isOpen={isDialogOpen} onClose={closeDialog} />
<MobileNav isOpen={isMenuOpen} onClose={() => isMenuOpen = false} />

<style>
  :global(html), :global(body) {
    margin: 0;
    padding: 0;
    overflow: hidden;
    height: 100vh;
  }

  #land {
    height: 100%;
    overflow: hidden;
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

  .glass {
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);
  }

  .bg-overlay {
    position: relative;
    background-image: url('../images//landing-bg.webp');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }

  .bg-overlay > * {
    position: relative;
    z-index: 2;
  }

  @media (max-width: 768px) {
    .bg-overlay {
      background-position: center center;
    }
  }
</style>