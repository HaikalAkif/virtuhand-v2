<script lang="ts">
  import Particles from "../Particles.svelte";

  const benefits = [
    {
      title: "Natural Conversation",
      description: "Experience fluid, context-aware conversations that feel natural and engaging.",
      icon: "💬"
    },
    {
      title: "24/7 Availability",
      description: "Access intelligent assistance whenever you need it, day or night.",
      icon: "🕒"
    },
    {
      title: "Multi-Format Support",
      description: "Share text, images, and files seamlessly during your conversations.",
      icon: "📎"
    },
    {
      title: "Free Services",
      description: "Unlimited usage without worrying about any payments.",
      icon: "🤑"
    }
  ];

  function returnToMain() {
      window.location.href = "/";
  }
</script>

<div class="min-h-screen bg-gray-900 text-white relative overflow-hidden">
<Particles className="absolute inset-0" refresh={true} />
<div class="relative z-10 overflow-y-auto h-full">
  <div class="w-full h-full py-16 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <section class="mb-20">
        <h1 class="text-4xl font-bold mb-8">About VirtuHand</h1>
        <div class="bg-gray-800 rounded-2xl p-8 mb-6">
          <h2 class="text-2xl font-semibold mb-4">Our Journey</h2>
          <p class="text-gray-300 text-lg leading-relaxed mb-6">
            VirtuHand was born from a vision to help people ease the work of understanding unreadable text. Started as a passion final year project, we set out to create an assistant that 
            doesn't just respond, but truly understands and help people out.
          </p>
        </div>
      </section>

      <section class="mb-20">
        <h2 class="text-3xl font-bold mb-8">Our Values</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="bg-gray-800 rounded-xl p-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center">
              <span class="text-2xl mr-2">🎯</span>
              Innovation First
            </h3>
            <p class="text-gray-300">
              We constantly push the boundaries of what's possible in AI interaction, 
              striving to create more intuitive and efficient ways of communication.
            </p>
          </div>
          <div class="bg-gray-800 rounded-xl p-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center">
              <span class="text-2xl mr-2">🤝</span>
              User-Centric Design
            </h3>
            <p class="text-gray-300">
              Every feature and interaction is crafted with our users in mind, 
              ensuring an experience that's both powerful and accessible.
            </p>
          </div>
          <div class="bg-gray-800 rounded-xl p-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center">
              <span class="text-2xl mr-2">🔐</span>
              Trust & Security
            </h3>
            <p class="text-gray-300">
              We prioritize the security and privacy of our users, implementing 
              robust protection measures for all conversations and data.
            </p>
          </div>
          <div class="bg-gray-800 rounded-xl p-6">
            <h3 class="text-xl font-semibold mb-4 flex items-center">
              <span class="text-2xl mr-2">📈</span>
              Continuous Improvement
            </h3>
            <p class="text-gray-300">
              We're committed to constantly improving our service through user 
              feedback and technological advancements.
            </p>
          </div>
        </div>
      </section>

      <section class="mb-20">
        <h2 class="text-3xl font-bold mb-8">Key Features & Benefits</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          {#each benefits as benefit}
            <div class="bg-gray-800 rounded-xl p-6 transform hover:scale-105 transition-transform duration-300">
              <div class="text-4xl mb-4">{benefit.icon}</div>
              <h3 class="text-xl font-semibold mb-2">{benefit.title}</h3>
              <p class="text-gray-300">{benefit.description}</p>
            </div>
          {/each}
        </div>
      </section>

      <section class="text-center">
        <div class="bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl p-8">
          <h2 class="text-2xl font-bold mb-4">Our Mission</h2>
          <p class="text-lg max-w-2xl mx-auto">
            To make intelligent digital assistance accessible to everyone, creating 
            meaningful interactions that enhance productivity and understanding through 
            the power of AI.
          </p>
        </div>
      </section>

      <section class="mt-20 text-center">
        <h2 class="text-2xl font-bold mb-6">Want to Learn More?</h2>
        <p class="text-gray-300 mb-8">
          We're always excited to share more about VirtuHand and explore how we can help you.
        </p>
        <div class="flex justify-center gap-4">
          <a
            href="/contact"
            class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg transition-colors duration-300"
          >
            Contact Us
          </a>
        </div>
      </section>
    </div>
  </div>
</div>
</div>