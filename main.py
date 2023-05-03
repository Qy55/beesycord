import private
import discord
from discord.ext import commands


objIntents = discord.Intents.all()
objBot = commands.Bot(command_prefix="$", intents = objIntents)



@objBot.event
async def on_ready():
    print("Bot Online")
    

@objBot.command(aliases = ["안녕"])
async def hello(ctx):
    await ctx.send("world")
    
@objBot.command(aliases = ["계정신청"])
async def Register(ctx):
    pass

objBot.run(private.TOKEN)
print("init develop")