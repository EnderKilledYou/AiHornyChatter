import json

import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle

from load import load_intents
from load_helpers import get_character_labelencoder_emotion_path, get_character_tokenizer_emotion_path, \
    get_character_emotion_folder_path


def get_character_emotion_intent_path(character: str, emotion: str):
    return f'{character}.{emotion}.intents.json'


def prepare_character_emotion(character: str, emotion: str):
    data = load_character_emotion_json_as_dict(character, emotion)
    training_sentences = []
    training_labels = []
    labels = []
    for intent in data['intents']:
        for pattern in intent['patterns']:
            training_sentences.append(pattern)
            training_labels.append(intent['tag'])


        if intent['tag'] not in labels:
            labels.append(intent['tag'])
    num_classes = len(labels)
    lbl_encoder = LabelEncoder()
    lbl_encoder.fit(training_labels)
    training_labels = lbl_encoder.transform(training_labels)
    vocab_size = 1000
    embedding_dim = 16
    max_len = 20
    oov_token = "<OOV>"
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
    tokenizer.fit_on_texts(training_sentences)
    word_index = tokenizer.word_index
    sequences = tokenizer.texts_to_sequences(training_sentences)
    padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
    model.add(GlobalAveragePooling1D())
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.summary()
    epochs = 1500
    history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)
    model.save(get_character_emotion_folder_path(character, emotion))
    # to save the fitted tokenizer

    with open(get_character_tokenizer_emotion_path(character, emotion), 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # to save the fitted label encoder

    with open(get_character_labelencoder_emotion_path(character, emotion), 'wb') as ecn_file:
        pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)


def load_character_emotion_json_as_dict(character, emotion):
    with open(get_character_emotion_intent_path(character, emotion), 'r') as json_data:
        data = json.load(json_data)
    return data


if __name__ == 'main':
    dataz = load_intents()
    prepare_character_emotion('default', 'base', dataz)
