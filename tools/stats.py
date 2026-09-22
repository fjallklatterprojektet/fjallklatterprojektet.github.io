import argparse
import glob
import os

import pandas as pd
import textstat
from bs4 import BeautifulSoup


def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()

    soup = BeautifulSoup(file_content, "html.parser")
    main_soup = soup.find("main")

    return "".join(main_soup.find_all(string=True)) if main_soup else ""

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to the directory")
parser.parse_args()

args = parser.parse_args()
path = args.path

html_files = glob.glob(path + "*.html", recursive=True)

textstat.set_lang("sv")
texts = map(extract_text_from_html, html_files)
word_counts = map(lambda t: textstat.lexicon_count(t, removepunct=True), texts)

df = pd.DataFrame(word_counts, map(os.path.basename, html_files))

print(df)
