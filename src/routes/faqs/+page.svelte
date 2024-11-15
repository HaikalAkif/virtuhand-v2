<script>
    import { faqs } from '../../lib/data/faqdata.js';
    import { slide } from 'svelte/transition';
    import { ChevronDownOutline } from 'svelte-ionicons';
  
    // Track open/closed state for each FAQ
    let openStates = new Map(faqs.map(faq => [faq.id, false]));
  
    // Toggle answer visibility
    function toggleAnswer(id) {
      openStates.set(id, !openStates.get(id));
      openStates = openStates;
    }
  </script>
  
  <div class="min-h-screen bg-gray-900 flex flex-col">
    <main class="flex-grow py-12 px-4 sm:px-6 lg:px-8 overflow-y-auto">
        <div class="max-w-3xl mx-auto">
          <div class="text-center mb-12">
            <h1 class="text-3xl font-bold text-white sm:text-4xl">
              Frequently Asked Questions
            </h1>
            <p class="mt-4 text-lg text-gray-300">
              Find answers to common questions about VirtuHand services
            </p>
          </div>
    
          <div class="space-y-4">
            {#each faqs as faq (faq.id)}
              <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700">
                <button
                  on:click={() => toggleAnswer(faq.id)}
                  class="w-full px-6 py-4 flex justify-between items-center hover:bg-gray-700 transition-colors duration-200"
                >
                  <span class="text-left font-medium text-gray-100">
                    {faq.question}
                  </span>
                  <div class="transform transition-transform duration-200 {openStates.get(faq.id) ? 'rotate-180' : ''}">
                    <ChevronDownOutline 
                      class="w-5 h-5 text-gray-300"
                    />
                  </div>
                </button>
    
                {#if openStates.get(faq.id)}
                  <div
                    class="px-6 py-4 border-t border-gray-700 text-gray-300"
                    transition:slide={{ duration: 300 }}
                  >
                    {faq.answer}
                  </div>
                {/if}
              </div>
            {/each}
          </div>
        </div>
      </main>
  
    <footer class="bg-gray-800 py-6 mt-8">
      <div class="text-center space-y-2">
        <p class="text-gray-300">Contact me at: haikalakif17@gmail.com</p>
        <p class="text-gray-300">
          GitHub: 
          <a 
            href="https://github.com/HaikalAkif" 
            class="text-blue-400 hover:text-blue-300 transition-colors duration-200"
            target="_blank" 
            rel="noopener noreferrer"
          >
            @iCool
          </a>
        </p>
      </div>
    </footer>
  </div>