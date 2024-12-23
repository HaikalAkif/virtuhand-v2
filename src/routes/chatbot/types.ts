export type MessageType = 'text' | 'image' | 'loading' | 'error';
export type MessageSender = 'user' | 'bot';

export interface ChatMessage {
  id: string;
  content: string;
  type: MessageType;
  timestamp: Date;
  sender: MessageSender;
}
