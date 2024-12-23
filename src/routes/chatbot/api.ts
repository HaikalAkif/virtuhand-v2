export async function sendToAPI(file: File) {
    const fd = new FormData();
    fd.append('image', file);
  
    const response = await fetch('http://localhost:3000/virtuhand', {
      method: 'POST',
      body: fd,
    });
  
    if (!response.ok) {
      const responseJson = await response.json();
      throw new Error(responseJson['message'] || 'Upload failed');
    }
  
    return response;
  }