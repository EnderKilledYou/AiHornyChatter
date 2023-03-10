import json
import urllib
import urllib.request
from nltk.corpus import wordnet

import spacy

from nlp import nlp


# shim
def unicode(s):
    return s

class BestSyn:

    def get_datamuse_syn_list(self):
        url = "https://api.datamuse.com/words?ml=" + self.word
        response = urllib.request.urlopen(url)
        data = response.read().decode("utf-8")
        json_data = json.loads(data)
        word_list = []
        for x in json_data:
            word_list.append(x['word'])
        return word_list

    def __init__(self, word):
        self.word = word
        self.best_score = 0.0
        self.best_choice = ""
        self.nlp = nlp
    def pull(self):
        words_list = self.get_datamuse_syn_list()
        for syn_word in words_list:
            use_nltk = True
            try:
                nltk_raw_word = wordnet.synsets(self.word)[0]
                nltk_syn_word = wordnet.synsets(syn_word)[0]
            except BaseException as b:
                use_nltk = False
                # todo: more specific exceptions

            spacy_raw_word = self.nlp(unicode(self.word.lower()))
            spacy_syn_word = self.nlp(unicode(syn_word.lower()))

            spacy_score = spacy_raw_word.similarity(spacy_syn_word)

            if use_nltk:
                nltk_score = nltk_syn_word.wup_similarity(nltk_raw_word)
                if nltk_score is None:
                    nltk_score = 0
                score = (nltk_score + spacy_score) / 2
            else:
                score = spacy_score

            if score > self.best_score:
                self.best_score = score
                self.best_choice = syn_word
        result = [self.best_score, self.best_choice]
        return result

    def __del__(self):
        self.word = False
        self.best_score = False
        self.best_choice = False
