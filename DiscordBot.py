import time
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():#Displays message below as prompt on console to confirm that script is running
	print("MandiBot is up and running")

@client.event
async def on_message(message):
	senderID = message.author.id
	memberObject = message.author
	if (senderID != client.user.id):#This statement avoids the client from sending duplicate messages
		if message.content.upper().startswith(("!HEY")):#Responds with quick greeting
			await client.send_message(message.channel, "Whats up <@{}>?".format(senderID))
		if message.content == (("!xd") or ("!lmao")):
			await client.send_message(message.channel, "lol")
		if message.content.upper().startswith(("!HELP","!COMMANDS", "!HELP")):#Lists available commands **WILL ADD !JOINDATE after it becomes functional**
			await client.send_message(message.channel, "These are the current commands:\n\n!Hey: Bot sends greetings\n\n!xd or !lmao: Bot responds with acronym\n\n!members: Bot prints out names and nicknames of members")
		if message.content.upper().startswith(("!MEMBERS")):#Lists current server members, enumerating them by their ID and Server Nickname
			x = message.server.members
			index = 1
			for member in x:
				await client.send_message(message.channel, "{}.Name: {}\nNickname: '{}'".format(index, member.name, member.nick))
				index += 1
		if message.content.upper().startswith("!JOINDATE"):#Supposed to show the date on which you joined the server **Not Working**
			await client.send_message("Your join info is: {}".format(member.joined_at))



client.run("INSERT TOKEN HERE") #Individual Token from Discord *KEEP SECRET*
