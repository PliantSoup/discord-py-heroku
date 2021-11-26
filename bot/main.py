import discord
import json
from discord.ext import commands
from config import settings
import musictest
from main_cog import MainCog

client = commands.Bot(command_prefix=settings['prefix'],
                      intents=discord.Intents.all())

client.add_cog(musictest.Music(client))
client.add_cog(MainCog(client))


@client.event
async def on_ready():
    print("Connected")


@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        with open('reactrole') as reactfile:
            data = json.load(reactfile)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    with open('reactrole') as reactfile:
        data = json.load(reactfile)
        for x in data:
            if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


client.run(settings['token'])
