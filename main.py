import discord
from discord.ext import commands
import os
import asyncio
import asyncpixel
import math 
import motor.motor_asyncio
import urllib.request as ur
import time 
import json
import string
import requests

import urllib
from random import randint
from pprint import pprint
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
from num2words import num2words
import subprocess
import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
def prefix(client, message):
    try:
        with open("prefixes.json", 'r') as q:
            prefixes = json.load(q)

        return prefixes[str(message.guild.id)]
    except:
        pass

songs = asyncio.Queue()
play_next_song = asyncio.Event()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("I am online")

    x = datetime.datetime.now()
    x = x.strftime("%m")
    x = int(x) - 1
    with open('status1.txt') as f:
      lines = f.read().splitlines()
    statusfinal = lines[x]
    game = discord.Game(statusfinal)
    await bot.change_presence(status=discord.Status.online, activity=game)
    subprocess.call(["python", "stablereleasedatetimestatus.py"])


@bot.command(aliases=["69"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def _69(ctx):
    ctx.send("WOW YOU ARE SO FUNNY IM LAUGHING SO HARD\n...")
 
@bot.command()
async def setup(ctx):
    with open("prefixes.json", 'r') as q:
        prefixes = json.load(q)

    a1 = str(ctx.guild.id)
    try:
        a2 = prefixes[a1]
        await ctx.send("__*You've already set up George.__* \nDo you want to erase all settings and setup again [erase], or do you want to keep the settings?[keep]\n**                 **\n***KEEP IN MIND***\n**Please type the word specified in the brackets ([]) or else it will not work.**")
    except:
         await ctx.send("Hello, and thank you for adding ***George the bot*** to your server!")


@bot.command(invoke_without_command=True,aliases=['h','helpme'])
async def help(ctx):
    await ctx.send("yes")


@bot.event
async def on_guild_join(guild):
    guildid = guild.id
    a_dictionary = {guildid: "<"}

    with open("premium.json", "r+") as file:
        data = json.load(file)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
    b_dictionary = {guildid: "justno"}

    with open("prefixes.json", "r+") as file:
        data = json.load(file)
        data.update(b_dictionary)
        file.seek(0)
        json.dump(data, file)

    for general in guild.text_channels:
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="Thank you for inviting George!",
                                  description="George the bot is a great bot that combines simplicity into setting up the bot, and also is a great experience for users. \nFor help type: '<help' ")
            embed.set_author(name="George")
            embed.set_thumbnail(url="https://lh3.googleusercontent.com/-ByQF9xuuVsw/X-5SZFyW9JI/AAAAAAAABNo/oj8-p9-mhx4JyMaz_1qG7AFYcVhK7u0sgCLcBGAsYHQ/s0/georgehello.gif")
            await general.send(embed=embed)
            await general.send("To get started, type '<setup'!")
            return



@bot.command()
async def birthday(ctx):
    await ctx.send("HAPPY BIRTHDAY.........WAIT. \n Who's birthday is it? Can the birthday boy/girl say 'me'?")

    def check(m):
        return m.content == 'me' and m.channel == ctx.channel

    msg = await bot.wait_for('message', check=check)
    await ctx.send('HAPPY BIRTHDAY {.author}!'.format(msg))

@bot.command()
async def prefix(ctx, prefix):
    if prefix == None:
        ctx.send("You didn't add a prefix to change to!")
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    changed_prefix = prefixes[str(ctx.guild.id)]

    embed1=discord.Embed(title=f'Prefix Changed for {ctx.guild.name}!',description=f"You changed it to:   **{changed_prefix}** \n Remember this prefix so you don't lose it !",color=0xfffffd)
    embed2=discord.Embed(title=f'Prefix Changed for {ctx.guild.name}!',description=f"You changed the prefix to:   **{changed_prefix}** \n \n Remember this and don't forget! \n \n Enter {prefix}prefix [the new prefix] to change it!",color=0xfffffd)

    await ctx.channel.send(embed=embed2)
    await ctx.author.send(embed=embed1)
"""
Hypixel commands lol
"""
def getInfo(call):
    r = requests.get(call)
    return r.json()
api_key = '61817beb-03e7-4984-930e-33fc64aad848'

@bot.command(aliases=["sbstats"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def skyblockstats(ctx, arg):
    uuid = requests.get(f"https://api.ashcon.app/mojang/v2/user/{arg}").json()["uuid"]
    ProfileIdLink = requests.get("https://api.hypixel.net/player?key=" + api_key + "&uuid=" + uuid).json()
    ProfileId = list(ProfileIdLink['player']['stats']['SkyBlock']['profiles'].keys())[0]

    data = requests.get("https://api.hypixel.net/skyblock/profile?key=" + api_key + "&profile=" + ProfileId).json()
    print("https://api.hypixel.net/skyblock/profile?key=" + api_key + "&profile=" + ProfileId)
    CoinPurse = int(data['profile']['members'][ProfileId]['coin_purse'])
    CoinPurse = math.floor(CoinPurse)

    tdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths'])
    vdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_void'])
    spiderdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_spider'])
    endermandeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_enderman'])
    skeledeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_skeleton'])
    zombiedeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_zombie'])
    frostydeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_frosty_the_snowman'])
    seaguardiandeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_sea_guardian'])
    lapiszombiedeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_lapis_zombie'])
    redstonepigmandeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_redstone_pigman'])
    voraciousspiderdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_voracious_spider'])
    cryptdreadlorddeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_crypt_dreadlord'])
    dungeonskeletondeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_dungeon_respawning_skeleton'])
    cryptlurkerdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_crypt_lurker'])
    skeletongruntdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_skeleton_grunt'])
    zombiegruntdeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_zombie_grunt'])
    scaredskeletondeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_scared_skeleton'])
    falldamagedeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_fall'])
    diamondzombiedeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_diamond_zombie'])
    diamondzombiedeaths = int(data['profile']['members'][ProfileId]['stats']['deaths_diamond_skeleton'])
    image = f"http://photopass.appspot.com/3d.php?user={arg}&vr=-25&hr=35&hrh=0&vrll=0&vrrl=0&vrla=0&vrra=0&displayHair=true&headOnly=false&format=png&ratio=40&aa=false&layers=true"
    values = []
    response = requests.get(image)


    ak = f"https://sky.shiiyu.moe/api/v2/profile/{arg}"
    aki = urllib.request.urlopen(ak)
    for keys in aki.values():
        if "deaths" in keys:
            values.append(keys)
    file = open("image.png", "wb")
    file.write(response.content)
    file.close()
    arg1 = string.capwords(arg)
    test1 = "For " + arg
    embed=discord.Embed(title="Skyblock Stats", description=test1)
    embed.set_thumbnail(url=image)
    Health = "<:Health_icon:834163104266584085>Health"
    embed.add_field(name=Health, value=arg1, inline=False)
    await ctx.send("<:Health_icon:834163104266584085>")
    if os.path.exists("image.png"):
        os.remove("image.png")
    else:
        print("Something went wrong [GeorgeError0]")

    print(CoinPurse)
"""
https://api.hypixel.net/skyblock/profile?key=61817beb-03e7-4984-930e-33fc64aad848&profile=ff4d71f018e74e49953ab349d02eed01
https://api.hypixel.net/skyblock/profile?key=61817beb-03e7-4984-930e-33fc64aad848&profile=
https://api.hypixel.net/skyblock/profile?key=61817beb-03e7-4984-930e-33fc64aad848&uuid=ff4d71f0-18e7-4e49-953a-b349d02eed01
"""



# TEST COMMAND
# THIS COMMAND IS ONLY FOR TESTING PURPOSES
#
#
@bot.command(aliases=["A"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def actionA(ctx):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefix = prefixes[str(ctx.guild.id)]

    embed = discord.Embed(title="Help for George",
                       description=f'Use {prefix}help <command> for extended information on a command.', color=0xFFFF00)
    embed.add_field(name='Moderation', value='kick, ban, unban, mute, unmute', inline=True)
    embed.add_field(name='Info', value='invite, prefix', inline=False)
    embed.add_field(name='Fun', value='8ball, echo, minecraft, valorant, minecraft', inline=True)
    embed.add_field(name='Server', value='delete, new, rename', inline=True)
    await ctx.send(embed=embed)

@actionA.error
async def A_error(ctx, error):
    error = str(error)
    errorone = error[33:-1]
    embed = discord.Embed(title="Error", color=0xff0000)
    name1 = "There are still "+str(errorone)+" seconds until you can use this command again!"
    embed.add_field(name=name1,
                    value="If you want to use this command without cooldowns, get George the bot Premium!",
                    inline=False)
    embed.set_footer(text="...")
    await ctx.send(embed=embed)

@bot.command(aliases=["B"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def actionB(ctx):
    embed = discord.Embed(title="Hi.", color=0xff0000)
    embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed)
"""
END OF TEST COMMANDS

"""
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def invite(ctx):
    await ctx.send("Invite George the bot here:")
    await ctx.send("https://dsc.gg/georgebot")
    await ctx.send("**             **")
    await ctx.send("If you need support with anything go here:")
    await ctx.send("https://dsc.gg/max'sworld")
    await ctx.send("**                        **")
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def friend(ctx):
    if ctx.guild.id == 726593227448123444:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send("Hey, look! My friend is in this server!")
        await ctx.send("<@804221077270036501> Hello!")
    else:
        async with ctx.typing():
            await ctx.send("***My friend?***\nWell, my friend is Evelyn. \nShe's only is in Max's World, since she's pretty shy. \nIf you want to meet her, go here!:\nhttps://dsc.gg/max'sworld")
@friend.error
async def friend_error(ctx, error):
    error = str(error)
    error2 = error[33:-1]
    embed1 = discord.Embed(title="Error", color=0xff0000)
    name1 = "There are still "+str(error2)+" seconds until you can use this command again!"
    embed1.add_field(name=name1,
                    value="If you want to use this command without cooldowns, get George the bot Premium!",
                    inline=False)
    embed1.set_footer(text="...")

    await ctx.send(embed=embed1)

#Fun
#
#
#
"""
This is the fun section. any commands here are for fun lol.


"""
@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def skyblock(ctx, *, args):
    await ctx.send(".")
    await ctx.send("https://sky.shiiyu.moe/stats/"+args)
@skyblock.error
async def sky_error(ctx, error):
    error = str(error)
    error1 = error[33:-1]
    embed = discord.Embed(title="Error", color=0xff0000)
    name1 = "There are still "+str(error1)+" seconds until you can use this command again!"
    embed.add_field(name=name1,
                    value="If you want to use this command without cooldowns, get George the bot Premium!",
                    inline=False)
    embed.set_footer(text="...")
    await ctx.send(embed=embed)
@bot.command(aliases=["w2n", "wtn","wordtonum", "WORDTONUM", "WORDTONUMBER"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def wordtonumber(ctx, *, args):
    try:
        test2 = num2words(int(args))
        result = "The integer for of the number you typed is: \n***" + str(test2) + "***"
        await ctx.send(result)
    except:
        await ctx.send("Are you sure that you entered a number in like... NUMBER form? (example: 42)")


@wordtonumber.error
async def w2n_error(ctx, error):
    error = str(error)
    error1 = error[33:-1]
    embed = discord.Embed(title="Error", color=0xff0000)
    name1 = "There are still "+str(error1)+" seconds until you can use this command again!"
    embed.add_field(name=name1,
                    value="If you want to use this command without cooldowns, get George the bot Premium!",
                    inline=False)
    embed.set_footer(text="...")
    await ctx.send(embed=embed)
@bot.command()
async def max(ctx, *, arg):
    try:
        arg = int(arg)
    except:
        await ctx.send("Are you trying to abuse this command.\nPlease type an integer, not some random text.")
    else:
        big = max(arg)
        await ctx.send("The letter lowest down the alphebet that I found was: \n***" + str(big) + "***")
@bot.command()
async def brawlstars(ctx):
    await ctx.send("Brawl Stars:\nhttps://supercell.com/en/games/brawlstars/")
@brawlstars.error
async def brawlstars_error(ctx, error):
    error = str(error)
    error1 = error[33:-1]
    embed = discord.Embed(title="Error", color=0xff0000)
    name1 = "There are still "+error1+" seconds until you can use this command again!"
    embed.add_field(name=name1,
                    value="If you want to use this command without cooldowns, get George the bot Premium!",
                    inline=False)
    embed.set_footer(text="...")
    await ctx.send(embed=embed)
#Premium
@bot.command()
async def valorant(ctx):
    await ctx.send("Very good game, would play again:")
    await ctx.send("https://playvalorant.com/")
@bot.command(aliases=["Minecraft", "MINECRAFT"])
async def minecraft(ctx):
    await ctx.send("Epic game, go play it because Dream plays it:")
    await ctx.send("https://www.minecraft.net/")
@bot.command(aliases=["FORTNITE", "cringe", "Cringe", "Fortnite", "sucks"])
async def fortnite(ctx):
    await ctx.send("No, stop, you are hurting my brain.")
    time.sleep(1)
    await ctx.send("Don't play fortnite I beg you.")
    await ctx.send("Please. DO NOT PLAY FORTNITE")

#End of fun section
@bot.command()
async def settings(ctx):
    embed = discord.Embed(title=".", color=0xbe1919)
    embed.set_author(name=" ",
                     icon_url="https://lh3.googleusercontent.com/-mGQXMEmDojE/X-LbkNfGpeI/AAAAAAAABJQ/kXsVIHMc1IQAAtgvrwZ7F3wVtNlPLXtygCLcBGAsYHQ/s0/9568_dogspin.gif")
    embed.add_field(name="d", value=".", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['8ball','eightball'])
async def _8ball(ctx, arg):
    random = randint(0, 19)
    ball = ["It is certain.", "Without a doubt.", "You may rely on it.", "Yes, definitely.", "It is decidedly so.", "As I see it, yes.", "Most likely.", "Yes.", "Outlook good.", "Signs point to yes.", "Reply hazy, try again.","Better not tell you now.","Ask again later.","Cannot predict now.","Concentrate and ask again.","Don’t count on it.","Outlook not so good.","My sources say no.","Very doubtful.","My reply is no."]
    if random <= 9:
        embed = discord.Embed(title="Anwser", color=discord.Color.green())
        embed.add_field(name=ball[random], value='HOW ABOUT GETTING GEORGE PREMIUM', inline=True)
        await ctx.send(embed=embed)
    elif random <= 14:
        embed = discord.Embed(title="Anwser", color=discord.Color.light_grey())
        embed.add_field(name=ball[random], value='HOW ABOUT GETTING GEORGE PREMIUM', inline=True)
        await ctx.send(embed=embed)

    elif random <= 19:
        embed = discord.Embed(title="Anwser", color=discord.Color.dark_red())
        embed.add_field(name=ball[random], value='HOW ABOUT GETTING GEORGE PREMIUM', inline=True)
        await ctx.send(embed=embed)







ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}


ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}
ytdl = YoutubeDL(ytdlopts)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! {bot.latency}")



@bot.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    if user.dm_channel == None:
        await user.create_dm()
    await user.dm_channel.send(
        content=f"You have been kicked from ***Max's World*** by Max's Ban Bot lol \n***Reason***: {reason} ")
    await user.kick(reason=reason)

@bot.command(aliases=['hi','hello'])
async def george(ctx):
  await ctx.send("**Hello**")
  await ctx.send(file=discord.File('HELLO.gif'))

@bot.command()
async def ban(ctx, user: discord.Member, *, reason=None):
    if user.dm_channel == None:
        guild = ctx.guild
        await user.create_dm()
        await user.dm_channel.send(
            content=f"You have been banned from ***"+str(guild)+"*** by Max's Ban Bot lol \n***Reason***: " + reason)
        await user.dm_channel.send(content=f"Please appeal your ban at: https://forms.gle/mHSesTXXBLftcz8E6")
        await user.ban(reason=reason)
@bot.command()

async def delete(ctx, arg):
    arg = int(arg)
    if arg > 200:
        embed = discord.Embed(title="Error",
                              description="Discord only allows me to delete 200 messages at a time, and also only allows me to delete messages that are younger than 2 weeks.",
                              color=0xff0000)
        embed.add_field(name="I will have to only delete 200 messages.", value="Is that fine? Send: [y/n]",
                        inline=False)
        await ctx.send(embed=embed)


        channel = ctx.channel


        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == ':thumbsup:'

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send(':thumbsdown:')
        else:
            embed = discord.Embed(title=":white_check_mark:", color=0x00ff08)
            embed.add_field(name="I have deleted 200 messages", value="undefined", inline=False)
            await ctx.send(embed=embed)
            arg = 200
    ctx.channel.purge(limit=arg)


@bot.command()

async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)

            await ctx.send(f"{user.mention} unbanned.")
            return
@bot.command()

async def mute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted rip")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Verified")
    await member.remove_roles(role)


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")


@bot.command()
@commands.has_any_role("Admin1", "Mod1")
async def unmute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted rip")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Verified")
    await member.add_roles(role)


@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")
@bot.command()
async def join(ctx):

    try:
        channel = ctx.author.voice.channel
        try:
            await channel.connect()
            await ctx.send("I have connected to your voice channel!")
        except:
            await ctx.send("You have already connected to the voice channel!")
    except:
        await ctx.send("You are not in a voice channel!")




@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    try:
        await server.disconnect()
        await ctx.send("Disconnected from your voice channel!")
    except:
        await ctx.send("The bot is already disconnected!")

songs = asyncio.Queue()
play_next_song = asyncio.Event()





async def audio_player_task():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()


def toggle_next():
    bot.loop.call_soon_threadsafe(play_next_song.set)


@bot.command(pass_context=True)
async def play(ctx, url):
    if not bot.is_voice_connected(ctx.message.server):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        voice = bot.voice_bot_in(ctx.message.server)

    player = await voice.create_ytdl_player(url, after=toggle_next)
    await songs.put(player)

bot.loop.create_task(audio_player_task())



@bot.command()
async def logout(ctx):
    if ctx.author.id == 710533851692269618:
        await ctx.send("Bye.")
        await bot.logout()

bot.run(TOKEN)
