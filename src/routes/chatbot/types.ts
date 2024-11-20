export interface ChatMessage {
	id: string;
	content: string;
	type: 'text' | 'image' | 'loading' | 'error';
	timestamp: Date;
	sender: 'user' | 'bot';
}
