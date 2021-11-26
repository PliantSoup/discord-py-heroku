import discord
import json
from discord.ext import commands
from embedlist import *

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Выводит Welcome сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def welcome(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=welcomel['title'],
                              url=welcomel['url'],
                              description=welcomel['description'],
                              color=0x00ff00)
        embed.add_field(name=welcomel['f1_name'],
                        value=welcomel['f1_value'],
                        inline=False)
        await ctx.send(embed=embed)

    @commands.command(description="Обновляет Welcome сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def updWelcome(self, ctx):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(readme_id)
        embed = discord.Embed(title=welcomel['title'],
                              url=welcomel['url'],
                              description=welcomel['description'],
                              color=0x00ff00)
        embed.add_field(name=welcomel['f1_name'],
                        value=welcomel['f1_value'],
                        inline=False)
        msg = await channel.fetch_message(welcomel['msg_id'])
        await msg.edit(embed=embed)

    @commands.command(description="Выводит Links сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def links(self, ctx):
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title="Official Links", description="**__Evergreen Trees__**", color=0x00ff00)
        emb.add_field(name="Website", value="Coming soon", inline=False)
        emb.add_field(name="Twitter", value="https://twitter.com/eg_trees", inline=False)
        emb.add_field(name="Discord", value="https://discord.gg/aVnyDXh4Wx", inline=False)
        emb.add_field(name="OpenSea", value="https://opensea.io/collection/evergreen-trees", inline=False)
        await ctx.send(embed=emb)

    @commands.command(description="Обновляет Links сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def updLinks(self, ctx):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(readme_id)
        embed = discord.Embed(title=linksl['title'],
                              description=linksl['description'],
                              color=0x00ff00)
        embed.add_field(name=linksl['f1_name'],
                        value=linksl['f1_value'],
                        inline=False)
        embed.add_field(name=linksl['f2_name'],
                        value=linksl['f2_value'],
                        inline=False)
        embed.add_field(name=linksl['f3_name'],
                        value=linksl['f3_value'],
                        inline=False)
        embed.add_field(name=linksl['f4_name'],
                        value=linksl['f4_value'],
                        inline=False)
        msg = await channel.fetch_message(linksl['msg_id'])
        await msg.edit(embed=embed)

    @commands.command(description="Выводит Verify сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def verify(self, ctx, emoji, role: discord.Role):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="Verification",
                              description="**Please verify that you read the information by clicking with a ''🌲'' below.**\n"
                                          "Our team will **__NEVER__** contact you first in DMs.\n"
                                          "Don't fall for scam. Stay safe!",
                              color=0x00ff00)
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction(emoji)

        with open('reactrole') as json_file:
            data = json.load(json_file)

            new_reactrole = {
                'role_name': role.name,
                'role_id': role.id,
                'emoji': emoji,
                'message_id': msg.id
            }

            data.append(new_reactrole)

        with open('reactrole', 'w') as j:
            json.dump(data, j, indent=4)

    @commands.command(description="Обновляет Verify сообщение")
    @commands.has_role("🍃Forest Keeper")
    async def updVerify(self, ctx):
        await ctx.channel.purge(limit=1)
        channel = self.bot.get_channel(readme_id)
        embed = discord.Embed(title=verifyl['title'],
                              description=verifyl['description'],
                              color=0x00ff00)
        msg = await channel.fetch_message(verifyl['msg_id'])
        await msg.edit(embed=embed)

    @commands.command(aliases=['delete'], description="Чистит чат {amount:int}")
    @commands.has_role("🍃Forest Keeper")
    async def clearmsg(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)