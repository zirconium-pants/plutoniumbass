# PlutoniumBass_v1.2

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random

bot = commands.Bot(command_prefix='p!')

gayList = ['gay', 'gei', 'ghei', 'homosexual', 'ghey', 'gey', 'homo', 'bisexual', 'bi', 'attracted to other human beings of the same gender']
jokeList = ["I'll stop you right there", \
            "This is a vaquita\n (Image loading...)", \
            "I never trust stairs. They're always **up** to something.", \
            "I don't like elevators, and have begun taking **steps** to avoid them", \
            "I tried to grab fog, but I mist...", \
            'One day, two guys are looking over a hillside. One guy says to the other guy "See that house over there? I made that. But do they call me the Housemaker? See that Church over there? I made that too. But do they call me the Chruch builder? No. They don\'t call me the House maker or the Church builder. But you kiss a pig once...."', \
            'A pirate captured a sailor and offered the sailor to become a pirate or die. The sailor thought for a moment and said, "I will join you if you can impress me with facts about yourself. I only follow people I respect." So the pirate pointed to his prosthetic leg and said "See this? I lost this to a shark. The shark bit off my leg, but I killed the shark in the end." The sailor was very impressed, but didn\'t want to give in just yet. Seeing the sailor\'s hesitation, the pirate said "See this hook? I lost my hand in a battle against the British Navy. I drove them all off even though I was outnumbered 3-1." The sailor was now very impressed. He said "I am very impressed. But do you mind telling me the story behind your eyepatch? I\'m sure it must have been an epic tale." The pirate said, "Nah, I lost my eye because a bird pooped on it." The sailor was very confused. He said, "How did that cause you to lose youreye?" The pirate replied "I used the wrong hand to wipe it off."', \
            "I went to the zoo the other day, but there was only one dog in it. It was a shitzu.", \
            "Where do pirates with hook hands go to replace their hooks? The *second hand* store.", \
            
            #"", \
            ]

@bot.event
async def on_ready():
    print ("Readied Up!")
    print ("User(Bot): " + bot.user.name)
    print ("Bot ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='Use p!help'))

#    help_info = "Commands: (Prefix = '!plat')\n"
#    help_info += "help - Prints this out\n"
#    help_info += "truth - Prints an ancient GoG proverb\n"
#    help_info += "ping - pong?\n"
#    help_info += "info (@user) - Prints info about the user\n"

@bot.command(pass_context=True)
async def version(ctx):
    await bot.say("Version 1.1\n"
        + " - Go ahead and say that your favorite arctic researcher is gay. Do it.\n" \
        + " - Added 'wiki' command\n" \
        + " - Added 'joke' command\n" \
        + " - Bought more plutonium as a midnight snack")
    

@bot.event
async def on_message(message):
    for x in gayList:
        if ('Mei is ' + x) in message.content:
            await bot.send_message (message.channel, "Mei is NOT ghey you hoser.")
            break
        if ('mei is ' + x) in message.content:
            await bot.send_message (message.channel, "Mei is NOT ghey you hoser.")
            break
    await bot.process_commands(message)
    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("PONG PONG")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}\n".format(user.name) \
        + "The users ID is: {}\n".format(user.id) \
        + "The users status is: {}\n".format(user.status) \
        + "The users highest role is: {}\n".format(user.top_role) \
        + "The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def truth(ctx):
    await bot.say('"The truth hurts, buddy."')

@bot.command(pass_context=True)
async def ready(ctx):
    await bot.say('"Get ready to shooty-shoot."')

@bot.command(pass_context=True)
async def thinkthrower(ctx):
    await bot.say('"Thinkthrower activate! :fire::fire::fire:<:plat_think:363509504266076160>"')

@bot.command(pass_context=True)
async def bug(ctx):
    await bot.say('"big bug ghey"')

@bot.command(pass_context=True)
async def gang(ctx):
    await bot.say("Link: https://youtu.be/Zz4X5vmXixc")
    await bot.say("__Gucci Gang Platinum Parody (By Mr. Foster):__\n   " \
        + "Plattie Gang, ooh, yeah, Lil Bass, yeah, Plattie gang, ooh\n   " \
        + "(Intro) Plattie gang, Plattie gang, Plattie gang, Plattie gang, Plattie gang, Plattie gang, Plattie gang\n   " \
        + "I make a new meme erry day\n   " \
        + "My boi Toom make emojis rain, ooh\n   " \
        + "I made a meme, I forgot its name\n   " \
        + "I won't buy a meme no wedding ring\n   " \
        + "Rather read GoG anime\n   " \
        + "Plattie gang, Plattie gang, Plattie gang\n   " \
        + "(Repeat Intro)\n   " \
        + "My memes worth more than your rent, ooh\n   " \
        + "Yer mum still live in a tent, yuh\n   " \
        + "All of my memes be dank, huh\n   " \
        + "All o your memes stank, ooh\n   " \
        + "None of these memes be new to me\n   " \
        + "If you laugh at 'em, you a normie\n   " \
        + "Bought some :plat_loaf: shirts, cost hella Gs\n   " \
        + "Gon' turn Plat Merch to a company\n   " \
        + "Boi, your breath smell like Mountain Dew\n   " \
        + "You better have some Doritos too\n   " \
        + "They gave me CEO cause I'm the best\n   " \
        + "Now Lil Bass fly a private jet\n   " \
        + "Everybody screaming 'Nice Jet!'\n   " \
        + "Lil Bass memes be the best\n   " \
        + "Hunnid on my wrist spend it all quick\n   " \
        + "Selling loaf shirts, buy em with a click\n   " \
        + "(Repeat Intro)")

@bot.command(pass_context=True)
async def stop(ctx):
    await bot.say('"I\'ll stop you right there."')

@bot.command(pass_context=True)
async def mei(ctx):
    await bot.say('"Mei is NOT ghey, you hoser."')

@bot.command(pass_context=True)
async def csgobot(ctx):
    await bot.say("Stop it, for the love of God.")

@bot.command(pass_context=True)
async def song(ctx):
    await bot.say(":guitar:<:plat_think:363509504266076160>:thumbsup:\n" \
        + "strum strum strummmm\n" \
        + "ON THE TABLE\n" \
        + "ICE CUBE ICE CUBE\n" \
        + "IN THE WAY\n" \
        + "ICE CUBE ICE CUBE\n" \
        + "ON THE FLOOR\n" \
        + "ICE CUBE ICE CUBE\n" \
        + "MEI'S NOT GHEI\n" \
        + "strum strum strummmmm\n" \
        + ":plat_bow:")

@bot.command(pass_context=True)
async def wiki(ctx):
    await bot.say("Here's the main page for the wiki: https://platinumbass-universe.wikia.com/wiki/PlatinumBass_Universe_Wiki")

@bot.command (pass_context=True)
async def joke(ctx):
    x = random.randint(0, len(jokeList) - 1)
    await bot.say(jokeList[x])
    
# @bot.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
#    await bot.kick(user)

bot.run(TOKEN)
