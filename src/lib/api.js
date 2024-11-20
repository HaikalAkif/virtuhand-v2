export async function uploadImage(file) {
    const url = 'http://localhost:3000/virtuhand';

    // Prepare the form data
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        return result.message; // Extract and return `response.message`
    } catch (error) {
        console.error('Error uploading image:', error);
        throw error;
    }
}
