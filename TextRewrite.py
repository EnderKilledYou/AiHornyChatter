from nltk.corpus import wordnet
import spacy
import urllib
import json

from BestSyn import BestSyn

nlp = spacy.load('en')


class TextRewrite:

    def __init__(self, sentence):
        self.sentence = sentence

    def work(self):
        """
        @var rewrite_types: Type of words that can rewrited
        """
        rewrite_types = [u'NN', u'NNS', u'JJ', u'JJS']
        pos_tokenizer = nlp(unicode(self.sentence))
        words = []
        for token in pos_tokenizer:
            if token.tag_ in rewrite_types:
                words.append(token.text)
        rewrited_sentence = self.sentence
        for word in words:
            word_syn = BestSyn(word).pull()[1]
            rewrited_sentence = rewrited_sentence.replace(word, word_syn)
        return rewrited_sentence

    def __del__(self):
        self.sentence = False
