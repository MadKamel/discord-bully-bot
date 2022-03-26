import discord, os

tokenfile = open("token", "r") #token go brrr

token = tokenfile.read()



client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} is ready.')

@client.event
async def on_message(message):
    print('A user speaks: "' + message.content + '".')
    split_msg = message.content.split(" ")
    if message.author == client.user:
        return
    if 'e' in split_msg or 'E' in split_msg:
        print('Message had "e" or "E"- send a gif.')
        await message.channel.send("https://tenor.com/view/laugh-neptune-neptunia-nep-gif-7234123")
    if message.content.lower() == 'lol':
        print('Message was a permutation of "lol"- send a gif.')
        await message.channel.send("https://tenor.com/view/neptunia-laughing-neptune-lol-lmao-gif-10075190")

client.run(token)