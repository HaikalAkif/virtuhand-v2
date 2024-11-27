import os
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow as tf
from spellchecker import SpellChecker
from transformers import pipeline
from better_profanity import profanity
import io

# Initialize the Flask app
app = Flask(__name__)

# Load the trained handwriting recognition model
model = load_model("path_to_your_model.h5")

# Initialize spelling, grammar correction, and bad word filtering tools
spell = SpellChecker()
grammar_pipeline = pipeline("text2text-generation", model="t5-small")
profanity.load_censor_words()

# Define characters for decoding
characters = "abcdefghijklmnopqrstuvwxyz0123456789 "
char_to_index = {char: idx for idx, char in enumerate(characters)}
index_to_char = {idx: char for char, idx in char_to_index.items()}

# CTC Decoding function
def decode_prediction(pred):
    decoded, _ = tf.keras.backend.ctc_decode(pred, input_length=[pred.shape[1]], greedy=False, beam_width=10)
    return ''.join([index_to_char[i] for i in decoded[0][0].numpy() if i != -1])

# Spell and grammar correction
def correct_spelling(text):
    tokens = text.split()
    corrected = [spell.correction(token) for token in tokens]
    return " ".join(corrected)

def correct_grammar(text):
    return grammar_pipeline(f"fix grammar: {text}")[0]['generated_text']

# Bad word filtering
def filter_bad_words(text):
    return profanity.censor(text)

# Route to handle image uploads and transcription
@app.route("/upload", methods=["POST"])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Process the uploaded image
    img = Image.open(io.BytesIO(file.read())).convert('L')
    img = img.resize((128, 32))  # Resize to match input size
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict transcription
    pred = model.predict(img_array)
    transcribed_text = decode_prediction(pred)

    # Apply corrections and filtering
    corrected_spelling = correct_spelling(transcribed_text)
    corrected_grammar = correct_grammar(corrected_spelling)
    final_output = filter_bad_words(corrected_grammar)

    return jsonify({"transcription": final_output})

# Chatbot route for user interaction
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_query = data.get("query", "")

    # A simple chatbot logic (replace with advanced NLP for better results)
    if "help" in user_query.lower():
        response = "How can I assist you with your handwriting transcription?"
    elif "transcription" in user_query.lower():
        response = "You can upload a handwriting image for transcription via the upload feature."
    else:
        response = "I'm here to assist you. Please provide more details about your query."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

