from nltk.corpus import wordnet
import spacy

from BestSyn import BestSyn
from nlp import nlp


class TextRewrite:

    def work(self, sentence):
        return str(sentence)
        """
        @var rewrite_types: Type of words that can rewrited
        """
        rewrite_types = [u'NN', u'NNS', u'JJ', u'JJS']
        pos_tokenizer = nlp(str(sentence))
        words = []
        for token in pos_tokenizer:
            if token.tag_ in rewrite_types:
                words.append(token.text)
        rewrited_sentence = sentence
        for word in words:
            word_syn = BestSyn(word).pull()[1]
            rewrited_sentence = rewrited_sentence.replace(word, word_syn)
        return rewrited_sentence

    def __del__(self):
        self.sentence = False
