import discord
from discord.ext import commands
from random import choice
import os



mat_msg = ['бля', 'пизд', 'хуй', 'пидар', 'гондон', 'педик', 'хуета', 'Бля', 'Хуй', 'Хуе', 'Пизд', 'хуе']
kosyak_msg = ['косяк', 'касяк', 'проиграили', 'слили', 'слив', 'сдохли']
hello_msg = ['Привет', 'Здравствуйте', 'Добрый', 'Приветствую', 'привет', 'привествую', 'Хай', 'хай']
suka = ['Сука','сука','Сучка']

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

# Events

    @commands.Cog.listener()
    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Warface'))
        print("Bot Online!")

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in hello_msg:
            if i in message.content:
                author = message.author
                helo = choice(['Hello','Здрасти','Здрафстфуйте','Приуэт насяльника'])
                await message.channel.send(f"{helo} {author.mention}")
        for kos in kosyak_msg:
            if kos in message.content:
                await message.channel.send('Ну это снова <@600396505064407053> накосячил!', delete_after=7)
        for suk in suka:
            if suk in message.content:
                await message.channel.send('Сам такой!', delete_after=7)
        for mat in mat_msg:
            if mat in message.content:
                author = message.author
                await message.delete(delay=2)
                await message.channel.send(f"{author.mention} матершинник, стыд и позор!")

# Commands

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def rust(self, ctx):
        await ctx.send("Сервер: ```connect 37.230.137.11:22061```")

    @commands.command(aliases=['гг', 'ГГ', 'GG'])
    async def gg(self, ctx):
    	await ctx.send("@here Го Гамать!")


def setup(client):
    client.add_cog(Ping(client))
