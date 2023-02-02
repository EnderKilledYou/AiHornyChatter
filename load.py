import json
import os


def load_intents():
    with open('intents.json', 'r') as jsonx:
        data = json.load(jsonx)

    return data
