from spellchecker import SpellChecker
from transformers import pipeline
from better_profanity import profanity

spell = SpellChecker()
grammar_pipeline = pipeline("text2text-generation", model="t5-small")
profanity.load_censor_words()

def correct_spelling(text):
    tokens = text.split()
    corrected = [spell.correction(token) for token in tokens]
    return " ".join(corrected)

def correct_grammar(text):
    return grammar_pipeline(f"fix grammar: {text}")[0]['generated_text']

def filter_bad_words(text):
    return profanity.censor(text)
