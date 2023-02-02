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

        ],  # cleaned user input, stemmed and trunc'd, [{original,cleaned}]

        "responses": [

        ],  # now looks like [{text,personalityAffinity}]
        "emotionalComplexity": 1,  # min 1, max ???
        # what to say initially if a user starts a new session in this emotional state. aka sad.. go *sigh*
        # which personality trait to use as a the chance that they use a starter
        "starter": {"responses": []},
        "personalityState": "",  # the current personality trait that is dominate and determines roles
        # this matches an emotion for a amplification to the top two emotions that are greater minthreshold
        "personality": {
            "aggressive": [],  # [{emotion,amplyifyAmount,minThresh}]
            "passive": [],
            "horny": [],
            "depressed": [],
            "dominating": [],
            "quirky": [],
            "gamer": [],
            "scary": [],
            "promiscuous": []  # p.s. promiscuous is NOT an emotion.
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
