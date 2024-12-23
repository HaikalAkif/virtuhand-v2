<script>
  import { fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import toast, { Toaster } from 'svelte-french-toast';
  
  export let isOpen = false;
  export let onClose = () => {};

  const handleSubscribeClick = () => {
    toast.error('This feature is not available yet', {
      position: 'bottom-center',
    });
  };

  const handleClick = (e, link) => {
      if (link === 'Pricing') {
          e.preventDefault();
          handleSubscribeClick(e);
      }
      // Other links will navigate normally
  };
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
            class="nav-link text-white text-xl relative overflow-hidden group"
            on:click={(e) => handleClick(e, link)}
          >
            <span class="relative z-10">{link}</span>
          </a>
        {/each}
      </div>
    </div>
    <Toaster />
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