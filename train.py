from NoSuchTag import NoSuchTagError
from TextRewrite import TextRewrite


def get_data(character, emotions):
    return {}


def save_tag(character, emotions, tag_name, tag_dict):
    pass


def add_intent_input(character, emotions, tag_name, prompt):
    tag = get_tag(character, emotions, tag_name)
    if not tag:
        raise NoSuchTagError()
    tag['patterns'].append(prompt)
    save_tag(tag_name, tag)


def add_tag(character, emotions, tag_name):
    tag = {
        "tag": tag_name,
        "patterns": [

        ],
        "responses": [

        ],
        # what to say initially if a user starts a new session in this emotional state. aka sad.. go *sigh*
        # which personality trait to use as a the chance that they use a starter
        "starter": {"responses": []},
        "personalityState": "",  # the current personality trait that is dominate and determines roles
        "personality": {
            "aggressive": 0,
            "passive": 0,
            "horny": 0,
            "depressed": 0,
            "dominating": 0,
            "quirky": 0,
            "gamer": 0,
            "scary": 0,
            "promiscuous": 0
        },
        "emotions": {}
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
