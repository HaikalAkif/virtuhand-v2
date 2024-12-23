
<script>
    import { SunnyOutline, MoonOutline} from 'svelte-ionicons'
    import { onMount } from 'svelte'
  
    let theme = 'light'
  
    onMount(() => {
      // Check localStorage first
      const savedTheme = localStorage.getItem('theme')
      if (savedTheme) {
        theme = savedTheme
      } else {
        // Check system preference
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
          theme = 'dark'
        }
      }
      updateTheme(theme)
    })
  
    // Function to update theme
    function updateTheme(newTheme) {
      theme = newTheme
      localStorage.setItem('theme', theme)
      
      if (theme === 'dark') {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    }
  
    // Toggle function
    function toggleTheme() {
      const newTheme = theme === 'light' ? 'dark' : 'light'
      updateTheme(newTheme)
    }
  </script>
  
  <button
    type="button"
    class="inline-flex h-10 w-16 items-center rounded-full bg-zinc-200 p-1 dark:bg-zinc-700 hidden md:flex"
    on:click={toggleTheme}
    aria-label="Toggle theme"
  >
    <div
      class="relative h-8 w-8 rounded-full bg-white shadow-sm transition-transform dark:translate-x-6 dark:bg-zinc-800"
    >
      <SunnyOutline
        class="absolute left-1/2 top-1/2 h-4 w-4 -translate-x-1/2 -translate-y-1/2 text-Tblack opacity-100 transition-opacity dark:opacity-0"
      />
      <MoonOutline
        class="absolute left-1/2 top-1/2 h-4 w-4 -translate-x-1/2 -translate-y-1/2 text-Twhite opacity-0 transition-opacity dark:opacity-100"
      />
    </div>
  </button>