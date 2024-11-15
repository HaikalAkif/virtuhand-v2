<script>
  import { ArrowBack } from 'svelte-ionicons';
  import toast, { Toaster } from 'svelte-french-toast';

  const handleSubscribeClick = () => {
    toast.error('This feature is not available yet', {
      position: 'top-center',
    });
  };
</script>

<div class="min-h-screen bg-gray-900 text-white">
  <nav class="sticky top-0 z-10 w-full bg-gray-900 border-b border-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <a href="/" class="flex items-center text-white hover:text-gray-300">
          <ArrowBack class="h-5 w-5 mr-2" />
          <span class="font-mono font-bold">Back</span>
        </a>
        <h2 class="text-2xl font-bold text-lime-500">VirtuHand</h2>
        <div class="w-20"></div>
      </div>
    </div>
  </nav>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold mb-4">Choose your plan</h1>
    </div>

    <div class="flex flex-col lg:flex-row gap-8 justify-center items-stretch max-w-5xl mx-auto">
      <!-- Free Plan -->
      <div class="w-full lg:w-1/2 bg-gray-800/50 rounded-xl p-8 backdrop-blur-sm border border-gray-700">
        <div class="flex flex-col h-full">
          <div class="mb-8">
            <h2 class="text-2xl font-bold mb-2">Free</h2>
            <div class="flex items-baseline mb-4">
              <span class="text-3xl font-bold">RM0</span>
              <span class="ml-1 text-gray-400">/month</span>
            </div>
            <p class="text-gray-300">
              Discover how AI may assist you with<br/>daily duties.
            </p>
          </div>

          <div class="space-y-4 flex-grow">
            <div class="space-y-3">
              <div class="flex items-center gap-2">
                <span>• Limited to 5 transcribe per day</span>
              </div>
              <div class="flex items-center gap-2">
                <span>• Support 3 languages only</span>
              </div>
            </div>
          </div>

          <div class="mt-8">
            <div class="w-full py-3 bg-gray-700 text-white rounded-lg flex items-center justify-center gap-2">
              <span class="h-2 w-2 bg-green-500 rounded-full animate-pulse"></span>
              Active Plan
            </div>
          </div>
        </div>
      </div>

      <!-- Premium Plan -->
      <div class="w-full lg:w-1/2 bg-gray-800/50 rounded-xl p-8 backdrop-blur-sm border border-gray-700 hover:border-lime-700">
        <div class="flex flex-col h-full">
          <div class="mb-8">
            <h2 class="text-2xl font-bold mb-2">Premium</h2>
            <div class="flex items-baseline mb-4">
              <span class="text-3xl font-bold">RM19</span>
              <span class="ml-1 text-gray-400">/month</span>
            </div>
            <p class="text-gray-300">
              Discover how AI may assist you with<br/>daily duties.
            </p>
          </div>

          <div class="space-y-4 flex-grow">
            <div class="space-y-3">
              <div class="flex items-center gap-2">
                <span>• Unlimited Transcribe</span>
              </div>
              <div class="flex items-center gap-2">
                <span>• Support All languages</span>
              </div>
              <div class="flex items-center gap-2">
                <span>• Early Access to New Features</span>
              </div>
            </div>
          </div>

          <div class="mt-8">
            <button onclick={handleSubscribeClick} class="w-full py-3 bg-teal-300 text-gray-900 rounded-lg hover:bg-teal-400 transition-colors font-medium">
              Subscribe Now
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="text-center mt-8 text-sm text-gray-400">
      Subscription auto-renews until canceled. <a href="#" class="underline">Learn more</a>
    </div> -->

    <Toaster />
  </main>
</div>

  