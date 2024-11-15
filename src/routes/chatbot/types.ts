export interface ChatMessage {
    id: string;
    content: string;
    type: 'text' | 'image';
    timestamp: Date;
    sender: 'user' | 'bot';
  }