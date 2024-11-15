
<script>
    import { fade, fly } from 'svelte/transition';
    import { quintOut } from 'svelte/easing';
    
    export let isOpen = false;
    export let onClose = () => {};
  </script>
  
  {#if isOpen}

    <div
      class="fixed inset-y-0 right-0 z-50 w-full bg-gray-900"
      transition:fly={{ x: 300, duration: 300, easing: quintOut }}
    >
      <div class="flex flex-col h-100-vh p-6">
        <div class="flex justify-between items-center mb-6">
          <a href="/" class="text-2xl text-lime-500 font-iGro">VirtuHand</a>
          <button 
            class="text-white text-3xl hover:rotate-90 transition-transform duration-300"
            on:click={onClose}
          >
            ×
          </button>
        </div>
        
        <div class="flex flex-col gap-8">
          {#each ['Tools', 'Pricing', 'FAQs', 'About'] as link}
            <a 
              href={`/${link.toLowerCase()}`} 
              class="nav-link text-white text-xl relative overflow-hidden group border border-white"
            >
              <span class="relative z-10">{link}</span>
            </a>
          {/each}
        </div>
        <div class="flex flex-col gap-3 my-4">
            <button class="w-full py-3 text-slate-100 border-2 border-white rounded-full hover:bg-white hover:text-gray-900 transition-colors duration-300">
              Log In
            </button>
            <button class="w-full py-3 text-gray-900 bg-white rounded-full hover:bg-lime-500 hover:text-white transition-colors duration-300">
              Sign Up
            </button>
            <div class="relative flex items-center justify-center bottom-0">
            <h6 class="text-Twhite">V2.02</h6>
        </div>
        </div>
        
      </div>
    </div>
  {/if}
  
  <style>
    .nav-link {
      padding: 0.5rem 0;
      transition: transform 0.2s;
    }
    
    .nav-link:active {
      transform: scale(0.97);
    }
  </style>