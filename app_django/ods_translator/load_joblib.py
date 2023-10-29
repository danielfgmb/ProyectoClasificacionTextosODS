from django.conf import settings

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
import os
from unidecode import unidecode
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# PREPROCESS
def change_non_ascii(words):
    # acentos aceptados en esta fase
    pattern = r'[\u00E1\u00E9\u00ED\u00F3\u00FA\u00C1\u00C9\u00CD\u00D3\u00DA\u00FC\u00DC\u00F1\u00D1]'
    new_words = []
    for word in words:
        original_size = len(word)
        new_word = word.encode('latin-1',"ignore").decode('utf-8',"ignore")
        if not re.search(pattern, new_word):
            new_word = word
        new_words.append(new_word)
    return new_words

def remove_accents(words):
    return [unidecode(word) for word in words]

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    return [word.lower() for word in words]

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s¡°©]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

stop_words = set(nltk.corpus.stopwords.words('spanish'))  # Lista de stop words en español

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    return [word for word in words if word not in stop_words]

def fix_special_characters(words):
    """Fix special characters in list of tokenized words"""
    fixed_words = []
    for word in words:
        fixed_word = word.replace('ã³', 'o').replace('ã©', 'e').replace('ã¡', 'a').replace('ã', 'i').replace('ã|', 'u')
        fixed_words.append(fixed_word)
    return fixed_words


def preprocess(doc):
    words = doc.split(" ")
    words = change_non_ascii(words)
    words = remove_accents(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_stopwords(words)
    return fix_special_characters(words)

def df_preprocess(df):
    return df.apply(preprocess)

TransformerPreprocesar = FunctionTransformer(df_preprocess)


stemmer_es = nltk.stem.SnowballStemmer("spanish")

def tokenize(words):
    nltk_stemedList_es = [stemmer_es.stem(word) for word in words]
    return " ".join(nltk_stemedList_es)

def tokenize_df(df):
    return df.apply(tokenize)

TransformerTokenizar = FunctionTransformer(tokenize_df)
