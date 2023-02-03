from colorama import Fore, Style

from TextRewrite import TextRewrite
from eliza import conversation_input
from samantha_loader import run_samantha

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    text_channel_list = []


users = {}


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id not in users:
        users[message.author.id] = run_samantha()
        inquery, starter = users[message.author.id]
        await message.author.send(starter())
    if message.guild:
        return

    inquery, starter = users[message.author.id]

    async with message.channel.typing():
        inp = str(message.content)
        txt = inquery(inp)
        if txt is not None:
            await message.author.send(txt)
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, txt)
            return

        respond = conversation_input(inp)
        work = tx.work(respond)
        rewrote_response = str(work)
        print("Generated: " + respond)
        print("Reworked: " + rewrote_response)
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, rewrote_response)
        await message.author.send(rewrote_response)


tx = TextRewrite()
client.run('Nzk2NDQyMTA1OTk1MTk4NTE0.GAJ9wo.INVpKBh3PdFcg7Rlb1kFBrlHKFDly0kicXn5IQ')
