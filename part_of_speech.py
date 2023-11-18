import nltk
import requests
import string

try:
    data = requests.get(
        "https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt"
    )
except Exception:
    print("Not Found")
tags = {
    "CC": "conjunction",
    "CD": "number",
    "DT": "determiner",
    "EX": "existential there",
    "FW": "foreign word",
    "IN": "conjunction",
    "JJ": "adjective",
    "JJR": "adjective",
    "JJS": "adjective",
    "MD": "verb",
    "NN": "noun",
    "NNS": "noun",
    "NNP": "noun",
    "NNPS": "noun",
    "PDT": "predeterminer",
    "PRP": "pronoun",
    "PRP$": "pronoun",
    "RB": "adverb",
    "RBR": "adverb",
    "RBS": "adverb",
    "RP": "particle",
    "TO": "to-particle",
    "UH": "interjection",
    "VB": "verb",
    "VBD": "verb",
    "VBG": "verb",
    "VBN": "verb",
    "VBP": "verb",
    "VBZ": "verb",
    "WDT": "determiner",
    "WP": "pronoun",
    "WP$": "pronoun",
    "WRB": "adverb",
}

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

if data.status_code == 200:
    data = data.text
    for p in string.punctuation:
        if p in data:
            data = data.replace(p, "")

    tokens = nltk.word_tokenize(data)
    pos_lst = nltk.pos_tag(tokens)
    grouped_lst = []
    for item in pos_lst:
        token = list(item)
        token[1] = tags[item[1]]
        grouped_lst.append(token)
    freq_pos = {}
    for item in grouped_lst:
        if item[1] in freq_pos.keys():
            freq_pos[item[1]] += 1
        else:
            freq_pos[item[1]] = 1
    sorted_freq_pos = sorted(freq_pos.items(), key=lambda x: x[1], reverse=True)
    print(sorted_freq_pos)
