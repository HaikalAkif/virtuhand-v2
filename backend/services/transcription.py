import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
from services.nlp import correct_spelling, correct_grammar, filter_bad_words

model = load_model("models/handwriting_model.h5")
characters = "abcdefghijklmnopqrstuvwxyz0123456789 "
index_to_char = {idx: char for idx, char in enumerate(characters)}

def decode_prediction(pred):
    decoded, _ = tf.keras.backend.ctc_decode(pred, input_length=[pred.shape[1]], greedy=False, beam_width=10)
    return ''.join([index_to_char[i] for i in decoded[0][0].numpy() if i != -1])

def process_image(file):
    img = Image.open(file).convert('L')
    img = img.resize((128, 32))  # Resize to model input size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=[-1, 0])
    pred = model.predict(img_array)
    transcribed_text = decode_prediction(pred)
    corrected_spelling = correct_spelling(transcribed_text)
    corrected_grammar = correct_grammar(corrected_spelling)
    return filter_bad_words(corrected_grammar)
