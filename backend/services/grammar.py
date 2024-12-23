from transformers import pipeline

# Load the pre-trained T5 model for grammar correction
grammar_pipeline = pipeline("text2text-generation", model="t5-small")

def correct_grammar(text):
    """Corrects grammar of the input text."""
    return grammar_pipeline(f"fix grammar: {text}")[0]['generated_text']
