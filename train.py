import json
import os.path
import spacy
from CharacterAlreadyExistsException import CharacterAlreadyExistsException
from NoSuchCharacterEmotionException import NoSuchCharacterEmotionException
from NoSuchCharacterException import NoSuchCharacterException
from NoSuchTag import NoSuchTagError
from TextRewrite import TextRewrite
from nlp import nlp
from prepare import load_character_emotion_json_as_dict, get_character_emotion_intent_path


# only pass a starter if they can start in that state (usually only ever base)
def create_data(character, emotion, starter=""):
    data_path = get_character_emotion_intent_path(character, emotion)
    if os.path.exists(data_path):
        raise CharacterAlreadyExistsException()
    with open(data_path, 'w') as new_data:
        with open('empty.json', 'r') as template:
            data = template.read()
            tmp = json.loads(data)
            tmp['starter'] = starter
            new_data.write(json.dumps(tmp))
    return data


# Gets a list of responses ordered by dominate emotions
def get_data(character: str, emotion: str) -> []:
    data_path = get_character_emotion_intent_path(character, emotion)
    if not os.path.exists(data_path):
        raise NoSuchCharacterEmotionException()
    with open(data_path, 'r') as json_data:
        data = json.load(json_data)

    return data


# Gets a list of responses ordered by dominate emotions
def get_datas(character: str, emotions: [str]) -> []:
    datas = []
    for emotion in emotions.reverse():
        data_path = get_character_emotion_intent_path(character, emotion)
        if not os.path.exists(data_path):
            raise NoSuchCharacterEmotionException()
        with open(data_path, 'r') as json_data:
            data = json.load(json_data)
            datas.append(data)

    return datas


def save_tag(character, emotions, tag_name, tag_dict):
    for emotion in emotions:
        data_path = get_character_emotion_intent_path(character, emotion)
        data = load_character_emotion_json_as_dict(character, emotion)
        intent_emotion = data['intents']
        found = False
        item_count = len(intent_emotion)
        for j in range(item_count):
            if intent_emotion[j]['tag'] == tag_name:
                intent_emotion[j] = tag_dict

                found = True
        if not found:
            intent_emotion.append(tag_dict)
        with open(data_path, 'w') as tag_file:
            json.dump(data, tag_file)


def add_intent_input(character, emotions, tag_name, prompt):
    tag = get_tag(character, emotions, tag_name)
    if not tag:
        raise NoSuchTagError()
    tag['patterns'].append(prompt)
    save_tag(tag_name, tag)


def add_tag(character, emotions, tag_name, patterns=[], responses=[], emotion_influences={}):
    tag = {
        "tag": tag_name,

        "patterns": patterns,  # cleaned user input, stemmed and trunc'd, [{original,cleaned}]

        "responses": responses,  # now looks like [{text,personalityAffinity}]
        "emotionalComplexity": 1,  # min 1, max ???
        # what to say initially if a user starts a new session in this emotional state. aka sad.. go *sigh*
        # which personality trait to use as a the chance that they use a starter
        "starter": {"responses": []},

        "emotions": emotion_influences
    }
    save_tag(character, emotions, tag_name, tag)


def add_intent_response(character, emotions, tag_name, response):
    tag = get_tag(character, emotions, tag_name)
    if not tag:
        raise NoSuchTagError()
    tag['responses'].append(response)
    save_tag(tag_name, tag)


# the emotional response to triggering a tag. Can be empty.
def add_emotion_to_tag(character, emotions, tag_name, emotion, amount):
    tag = get_tag(character, emotions, tag_name)
    if not tag:
        raise NoSuchTagError()
    if emotion not in tag['emotion']:
        tag['emotion'][emotion] = amount
    else:
        tag['emotion'][emotion] += amount
    save_tag(tag)


# emotions is a list of emotions in order or priority to check for responses. For example, if anger is first, we check the anger intents for a response..
def get_tag(character, emotions, tag_name):
    data = get_data(character, emotions)
    tag = next(filter(lambda x: x['tag'] == tag_name, data['intents']))
    return tag


def generate_response_rewrite(text, amount, output):
    generator = TextRewrite(text)
    for index in range(amount):
        output.append(generator.work())
