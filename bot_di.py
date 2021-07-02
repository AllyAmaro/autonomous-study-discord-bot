import discord
import random
from discord import Embed
import asyncio
import time

TOKEN = 'ODU0ODA4OTI2MTUwNzIxNjI3.YMpU2Q.ZVkCRHh36pm2Lqz7arDoEVbu1Zo'

client = discord.Client()


@client.event
async def on_message(message):
    print('Hello human!I am {0.user} and my goal is to help you study!'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user = str()
    user_message = str(message.content)
    channel = str(message.channel.name)
    print('f{username}: {user_message}({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'study-bot':
        if user_message.lower() == '(todo':
            await message.channel.send(
                f'The todo list for today has been created! What do you want to add {username}? Say !add [what you want to add].')
            return
        elif user_message.lower() == '(study':
            await message.channel.send(
                f'A study session has begun! Say !studysession to know how much time your study session has already lasted and !studyend to end it.')
            return
        elif user_message.lower() == '(add':
                await message.channel.send(f':x: No Task entered. Say what you want to add after the command!')
                print(":x: No Task entered. Say what you want to add after the command!")


    if user_message.lower() == '(hi':
            await message.channel.send('Hello Human!')
            embed = Embed(title='Hello human!',
                              description='I am your companion, Autonomous Study, and my goal is to help you study!',
                              colour=0xB6C9F0)
            fields = [("Commands", "Ask !help to see everything I can do for you!", True),
                      ("Help","DM Ally if you're having trouble with this bot or anything else in this server", True)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await message.channel.send(embed=embed)
            embed.set_footer("I am officially online!")
            return

    if user_message.lower() == '(help':
            await message.channel.send('Here is all I can do:')
            embed = Embed(title='I can do many things!',
                              description='Say ([the subtitle description] to know every command available in each section:',
                              colour=0xB6C9F0)
            fields = [("Lists and reminders", "(listhelp", True),
                      ("Study sessions","(studyhelp", True),
                      ("Notes, documents and links","(linkshelp", True),
                      ("Playlist","(playlisthelp", True),
                      ("Statistics","(statisticshelp", True)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await message.channel.send(embed=embed)
            embed.set_footer("Ask for help if needed!")
            return

def community_report(guild):
            online = 0
            idle = 0
            offline = 0

            for m in guild.members:
                if str(m.status) == "online":
                    online += 1
                if str(m.status) == "offline":
                    offline += 1
                else:
                    idle += 1

            return online, idle, offline

        async def user_metrics_background_task():
            while not client.is_closed():
                try:
                    online, idle, offline = community_report(sentdex_guild)
                    with open("usermetrics.csv", "a") as f:
                        f.write(f"{int(time.time())},{online},{idle},{offline}\n")
                await asyncio.sleep(5)
            except Exception as e:
            print(str(e))
            await asyncio.sleep(5)

    @client.event  # event decorator/wrapper
    async def on_ready():
        global sentdex_guild
        sentdex_guild = client.get_guild(405403391410438165)
        print(f"We have logged in as {client.user}")

    @client.event
    async def on_message(message):
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

        if user_message.lower() == '(members':
            await message.channel.send(f"```py\n{sentdex_guild.member_count}```")

        elif user_message.lower() == '(logout':
            await client.close()

        elif user_message.lower() == '(status':
            online, idle, offline = community_report(sentdex_guild)
            await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

client.loop.create_task(user_metrics_background_task())

client.run(TOKEN)




