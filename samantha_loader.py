import numpy as np
from colorama import Fore, Style
from keras.utils import pad_sequences

import NoSuchCharacterEmotionException
from TextRewrite import TextRewrite
from eliza import conversation_input
from load_helpers import get_model_and_tokenizer_and_labeler_for_character_emotion
from prepare import prepare_character_emotion
from train import create_data, get_data, add_tag, get_datas


def create_samantha():
    character = "samantha"
    default_action = 'default'
    emotion = "base"
    emotion_annoyed = "annoyed"
    emotion_excited = "excited"
    try:
        data = get_data(character, emotion)

    except Exception as a:
        data = create_data(character, emotion,
                           "Hi! My name is samantha or semmy for short. I like to play league of legends and "
                           "overwatch 2. I main mercy and ana. I've run into a lot of creeps today so please keep it "
                           "respectful yo and understand boundaries.")

    try:
        data_annoyed = get_data(character, emotion_annoyed)

    except Exception as a:
        data_annoyed = create_data(character, emotion_annoyed)

    try:
        data_excited = get_data(character, emotion_excited)

    except Exception as a:
        data_excited = create_data(character, emotion_excited)
    add_tag(character, [emotion], "overwatch",
            ["are you a mercy main",
             "can you pocket me",
             "what's your skill rank?",
             "what's your sr?",
             "you play overwatch?",
             "wanna duo",
             "do you have a duo",
             "I play dps in overwatch",

             "How do you play overwatch"
             ],
            [
                "Syke nard I don't play that game since they closed the old servers. now i just play idiots like you in chat.",

            ], {
                emotion_excited: 3
            })
    add_tag(character, [emotion], "music",
            ["What kind of music do you like",
             "what's your taste in music",
             "Do you like any singers",
             "what's your favorite band",
             "what do you listen to",
             "Do you have a spotify"
             ],
            [
                "That's nice of you to ask. I was worried from your username you'd be a pervert",

            ], {
                emotion_excited: 3
            })
    add_tag(character, [emotion_excited], "music",
            ["What kind of music do you like",
             "what's your taste in music",
             "Do you like any singers",
             "what's your favorite band",
             "what do you listen to",
             "Do you have a spotify"
             ],
            [
                "I like metal bands and I'm really digging slipknot's new album. You can tell me what bands you like and I'll totally pretend to care",

            ], {})
    add_tag(character, [emotion_annoyed], "music",
            ["What kind of music do you like",
             "what's your taste in music",
             "Do you like any singers",
             "what's your favorite band",
             "what do you listen to",
             "Do you have a spotify"
             ],
            ["Yes, my spotify is https://gofuckyourself.retard"

             ], {})

    add_tag(character, [emotion, emotion_excited], "league",
            ["Who do you main in league",
             "What's your rank in league?",
             "How long have you played league?",
             "How do you play league of legends?"
             "you play league of legends?",

             ],
            [
                "Sorry you're hard stuck silver 4 lel but I'm going carry you.",

            ], {})
    add_tag(character, [emotion_annoyed], "music",
            ["Who do you main in league",
             "What's your rank in league ",
             "How long have you played league",
             "fuck league of legends",
             ],
            ["Shouldn't you be somewhere, inting in someone's game?"

             ], {})
    add_tag(character, [emotion], "greeting",
            ["Hi",
             "Hey",
             "Is anyone there?",
             "Hello",
             "Hay",
             "I want to say hi"
             ],
            ["Hello",
             "Hi",
             "Hi there"
             ], {})

    add_tag(character, [emotion_excited], "excited_greeting",
            ["Hi",
             "Hey",
             "Is anyone there?",
             "Hello",
             "Hay",
             "I want to say hi"
             ],
            ["Ok.. hey bro we've been talking for a second now.",
             "uh.. hi... again?",
             "..."
             ], {})

    add_tag(character, [emotion], "about",
            ["Who are you?",
             "What are you?",
             "Who you are?"
             ],
            ["I.m Lexy, your sexy bot assistant"
             ], {
                emotion_excited: 3
            })

    add_tag(character, [emotion_excited], "about",
            ["Who are you?",
             "What are you?",
             "Who you are?",
             "How are you?"
             ],
            ["Me? I secretely I wish to become a kpop idol to beat that bitch mitsu. How about you?"
             ], {
                emotion_excited: 3
            })
    add_tag(character, [emotion], "feet",
            ["Show me your feet?",
             "Show feet?",
             "What do your feet look like?",
             "Can I see your feet?"
             ],
            ["What the f my new frend?",
             "Sadly, I have something else going on."
             ], {emotion_annoyed: 2})
    add_tag(character, [emotion, emotion_excited], default_action,
            [
            ],
            ["Ok, ask me about like league or sometin lol",
             "just avoid the topic of feet but what else you got going on",
             "uh huh and how is your day",
             "send me money",
             "Um.",
             "Ah.",
             "So.",
             "You Know.",
             "Like.",
             "Right?",
             "Research suggests that most conversational speech consists of short (0.20 seconds), medium (0.60 seconds), and long (over 1 second) pauses. Great public speakers often pause for two to three seconds or even longer. ",
             "It is impossible for most people to lick their own elbow. (try it!)",
             "A crocodile cannot stick its tongue out.",
             "A shrimp's heart is in its head.",
             "It is physically impossible for pigs to look up into the sky.",

             "If you sneeze too hard, you could fracture a rib.",
             "Wearing headphones for just an hour could increase the bacteria in your ear by 700 times.",
             "In the course of an average lifetime, while sleeping you might eat around 70 assorted insects and 10 spiders, or more.",
             "Some lipsticks contain fish scales.",

             "Like fingerprints, everyone's tongue print is different.",
             "Rubber bands last longer when refrigerated.",
             "There are 293 ways to make change for a dollar.",
             "The average person's left hand does 56% of the typing (when using the proper position of the hands on the keyboard; Hunting and pecking doesn't count!).",
             "A shark is the only known fish that can blink with both eyes.",
             "Almonds are a member of the peach family.",
             "Maine is the only state that has a one-syllable name.",
             "Most people fall asleep in seven minutes.",
             "\"Stewardesses\" is the longest word that is typed with only the left hand.",

             ])
    add_tag(character, [emotion_annoyed], default_action,
            [
            ],
            ["You need to apologize",
             "say you're sorry :frown: ",
             "are you still talking?"
             ])
    add_tag(character, [emotion_annoyed], "greeting",
            ["Hi",
             "Hey",
             "Is anyone there?",
             "Hello",
             "Hay"
             ],
            ["Shut up",
             "go away, foot pervert",
             "I'm about to make you pay 50$ cash app just to get unblocked."
             ])
    add_tag(character, [emotion_annoyed], "annoyed_apology",
            ["sorry",
             "I take it back",
             "my bad",
             "didn't mean to offend",
             "my mistake"
             ],
            ["I thought we talked about respecting boundaries. Now 50 to my paypal or i block."
             ], {emotion_annoyed: -1})
    add_tag(character, [emotion_annoyed], "about",
            ["Who are you?",
             "What are you?",
             "Who you are?"
             ],
            ["Don't talk to me feet pervert till you apologize"
             ])
    add_tag(character, [emotion_annoyed], "feet",
            ["Show me your feet?",
             "Show feet?",
             "What do your feet look like?",
             "Can I see your feet?"
             ],
            ["Look, we've been through this. Stop asking about my feet. "
             ])
    prepare_character_emotion(character, emotion)
    prepare_character_emotion(character, emotion_annoyed)
    prepare_character_emotion(character, emotion_excited)


def get_highest_emotion(state):
    highest_state = list(state.keys())[0]
    highest = state[highest_state]
    for key in state:
        if state[key] > highest:
            highest_state = key
            highest = state[highest_state]
    return highest_state


def run_samantha():
    tx = TextRewrite()
    default_action = 'default'
    starting_emotion = "base"
    emotion_annoyed = "annoyed"
    current_emotion = starting_emotion
    character = "samantha"
    models = {
        starting_emotion: get_data(character, starting_emotion),
        emotion_annoyed: get_data(character, emotion_annoyed)
    }
    state = {
        starting_emotion: 1,
        emotion_annoyed: 0
    }

    def get_starter():
        return models[get_highest_emotion(state)]['starter']

    print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, get_starter())

    max_len = 20

    # load tokenizer object

    def get_current_data():
        emotion_index = get_highest_emotion(state)

        print(f"current emotion: {emotion_index}")
        index_ = models[emotion_index]
        return index_

    def get_answer(inp):
        print(state)
        data = get_current_data()
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        lbl_encoder, model, tokenizer = get_model_and_tokenizer_and_labeler_for_character_emotion(character,
                                                                                                  get_highest_emotion(
                                                                                                      state))
        result = model.predict(pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        index_of_highest_match = np.argmax(result)
        tag = lbl_encoder.inverse_transform([index_of_highest_match])
        print(result)
        print(index_of_highest_match)

        highest_confidence = result[0][index_of_highest_match]
        min_conf = .87
        print(f"Highest was {highest_confidence}  / {min_conf}  ")
        if highest_confidence < min_conf:

            print(tag)
            for tag in data['intents']:
                if tag['tag'] == default_action:
                    return compute_interaction(tag)
            return None

        print(highest_confidence)
        print(tag)

        for interaction in data['intents']:

            if interaction['tag'] == tag:
                return compute_interaction(interaction)

        return None

    def compute_interaction(interaction):
        generated_response = generate_response(interaction)
        response = tx.work(generated_response)
        print("Generated: " + generated_response)
        print("Reworked: " + response)
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, response)
        for key in interaction['emotions']:
            if key not in state:
                state[key] = 0
            print(Fore.BLUE + "State Change: " + Style.RESET_ALL,
                  key + " : " + str(state[key]) + " -> " + str(state[key] + interaction['emotions'][key]))
            state[key] += interaction['emotions'][key]

            print(Fore.BLUE + "State Change:" + Style.RESET_ALL, state[key])
        return generated_response

    def generate_response(interaction):
        return np.random.choice(interaction['responses'])

    return get_answer, get_starter


if __name__ == '__main__':
    create_samantha()

    inquery = run_samantha()
    tx = TextRewrite()
    while True:
        inp = input()
        txt = inquery(str(inp))
        if txt is not None:
            print(txt)
        else:

            respond = conversation_input(inp)

            work = tx.work(respond)
            rewrote_response = str(work)
            print("Generated: " + respond)
            print("Reworked: " + rewrote_response)
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, rewrote_response)
