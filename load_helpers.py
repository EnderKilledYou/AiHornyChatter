import pickle

import keras


def get_character_labelencoder_emotion_path(character, emotion):
    return f'label_encoder.{character}.{emotion}.pickle'


def get_character_tokenizer_emotion_path(character, emotion, ):
    return f'tokenizer.{character}.{emotion}.pickle'


def get_character_emotion_folder_path(character, emotion):
    return f"chat_model_{character}_{emotion}"


model_cache = {}


def get_model_and_tokenizer_and_labeler_for_character_emotion(character, emotion):
    if character not in model_cache:
        model_cache[character] = {}
    if emotion not in model_cache[character]:
        with open(get_character_tokenizer_emotion_path(character, emotion), 'rb') as handle:
            tokenizer = pickle.load(handle)
        with open(get_character_labelencoder_emotion_path(character, emotion), 'rb') as enc:
            lbl_encoder = pickle.load(enc)

        model = keras.models.load_model(get_character_emotion_folder_path(character, emotion))
        model_cache[character][emotion] = (lbl_encoder, model, tokenizer)

    return model_cache[character][emotion]
