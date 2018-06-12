import discord
from discord.ext import commands

description = '''
I'm on it.
'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def whoru():
	"""Who am i?"""
	await bot.say("I am Fillmore.")

try:
	f = open('token')
	tok = f.readline().strip()
	bot.run(tok)
except OSError:
	print("Token file not found!")