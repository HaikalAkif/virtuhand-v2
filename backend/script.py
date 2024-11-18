from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Reshape, Dense, GRU, Bidirectional
from tensorflow.keras.layers import BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Lambda
import tensorflow.keras.backend as K
import tensorflow as tf
from tensorflow.keras.backend import ctc_decode
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from transformers import pipeline
nltk.download("words")
nltk.download("punkt")
from spellchecker import SpellChecker
from flask import Flask, request, jsonify

# Define possible characters in the dataset
characters = "!\"#&'()*+,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz " 

# Mapping of characters to indices
char_to_index = {char: idx for idx, char in enumerate(characters)}
index_to_char = {idx: char for char, idx in char_to_index.items()}

# Define input
input_img = Input(shape=(32, 128, 1), name="image")  # (height, width, channels)

# Convolutional layers
x = Conv2D(32, (3, 3), padding="same", activation="relu")(input_img)
x = MaxPooling2D((2, 2))(x)
x = BatchNormalization()(x)

x = Conv2D(64, (3, 3), padding="same", activation="relu")(x)
x = MaxPooling2D((2, 2))(x)
x = BatchNormalization()(x)

# Reshape for RNN input
x = Reshape((-1, 64))(x)  # Flatten spatial dimensions

# Recurrent layers
x = Bidirectional(GRU(128, return_sequences=True))(x)
x = Bidirectional(GRU(128, return_sequences=True))(x)

# Dense layer
output = Dense(len(characters) + 1, activation="softmax")(x)  # CTC-compatible output

# Define model
model = Model(inputs=input_img, outputs=output)
model.compile(optimizer=Adam(), loss="ctc_loss")

model.summary()

# CTC loss function
def ctc_loss(y_true, y_pred):
    input_length = tf.ones((y_pred.shape[0],)) * y_pred.shape[1]
    label_length = tf.reduce_sum(tf.cast(y_true != -1, tf.int32), axis=-1)
    return tf.reduce_mean(K.ctc_batch_cost(y_true, y_pred, input_length, label_length))

model.compile(optimizer=Adam(), loss=ctc_loss)

# Train the model
model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_val, y_val))

def decode_prediction(pred):
    decoded, _ = ctc_decode(pred, input_length=[pred.shape[1]], greedy=True)
    return ''.join([characters[i] for i in decoded[0][0].numpy()])

# Dictionary for valid words
valid_words = set(words.words())

# Improved spelling correction with suggestions
spell = SpellChecker()

def correct_spelling(text):
    tokens = word_tokenize(text)
    corrected = [spell.correction(token) if token not in valid_words else token for token in tokens]
    return " ".join(corrected)

raw_text = "Ths is a sampl txt."
print(correct_spelling(raw_text))

# Grammar correction using transformers
grammar_pipeline = pipeline("text2text-generation", model="t5-small")

# Grammar correction
def correct_grammar(text):
    return grammar_pipeline(f"fix grammar: {text}")[0]['generated_text']

# Example pipeline
def process_image_and_refine_transcription(image, model):
    # Preprocess the input image
    image = np.expand_dims(image, axis=(0, -1))  # Add batch and channel dimensions
    image = image / 255.0  # Normalize pixel values

    # Predict transcription
    pred = model.predict(image)
    transcribed_text = decode_prediction(pred)

    # Correct spelling
    corrected_spelling = correct_spelling(transcribed_text)

    # Correct grammar
    final_output = correct_grammar(corrected_spelling)

    return final_output

# Example inputs
raw_text = "Ths is a sampl txt."
print("Corrected Spelling:", correct_spelling(raw_text))

transcribed_text = "This is teh transcribbed text."
print("Corrected Grammar:", correct_grammar(transcribed_text))