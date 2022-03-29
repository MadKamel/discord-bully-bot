import discord, os

tokenfile = open("token", "r") #token go brrr
global MainGuild = 666313740672565269
global ISLogs = 958473856971067432

token = tokenfile.read()



client = discord.Client()

async def push_around(poor_user, channel_1, channel_2): #bullying function, for teasing people.
	while True:
		await poor_user.move_to(channel_1) #move them to one VC
		await poor_user.move_to(channel_2) #and then back

@client.event
async def on_ready():
	print(f'{client.user} is ready.') #

@client.event
async def on_message(message):
	print('A user speaks: "' + message.content + '".')
	split_msg = message.content.split(" ")
	if message.author == client.user:
		return

	if 'e' in split_msg or 'E' in split_msg:
		print('Message had "e" or "E"- send a gif.') #I honestly don't remember where I got this idea
		await message.channel.send("https://tenor.com/view/laugh-neptune-neptunia-nep-gif-7234123")

	if message.content.lower() == 'lol':
		print('Message was a permutation of "lol"- send a gif.')
		await message.channel.send("https://tenor.com/view/neptunia-laughing-neptune-lol-lmao-gif-10075190")



# Some code from other Discord Bots of mine, specifically RinnyBot. (remember that? where'd those days go off to?)

def loadchan(id): # Loads a channel
    global client
    print('Channel #' + str(client.get_channel(id)) + ' loaded.')
    return client.get_channel(id)

def loadrole(guild, id): # Loads a role from a specific guild
    print('Role <' + str(guild.get_role(id)) + '> loaded.')
    return guild.get_role(id)

def loadguild(id): # Loads a guild (server)
    global client
    print('Guild ' + str(client.get_guild(id)) + ' loaded.')
    return client.get_guild(id)

def loadmember(guild, id): # Loads a member from an id
    print('User @' + str(guild.get_member(id)) + ' loaded.')
    return guild.get_member(id)

async def setstatus(activity):
    global client
    print('Setting status to: ' + activity)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(activity))



client.run(token)
