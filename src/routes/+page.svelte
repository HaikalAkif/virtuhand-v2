<div class="overflow-hidden" id="land">

    <div class="flex flex-col items-center justify-start min-h-screen bg-gradient-to-b from-[#171717] via-[#004a53] to-[#00E0FF]">
      <div class="px-[10%] w-full min-h-screen overflow-hidden">
        <nav class="flex items-center justify-between w-full px-8 py-4 relative">
          <a href="/src/Landing.svelte" class="text-2xl font-bold text-lime-500">VirtuHand</a>
          <div class="flex items-center gap-10 justify-center bg-transparent px-8 py-2">
            <h3 class="text-white"><a href="#" class="link">Blog</a></h3>
            <h3 class="text-white"><a href="#" class="link">How to Use</a></h3>
            <h3 class="text-white"><a href="/pricing" class="link">Pricing</a></h3>
            <h3 class="text-white"><a href="#" class="link">About</a></h3>
          </div>
          <div class="flex items-center justify-center gap-4">
            <button class="px-4 py-2 text-slate-100 hover:scale-95">Log In</button>
            <button class="px-4 py-2 text-lime-400 bg-transparent border-2 border-lime-500 rounded-3xl hover:scale-95 hover:bg-lime-500 hover:text-black">Sign Up</button>
          </div>
        </nav>
  
        <div class="flex flex-col items-center justify-center mt-20">
          <h1 class="text-6xl font-bold text-center leading-[72px] text-white mb-8">Making Text Accessible<br>For Everyone</h1>
          <button class="glass px-6 py-2 w-[200px] text-lg text-white mb-[100px] backdrop-blur-lg">Try Now</button>
          <img
            src="/src/assets/images/chat-prev.png"
            alt="Preview"
            class="w-[90%] h-[800px] rounded-xl object-fit"
          />
        </div>
      </div>
    </div>
  </div>

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
      border-radius: 0 10px;
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.3);
      box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);
    }
  
    .glass:hover {
      background: rgba(255, 255, 255, 0.3);
    }
  </style>