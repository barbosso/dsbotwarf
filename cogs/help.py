import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
# Commands

    @commands.command()
    async def help(self, ctx):
        emb = discord.Embed(color=discord.Color.light_grey(), title = "Bot commands")
        emb.add_field(name="!ping", value="Ping!")
        emb.add_field(name="!load", value="Загрузить Cog. Example: !load ping")
        emb.add_field(name="!unload", value="Выгрузить Cog. Example: !unload ping")
        emb.add_field(name="!класс", value="Выбор игрового класса")
        emb.add_field(name="!штурм", value="Рандомный выбор варбкасового оружия штурмовика")
        emb.add_field(name="!мед", value="Рандомный выбор варбкасового оружия медика")
        emb.add_field(name="!инж", value="Рандомный выбор варбкасового оружия инженера")
        emb.add_field(name="!снап", value="Рандомный выбор варбкасового оружия снайпера")
        emb.add_field(name="!пистолет", value="Рандомный выбор варбкасового пистолета")
        emb.add_field(name="!спецоп", value="Выбор спецоперации")
        emb.add_field(name="!clear", value="удалить Х сообщений. example: !clear 5")
        emb.add_field(name="!альфа nickname", value="Получить данные игрока Warface с сервера Альфа")
        emb.add_field(name="!браво nickname", value="Получить данные игрока Warface с сервера Браво")
        emb.add_field(name="!чарли nickname", value="Получить данные игрока Warface с сервера Чарли")
        emb.add_field(name="!ютуб", value="Поиск на YouTube. Присылает 3 первых видео из поискового запроса")
        emb.add_field(name="!wiki", value="Поиск на Википедии")
        emb.add_field(name="!task", value="Получить список заданий дополнения Gorgona")
        await ctx.send(embed=emb, delete_after=30)
        await ctx.message.delete(delay=5)


def setup(client):
    client.add_cog(Help(client))
