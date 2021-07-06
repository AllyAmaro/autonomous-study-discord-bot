from dotenv import load_dotenv
load_dotenv()

import discord
from discord import Embed
import os

class todo: 
    def __init__(self, id, user_id, message): 
        self.id = id
        self.user_id = user_id 
        self.message = message
   
TOKEN = os.environ.get("DISCORD_TOKEN")
todo_list = []
client = discord.Client()

"""
@client.event
async def on_message(message):
    print('Hello human!I am {0.user} and my goal is to help you study!'.format(client))
"""

@client.event
async def on_message(message):

    print('Hello human!I am {0.user} and my goal is to help you study!'.format(client))

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    print('f{username}: {user_message}({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'study-bot':
      if user_message.lower() == '(todo':
        print("<=====")
        todo_embed = Embed(
          title = "Your Task list", 
          description ="Never let you down",
          colour = 0xB6C9F0
          )
        for t in todo_list:
          if t.user_id == message.author:
            todo_str = f":white_check_mark:{t.message}"
            todo_embed.add_field(name=todo_str, value=t.user_id, inline=True)        
        await message.channel.send(embed=todo_embed)
        #else:
          #await message.channel.send(f"Dear {username} there's no todos for you")
        return

      if user_message.lower().startswith('(add'):
                print("=======>")
                user_message_arr = user_message.split('|')
                if (len(user_message_arr) > 0):
                  id = len(todo_list) + 1
                  todo_message = user_message_arr[1]
                  todo_list.append(todo(id, message.author, todo_message))
                  await message.channel.send(f':white_check_mark: Task successfully created with - {todo_message}')
                else:
                  await message.channel.send(f':x: No Task entered. Say what you want to add after the command!')
    """
    elif user_message.lower() == '(study':
        await message.channel.send(
            f'A study session has begun! Say !studysession to know how much time your study session has already lasted and !studyend to end it.')
        return
    """
""""
    if user_message.lower() == '(hi':
            await message.channel.send('Hello Human!')
            embed = Embed(title='Hello human!',
                              description='I am your companion, Autonomous Study, and my goal is to help you study!',
                              colour=0xB6C9F0)
            fields = [("Commands", "Ask (help to see everything I can do for you!", True),
                      ("Help","DM Ally if you're having trouble with this bot or anything else in this server", True)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await message.channel.send(embed=embed)
            embed.set_footer(text=f"I am officially online!")
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
            embed.set_footer(text=f"Ask for help if needed!")
            await message.channel.send(embed=embed)
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
"""

print("The bot is running 🤖")
client.run(TOKEN)




