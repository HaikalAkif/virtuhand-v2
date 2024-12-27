
<script lang="ts">
  export let isOpen: boolean = true;
  let isMainMenuOpen: boolean = true;
</script>

<aside class={`fixed sm:relative h-screen bg-gray-900 text-white flex flex-col transition-all duration-300 z-20 ${isOpen ? 'w-[40vw] sm:w-64' : 'w-0 overflow-hidden'}`}>
  <div class="p-3 sm:p-4 flex justify-between items-center whitespace-nowrap">
    <h1 class="text-xl sm:text-2xl text-lime-500"><a href="/">VirtuHand</a></h1>
    <button 
      class="text-gray-400 hover:text-white P-2"
      on:click={() => isOpen = !isOpen}
    >
      ☰
    </button>
  </div>

  <div class="flex flex-col">
    <button 
      class="px-4 py-2 text-gray-400 hover:bg-gray-800 text-left text-sm sm:text-base"
      on:click={() => isMainMenuOpen = !isMainMenuOpen}
    >
      Main Menu
    </button>

    {#if isMainMenuOpen}
      <div class="flex flex-col">
        <a 
          href="#chatbots" 
          class="px-4 py-2 bg-gray-800 text-gray-300 hover:bg-gray-700 text-sm sm:text-base"
        >
          Chats
        </a>
        <a 
          href="/about" 
          class="px-4 py-2 text-gray-300 hover:bg-gray-800 text-sm sm:text-base"
        >
          About
        </a>
        <a 
          href="/privacypolicy" 
          class="px-4 py-2 text-gray-300 hover:bg-gray-800 text-sm sm:text-base"
        >
          Privacy Policy
        </a>
      </div>
    {/if}
  </div>
</aside>