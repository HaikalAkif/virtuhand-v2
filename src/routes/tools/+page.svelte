<script>
    import Particles from "../Particles.svelte";

    const tools = [
        {
            title: "File Format Converter",
            description: "Convert your text files between different formats (PDF, DOC, TXT)",
            icon: "📄",
            status: "Coming Soon"
        },
        {
            title: "Text Editor",
            description: "Simple online editor to modify your converted text",
            icon: "✏️",
            status: "Available"
        },
        {
            title: "Bulk Processing",
            description: "Convert multiple documents at once",
            icon: "📚",
            status: "Coming Soon"
        },
        {
            title: "Text Comparison",
            description: "Compare original and converted text side by side",
            icon: "🔍",
            status: "Available"
        },
        {
            title: "Language Detection",
            description: "Automatically detect the language of your text",
            icon: "🌐",
            status: "Coming Soon"
        },
        {
            title: "Export Options",
            description: "Export your converted text in various formats",
            icon: "💾",
            status: "Available"
        }
    ];
</script>

<div class="h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white overflow-hidden">
    <Particles className="absolute inset-0" refresh={true} />
    <div class="h-full container mx-auto px-4 py-8 overflow-y-auto">
        <div class="text-center mb-6 md:mb-8">
            <h1 class="text-2xl md:text-4xl font-bold mb-3 md:mb-4">Complementary Tools</h1>
            <p class="text-gray-300 text-sm md:text-base max-w-2xl mx-auto px-2">
                Enhance your text conversion experience with our additional tools. Some features are already available, while others are coming soon to make your workflow even smoother.
            </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-8">
            {#each tools as tool}
                <div class="bg-gray-800 rounded-lg p-4 md:p-6 hover:bg-gray-700 transition-colors duration-300 border border-gray-700">
                    <div class="flex items-start justify-between mb-3 md:mb-4">
                        <span class="text-3xl md:text-4xl">{tool.icon}</span>
                        <span class={`text-xs md:text-sm px-2 md:px-3 py-1 rounded-full ${tool.status === 'Available' ? 'bg-green-500' : 'bg-yellow-500'}`}>
                            {tool.status}
                        </span>
                    </div>
                    <h3 class="text-lg md:text-xl font-semibold mb-2">{tool.title}</h3>
                    <p class="text-sm md:text-base text-gray-400">{tool.description}</p>
                </div>
            {/each}
        </div>

        <div class="text-center mt-6 md:mt-8">
            <p class="text-gray-300 text-sm md:text-base mb-4 md:mb-6">Want to try our available tools?</p>
            <a 
                href="/chat" 
                class="bg-green-500 hover:bg-green-600 text-white font-semibold px-6 md:px-8 py-2 md:py-3 rounded-lg transition-colors duration-300 inline-block text-sm md:text-base"
            >
                Start Using Tools
            </a>
        </div>
    </div>
</div>