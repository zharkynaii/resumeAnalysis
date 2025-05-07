import nltk
nltk.download('stopwords')

import spacy
import subprocess
import sys

def install_spacy_model():
    try:
        spacy.load('en_core_web_sm')
    except OSError:
        subprocess.check_call([
            sys.executable, 
            "-m", "spacy", 
            "download", "en_core_web_sm"
        ])

if __name__ == "__main__":
    install_spacy_model()