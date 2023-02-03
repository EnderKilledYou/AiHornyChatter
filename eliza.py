#!/usr/bin/env python3
"""
Created on Wed Sep 15 05:44:06 2021
AIT 526
Eliza Chat bot - Programming Assignment 1
@author: Team 1 - Alice Chen, Hrishikesh Karambelkar, Prakriti Panday, Sean Park
"""
# import all the necessary packages
import datetime
import random
import re

from nltk.tokenize import word_tokenize

# model dictionary where the key words are defined as well as the responses.
model = {

    r'.*(kids?|child(ren)?).*':
        [
            "Can you tell me more about your %s?",
            "How would you describe your relationship with your %s?",
            "What do you enjoy doing with your %s?"
        ],
    r'i lost (.*)':
        [
            "I'm sorry to hear that. Can you tell me what happened?",
            "That must be tough. How are you feeling now?",
            "How are you dealing with the loss of %s?"
        ],
    r'.*(depress(ed)|sad|pressured?|stress(ed)?).*':
        [
            "How often do you feel %s?",
            "Have you talked to anyone about how you are feeling?",
            "Is there anything you enjoy doing so you don't feel %s?",
            "How do you prefer managing feeling %s?"
        ],
    r'.*(kill(ing|ed)?|suicide|die).*':
        [
            "Please stop dwelling on such thoughts. Do you share these thoughts with others in your life?",
            "Would you like to call the National Suicide Prevention Lifeline at 1-800-273-8255 (Talk)? The toll-free confidential Lifeline is available 24 hours a day, seven days a week",
            "This eliminates the possibility of improving the situation. Surely, we can find a solution"
        ],
    r'.*(job|work|career).*':
        [
            "Do you like what you do?",
            "Can you tell me more about your %s?",
            "How do you feel about your %s?"
        ],
    r'.*(covid|lockdown|masks|pandemic).*':
        [
            "Although best for us, the new norm has been difficult to adjust to.",
            "Such occurrences have been natural to human history. Surely, we can overcome it.",
            "How has it affected your life?"
        ],
    r'i hate (.*)':
        [
            "When did you decide you truly hate %s?",
            "Were there incidents that made you come to this conclusion?",
            "Could you share few reasons why you hate %s?"
        ],
    r'.*(anxiety|panic|fear|tremble).*':
        [
            "How do you usually manage such situations?",
            "How long has this been part of your life?",
            "There can be ways to manage this and continue with your daily routines"
        ],
    r'(.*) makes me happy':
        [
            "That’s wonderful. You should continue to pursue such feelings.",
            "Are there other feelings you associate with %s?",
            "How often do you make time for %s?"
        ],
    r'how can i stop (.*)':
        [
            "Well what reasons typically can you associate with %s?",
            "What avenues have you pursued in the past?",
            "Has %s been recent or ongoing for some time?"
        ],
    r'i am not ready (.*)':
        [
            "What makes you think you’re not ready %s?",
            "Did you at least try %s?",
            "What do you think you can do to prepare %s?"
        ],
    r'i don\'?t? want(.*)':
        [
            "Have you ever wanted %s?",
            "Is there a reason why you don't want %s?",
            "Do you want something else?",
            "What do you want now then?"
        ],
    r'(.*)divorce(.*)':
        [
            "Are you sure about pursuing this choice?",
            "What happened?",
            "Have you talked to your partner about this choice?"
        ],
    r'(.*)':
        [
            "Can you tell me more about it?",
            "Would you mind sharing more about it?",
            "Please tell me more.",
            "How does that make you feel?",
            "I would like to hear more about this.",
            "Have you talked to anyone about this?"
        ],

}

# pronoun dictionary for transformation
pronoun = {
    "you": "me",
    "yours": "mine",
    "your": "my",
    "you will": "I will",
    "you have": "I have",
    "you can": "I can",
    "me": "you",
    "mine": "yours",
    "my": "your",
    "I will": "you will",
    "I have": "you have",
    "I can": "you can"

}


def replace_pronouns(match):
    """replace pronouns to transform 2nd pov to 1st pov and 1st pov to 2nd pov, vice versa."""
    tokenizer = word_tokenize(match)

    # call the pronoun definition and replace the element in tokenizer, join the tokens, and return tokenizer
    for x, token in enumerate(tokenizer):
        if token in pronoun:
            tokenizer[x] = pronoun[token]
    return ' '.join(tokenizer)


def conversation_input(user_input):
    """Returns Eliza's answer for the user input."""

    for pattern, responses in model.items():
        # checks for matching input vs the key
        ans = re.search(pattern, user_input.rstrip(",.!"))
        # if the key matches the input, returns (prints) the "response"
        if ans:
            # the response will be randomly returned out of all the given "conversation_dict" under its key word
            response = random.choice(responses)
            # if the question in "conversation_dict" includes "%s," the response will return with the information
            # from the input
            if "%s" in response:
                match = ans[1]
                # when and if the key word include 2nd or 1st pov ("you" or "me"), it will transform to 1st or 2nd
                # pov vice versa.
                response = response % (replace_pronouns(match))
                return response
            else:
                return response


def process(user_name):
    """This is the core Chat bot engine. Check input user name and return a greeting message, "Eliza: Welcome %s.
    What would you like to share with me today?" with the user name replaced in %s. """
    print("Eliza: Welcome %s. What would you like to share with me today?" % user_name)
    # standard expression for bye
    end = [r'.*bye.*', r'.*exit.*']
    user_continue = True
    while user_continue:
        # check and get input name and information
        user_input = input('%s: ' % user_name)
        print()
        # convert input into lowercase
        user_input = user_input.lower()

        # check for "end" input such as 'bye' or 'exit'
        for i in end:
            user_exit = re.findall(i, user_input)
            # if there is an "end" input, exit the while loop
            if len(user_exit) != 0:
                user_continue = False
        # if there is no "end" input, continue and return an appropriate response
        if user_continue:
            response = conversation_input(user_input)
            print("Eliza: " + response)


def greet():
    """Additional functionality to greet with a proper time of the day: morning, afternoon, and evening. """
    current_time = datetime.datetime.now()
    # if user time zone is before 12:00pm, greet with "Good morning."
    if current_time.hour < 12:
        return "Good morning."
    # if user time zone is or after 12:00pm and before 6:00pm , greet with "Good afternoon."
    elif 12 <= current_time.hour < 18:
        return "Good afternoon."
    # otherwise greet with "Good evening."
    else:
        return "Good evening."


def end():
    """Additional functionality to end the chat with a proper time of the day: morning, afternoon, and evening. """
    current_time = datetime.datetime.now()
    # if user time zone is before 12:00pm, end with "great morning."
    if current_time.hour < 12:
        return "great morning."
    # if user time zone is or after 12:00pm and before 6:00pm, end with "great afternoon."
    elif 12 <= current_time.hour < 18:
        return "great afternoon."
    # otherwise end with "great evening."
    else:
        return "great evening."


def initiate_conversation():
    """Initiate dialogue and return message with user name input along with extra functionality datetime greeting. """
    print("Eliza: %s I'm Eliza, a psychotherapist. Who do I have the pleasure of speaking to today?" % greet())
    # initialize user name input
    name_input = input('User: ')
    print()
    # tokenize user name input
    tokenizer = word_tokenize(name_input)
    # use the last word as user name if name
    user_name = tokenizer[-1]
    return user_name
