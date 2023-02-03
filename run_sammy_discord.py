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
    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send(starter())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    async with message.channel.typing():
        inp = str(message.content)
        txt = inquery(inp)
        if txt is not None:
            await message.channel.send(txt)
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, txt)
            return

        respond = conversation_input(inp)
        work = tx.work(respond)
        rewrote_response = str(work)
        print("Generated: " + respond)
        print("Reworked: " + rewrote_response)
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, rewrote_response)
        await message.channel.send(rewrote_response)


inquery, starter = run_samantha()
tx = TextRewrite()
client.run('Nzk2NDQyMTA1OTk1MTk4NTE0.GAJ9wo.INVpKBh3PdFcg7Rlb1kFBrlHKFDly0kicXn5IQ')
