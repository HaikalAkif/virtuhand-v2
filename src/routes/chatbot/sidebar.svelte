
<script lang="ts">
  export let isOpen: boolean = true;
  let isMainMenuOpen: boolean = true;
</script>

<aside class={`h-screen bg-gray-900 text-white flex flex-col transition-all duration-300 ${isOpen ? 'w-64' : 'w-0 overflow-hidden'}`}>
  <div class="p-4 flex justify-between items-center whitespace-nowrap">
    <h1 class="text-2xl text-lime-500"><a href="/">VirtuHand</a></h1>
    <button 
      class="text-gray-400 hover:text-white"
      on:click={() => isOpen = !isOpen}
    >
      ☰
    </button>
  </div>

  <div class="flex flex-col">
    <button 
      class="px-4 py-2 text-gray-400 hover:bg-gray-800 text-left"
      on:click={() => isMainMenuOpen = !isMainMenuOpen}
    >
      Main Menu
    </button>

    {#if isMainMenuOpen}
      <div class="flex flex-col">
        <a 
          href="#chatbots" 
          class="px-4 py-2 bg-gray-800 text-gray-300 hover:bg-gray-700"
        >
          Chats
        </a>
        <a 
          href="/about" 
          class="px-4 py-2 text-gray-300 hover:bg-gray-800"
        >
          About
        </a>
        <a 
          href="https://www.termsfeed.com/live/087fb814-8ea9-4b64-81bb-11c9a349af1d" 
          class="px-4 py-2 text-gray-300 hover:bg-gray-800"
        >
          Privacy Policy
        </a>
      </div>
    {/if}
  </div>
</aside>