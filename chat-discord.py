import pickle

import discord
import numpy as np
from keras.utils import pad_sequences
import keras

from load import load_intents

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
model = keras.models.load_model('chat_model')

# load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# parameters
max_len = 20

data = load_intents()
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    result = model.predict(pad_sequences(tokenizer.texts_to_sequences([message.content]),
                                         truncating='post', maxlen=max_len))

    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    # await message.channel.send(tag)

    for i in data['intents']:
        if i['tag'] == tag:
            choice = np.random.choice(i['responses'])
            print(choice)
            await message.channel.send(choice)


client.run('Nzk2NDQyMTA1OTk1MTk4NTE0.GAJ9wo.INVpKBh3PdFcg7Rlb1kFBrlHKFDly0kicXn5IQ')
