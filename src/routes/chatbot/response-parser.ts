// Types for the Gemini response structure
interface GeminiMessage {
	text: string;
}

interface GeminiMessageResponse {
	message: GeminiMessage[];
	success: boolean;
}

interface GeminiPartsResponse {
	parts: GeminiMessage[];
	success: boolean;
}

export function parseGeminiMessageResponse(responseText: string): string[] {
	// Split the response into individual JSON objects
	const jsonObjects = responseText.trim().split('}{');

	// Restore the curly braces that were split
	const fixedJsonObjects = jsonObjects.map((obj, index) => {
		if (jsonObjects.length === 1) return obj;
		if (index === 0) return obj + '}';
		if (index === jsonObjects.length - 1) return '{' + obj;
		return '{' + obj + '}';
	});

	const parsedMessages: string[] = [];

	// Parse each JSON object and extract the message text
	for (const jsonObj of fixedJsonObjects) {
		try {
			const data = JSON.parse(jsonObj) as GeminiMessageResponse;
			if (data.success && Array.isArray(data.message)) {
				data.message.forEach((msg) => {
					if (msg.text) {
						parsedMessages.push(msg.text);
					}
				});
			}
		} catch (error) {
			console.error('Error parsing JSON object:', error);
			continue;
		}
	}

	return parsedMessages;
}

export function parseGeminiPartsResponse(responseText: string): string[] {
	// Split the response into individual JSON objects
	const jsonObjects = responseText.trim().split('}{');

	// Restore the curly braces that were split
	const fixedJsonObjects = jsonObjects.map((obj, index) => {
		if (jsonObjects.length === 1) return obj;
		if (index === 0) return obj + '}';
		if (index === jsonObjects.length - 1) return '{' + obj;
		return '{' + obj + '}';
	});

	const parsedMessages: string[] = [];

	// Parse each JSON object and extract the message text
	for (const jsonObj of fixedJsonObjects) {
		try {
			const data = JSON.parse(jsonObj) as GeminiPartsResponse;
			if (data.success && Array.isArray(data.parts)) {
				data.parts.forEach((msg) => {
					if (msg.text) {
						parsedMessages.push(msg.text);
					}
				});
			}
		} catch (error) {
			console.error('Error parsing JSON object:', error);
			continue;
		}
	}

	return parsedMessages;
}