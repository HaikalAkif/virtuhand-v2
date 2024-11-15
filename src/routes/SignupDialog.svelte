
<script>
    import { LogoGoogle, LogoApple, Globe, Eye, EyeOff } from "svelte-ionicons";

    export let isOpen = false;
    export let onClose = () => {};

    let showPassword = false;
    let email = '';
    let password = '';
    let rememberMe = false;

    function togglePasswordVisibility() {
      showPassword = !showPassword;
    }

    function handleSubmit() {
      // Handle form submission
      console.log('Form submitted', { email, password, rememberMe });
    }
  
    const handleEmailSignup = () => {
      console.log('Signup with Email');
    };
  
    const handleGoogleSignup = () => {
      console.log('Signup with Google');
    };
  </script>
  
  {#if isOpen}
    <div class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      
      <div class="bg-white p-8 rounded-lg w-full max-w-md shadow-lg relative">

        <button on:click={onClose} class="absolute top-2 right-2 text-gray-500 hover:text-gray-700">
          ✕
        </button>
  
        <h2 class="text-2xl font-semibold text-Tblack mb-1x text-center">Welcome</h2>
        <h5 class="text-m text-Tblack mb-6 text-center">Please enter your details to sign in</h5>
        <div class="flex flex-row gap-2 w-full">
          <button class="flex items-center justify-center rounded-md drop-shadow-lg py-3 px-12 bg-white w-full hover:scale-95">
            <LogoGoogle class="text-Tblack" />
          </button>
          <!-- <button class="flex items-center justify-center rounded-md drop-shadow-lg py-3 px-12 bg-white w-full hover:scale-95">
            <LogoApple class="text-Tblack" />
          </button> -->
        </div>
        <div class="relative flex items-center justify-center mt-6 mb-2">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-400"></div>
          </div>
          <div class="relative bg-white px-4 text-lg text-gray-500">
            or
          </div>
        </div>
  
        <form on:submit|preventDefault={handleSubmit} class="space-y-4">
          <div>
            <label for="email" class="block text-sm text-gray-600 mb-1">Email address</label>
            <input
              type="email"
              id="email"
              bind:value={email}
              placeholder="Enter your email"
              class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-lime-500"
              required
            />
          </div>
    
          <div>
            <label for="password" class="block text-sm text-gray-600 mb-1">Password</label>
            <div class="relative">
              <input
                type={showPassword ? 'text' : 'password'}
                id="password"
                bind:value={password}
                placeholder="Enter your password"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-lime-500"
                required
              />
              <button
                type="button"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500"
                on:click={togglePasswordVisibility}
              >
                {#if showPassword}
                  <EyeOff class="w-5 h-5" />
                {:else}
                  <Eye class="w-5 h-5" />
                {/if}
              </button>
            </div>
          </div>
    
          <div class="flex items-center justify-between">
            <label class="flex items-center gap-2">
              <input
                type="checkbox"
                bind:checked={rememberMe}
                class="rounded text-purple-600 focus:ring-lime-500"
              />
              <span class="text-sm text-gray-600">Remember for 30 days</span>
            </label>
            <a href="/forgot-password" class="text-sm underline text-purple-600 hover:text-purple-700">Forgot password?</a>
          </div>
    
          <button
            type="submit"
            class="w-full py-2 px-4 bg-lime-500 text-white rounded-lg hover:bg-lime-600 focus:outline-none focus:ring-2 focus:ring-lime-400 focus:ring-offset-2 shadow-md"
          >
            Sign in
          </button>
        </form>
    
        <p class="text-center mt-6 text-sm text-gray-600">
          Don't have an account?
          <a href="/create-account" class="text-purple-600 hover:text-purple-700">Create account</a>
        </p>
      </div>
    </div>
  {/if}
  