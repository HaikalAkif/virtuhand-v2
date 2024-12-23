from flask import Flask
from routes.transcription import transcription_bp
from routes.chatbot import chatbot_bp

app = Flask(__name__)

# Register blueprints for modular routes
app.register_blueprint(transcription_bp, url_prefix="/transcription")
app.register_blueprint(chatbot_bp, url_prefix="/chatbot")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


