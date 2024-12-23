from textblob import TextBlob

def correct_spelling(text):
    """Corrects the spelling of words in the input text."""
    blob = TextBlob(text)
    return str(blob.correct())

def filter_bad_words(text, bad_words):
    """Filters bad words from the input text."""
    for word in bad_words:
        text = text.replace(word, "****")
    return text

