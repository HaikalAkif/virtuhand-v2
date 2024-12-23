<script lang="ts">
    import Particles from "../Particles.svelte";
    
    // Function to scroll to section
    function scrollToSection(id: string) {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    }

    const sections = [
        { id: 'interpretation', title: 'Interpretation & Definitions' },
        { id: 'data-collection', title: 'Data Collection' },
        { id: 'data-usage', title: 'Data Usage' },
        { id: 'cookies', title: 'Cookies Policy' },
        { id: 'data-retention', title: 'Data Retention' },
        { id: 'data-transfer', title: 'Data Transfer' },
        { id: 'your-rights', title: 'Your Rights' },
        { id: 'contact', title: 'Contact Us' }
    ];
</script>

<div class="min-h-screen bg-gray-900 text-white relative overflow-hidden">
    <Particles className="absolute inset-0" refresh={true} />
    <div class="relative z-10 overflow-y-auto h-full">
    <div class="w-full h-full py-16 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto">
            <!-- Header Section -->
            <section class="mb-12">
                <h1 class="text-4xl font-bold mb-4">Privacy Policy</h1>
                <p class="text-gray-300">Last updated: November 10, 2024</p>
            </section>

            <!-- Quick Navigation -->
            <section class="mb-12 bg-gray-800 rounded-xl p-6">
                <h2 class="text-2xl font-semibold mb-4">Quick Navigation</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    {#each sections as section}
                        <button
                            on:click={() => scrollToSection(section.id)}
                            class="text-left px-4 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg transition-colors duration-300"
                        >
                            {section.title}
                        </button>
                    {/each}
                </div>
            </section>

            <!-- Main Content -->
            <div class="space-y-12">
                <!-- Interpretation Section -->
                <section id="interpretation" class="bg-gray-800 rounded-2xl p-8">
                    <h2 class="text-2xl font-semibold mb-6">Interpretation & Definitions</h2>
                    <div class="space-y-6 text-gray-300">
                        <p>The words of which the initial letter is capitalized have meanings defined under the following conditions. The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.</p>
                        <div class="bg-gray-700 rounded-xl p-6">
                            <h3 class="text-xl font-semibold mb-4">Key Terms</h3>
                            <ul class="space-y-4">
                                <li><span class="font-semibold">Account:</span> A unique account created for You to access our Service.</li>
                                <li><span class="font-semibold">Company:</span> Refers to VirtuHand.</li>
                                <li><span class="font-semibold">Service:</span> Refers to the Website.</li>
                                <li><span class="font-semibold">Personal Data:</span> Any information relating to an identified or identifiable individual.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Data Collection Section -->
                <section id="data-collection" class="bg-gray-800 rounded-2xl p-8">
                    <h2 class="text-2xl font-semibold mb-6">Data Collection</h2>
                    <div class="space-y-6 text-gray-300">
                        <div class="bg-gray-700 rounded-xl p-6">
                            <h3 class="text-xl font-semibold mb-4">Personal Data</h3>
                            <p class="mb-4">While using Our Service, We may collect:</p>
                            <ul class="list-disc list-inside space-y-2">
                                <li>Email address</li>
                                <li>First name and last name</li>
                                <li>Usage Data</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Data Usage Section -->
                <section id="data-usage" class="bg-gray-800 rounded-2xl p-8">
                    <h2 class="text-2xl font-semibold mb-6">Data Usage</h2>
                    <div class="space-y-6 text-gray-300">
                        <p>The Company may use Personal Data for:</p>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="bg-gray-700 rounded-xl p-6">
                                <h4 class="font-semibold mb-2">Service Maintenance</h4>
                                <p>To provide and maintain our Service, including monitoring usage patterns.</p>
                            </div>
                            <div class="bg-gray-700 rounded-xl p-6">
                                <h4 class="font-semibold mb-2">Account Management</h4>
                                <p>To manage Your registration and provide access to different functionalities.</p>
                            </div>
                            <div class="bg-gray-700 rounded-xl p-6">
                                <h4 class="font-semibold mb-2">Communication</h4>
                                <p>To contact You regarding updates or informative communications about the Service.</p>
                            </div>
                            <div class="bg-gray-700 rounded-xl p-6">
                                <h4 class="font-semibold mb-2">Service Improvement</h4>
                                <p>To improve our Service based on how you use it.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Contact Section -->
                <section id="contact" class="bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl p-8 text-center">
                    <h2 class="text-2xl font-bold mb-6">Questions About Our Privacy Policy?</h2>
                    <p class="mb-8">Contact us at: haikalakif17@gmail.com</p>
                    <a
                        href="mailto:haikalakif17@gmail.com"
                        class="inline-block bg-white text-blue-600 font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition-colors duration-300"
                    >
                        Contact Us
                    </a>
                </section>
            </div>
        </div>
    </div>
    </div>
</div>