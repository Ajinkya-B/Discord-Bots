"""
This is my first discord bot I created through a youtube tutorial! It is a simple bot
that looks for negative keywords a users text and replies them with positive message.
It also uses API to fetch a random inspiring quote on a user command.
Credit: https://www.youtube.com/watch?v=SPTfmiYiuok

Copyright and Usage Information
===============================
This file is Copyright (c) 2021 Ajinkya Bhosale.
"""

import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "angry", "unhappy", "miserable", "depressing"]

encouragements = ["Hang in there.",
                  "Cheer Up!",
                  "You are a great person",
                  "You’ve got this! Don't give up.",
                  "You can overcome any obstacle."]


# Helper function that fetches random API quotes
def get_quote():
    response = requests.get('https://zenquotes.io/api/quotes/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_encouragements(new_msg):
    if new_msg in db.keys():
        encouragements.append(new_msg)


@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith('$Hi'):
        quote = get_quote()
        await message.channel.send('Hello!')

    # send a random inspirational quote
    if msg.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(encouragements))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(os.environ['TOKEN'])  # put your token here
