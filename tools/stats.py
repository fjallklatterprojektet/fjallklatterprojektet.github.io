import argparse
import glob
import os

import pandas as pd
import textstat
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, "html.parser")
    main_soup = soup.find("main")

    return "".join(main_soup.find_all(string=True)) if main_soup else ""

def nltk_tokenize_words(text):
    return [word for word in word_tokenize(text) if len(word) > 1 or word.isalpha()]

def nltk_word_count(text):
    return len(nltk_tokenize_words(text))

def nltk_long_word_count(text):
    return len([word for word in nltk_tokenize_words(text) if len(word) > 6])

def nltk_sentence_count(text):
    return len(sent_tokenize(text))

def lix(text):
    word_count = nltk_word_count(text)
    long_word_count = nltk_long_word_count(text)
    sentence_count = nltk_sentence_count(text)
    if word_count > 0 and sentence_count > 0:
        return word_count / sentence_count + 100 * long_word_count / word_count
    else:
        return 0

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to the directory")
parser.parse_args()

args = parser.parse_args()
path = args.path

html_files = glob.glob(path + "*.html", recursive=True)

textstat.set_lang("sv")
texts = list(map(extract_text_from_html, html_files))

word_counts_textstat = list(map(lambda t: textstat.lexicon_count(t, removepunct=True), texts))
sentence_counts_textstat = list(map(lambda t: textstat.sentence_count(t), texts))

word_counts_nltk = list(map(lambda t: nltk_word_count(t), texts))
long_word_counts_nltk = list(map(lambda t: nltk_long_word_count(t), texts))
sentence_counts_nltk = list(map(lambda t: nltk_sentence_count(t), texts))
lix_scores = list(map(lambda t: round(lix(t)), texts))

data = {
    "Word Count (textstat)": word_counts_textstat,
    "Word Count (nltk)": word_counts_nltk,
    "Long Word Count (nltk)": long_word_counts_nltk,
    "Sentence Count (textstat)": sentence_counts_textstat,
    "Sentence Count (nltk)": sentence_counts_nltk,
    "LIX": lix_scores
}

df = pd.DataFrame(data, map(os.path.basename, html_files))

print(df)
