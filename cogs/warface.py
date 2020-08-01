import discord
from discord.ext import commands
import requests
from random import choice


class Warface(commands.Cog):

    def __init__(self, client):
        self.client = client
# Commands

    @commands.command()
    async def браво(self, ctx, arg):
        text = arg
        r = requests.get("http://api.warface.ru/user/stat/?name={}&server=2".format(text))
        response_json = r.json()
        nick = response_json['nickname']
        try:
            clan = response_json['clan_name']
        except KeyError:
            clan = (f"Не состоит в клане")
        rank = response_json['rank_id']
        us_pvp = response_json['pvp']
        us_pve = response_json['pve']
        pvpall = response_json['pvp_all']
        pveall = response_json['pve_all']
        pvpwin = response_json['pvp_wins']
        pvplost = response_json['pvp_lost']
        pvewin = response_json['pve_wins']
        pvelost = response_json['pve_lost']
        pvpklass = response_json['favoritPVP']
        pveklass = response_json['favoritPVE']
        embbr = discord.Embed(color=discord.Color.light_grey(), title = "Статистика игрока {}".format(nick))
        embbr.add_field(name="Клан", value=clan)
        embbr.add_field(name="Ранг", value=rank)
        embbr.add_field(name="У/С PVP", value=us_pvp)
        embbr.add_field(name="У/С PVE", value=us_pve)
        embbr.add_field(name="Сыграно PVP матчей", value=pvpall)
        embbr.add_field(name="Сыграно PVE матчей", value=pveall)
        embbr.add_field(name="Победа/Поражение PVP", value="{}/{}".format(pvpwin, pvplost))
        embbr.add_field(name="Победа/Поражение PVE", value="{}/{}".format(pvewin, pvelost))
        embbr.add_field(name="Игровой класс на PVP", value=pvpklass)
        embbr.add_field(name="Игровой класс на PVE", value=pveklass)
        await ctx.send(embed=embbr)


    @commands.command()
    async def альфа(self, ctx, arg):
        text = arg
        r = requests.get("http://api.warface.ru/user/stat/?name={}&server=1".format(text))
        response_json = r.json()
        nick = response_json['nickname']
        try:
            clan = response_json['clan_name']
        except KeyError:
            clan = (f"Не состоит в клане")
        rank = response_json['rank_id']
        us_pvp = response_json['pvp']
        us_pve = response_json['pve']
        pvpall = response_json['pvp_all']
        pveall = response_json['pve_all']
        pvpwin = response_json['pvp_wins']
        pvplost = response_json['pvp_lost']
        pvewin = response_json['pve_wins']
        pvelost = response_json['pve_lost']
        pvpklass = response_json['favoritPVP']
        pveklass = response_json['favoritPVE']
        embbr = discord.Embed(color=discord.Color.light_grey(), title = "Статистика игрока {}".format(nick))
        embbr.add_field(name="Клан", value=clan)
        embbr.add_field(name="Ранг", value=rank)
        embbr.add_field(name="У/С PVP", value=us_pvp)
        embbr.add_field(name="У/С PVE", value=us_pve)
        embbr.add_field(name="Сыграно PVP матчей", value=pvpall)
        embbr.add_field(name="Сыграно PVE матчей", value=pveall)
        embbr.add_field(name="Победа/Поражение PVP", value="{}/{}".format(pvpwin, pvplost))
        embbr.add_field(name="Победа/Поражение PVE", value="{}/{}".format(pvewin, pvelost))
        embbr.add_field(name="Игровой класс на PVP", value=pvpklass)
        embbr.add_field(name="Игровой класс на PVE", value=pveklass)
        await ctx.send(embed=embbr)


    @commands.command()
    async def чарли(self, ctx, arg):
        text = arg
        r = requests.get("http://api.warface.ru/user/stat/?name={}&server=3".format(text))
        response_json = r.json()
        nick = response_json['nickname']
        try:
            clan = response_json['clan_name']
        except KeyError:
            clan = (f"Не состоит в клане")
        rank = response_json['rank_id']
        us_pvp = response_json['pvp']
        us_pve = response_json['pve']
        pvpall = response_json['pvp_all']
        pveall = response_json['pve_all']
        pvpwin = response_json['pvp_wins']
        pvplost = response_json['pvp_lost']
        pvewin = response_json['pve_wins']
        pvelost = response_json['pve_lost']
        pvpklass = response_json['favoritPVP']
        pveklass = response_json['favoritPVE']
        embbr = discord.Embed(color=discord.Color.light_grey(), title = "Статистика игрока {}".format(nick))
        embbr.add_field(name="Клан", value=clan)
        embbr.add_field(name="Ранг", value=rank)
        embbr.add_field(name="У/С PVP", value=us_pvp)
        embbr.add_field(name="У/С PVE", value=us_pve)
        embbr.add_field(name="Сыграно PVP матчей", value=pvpall)
        embbr.add_field(name="Сыграно PVE матчей", value=pveall)
        embbr.add_field(name="Победа/Поражение PVP", value="{}/{}".format(pvpwin, pvplost))
        embbr.add_field(name="Победа/Поражение PVE", value="{}/{}".format(pvewin, pvelost))
        embbr.add_field(name="Игровой класс на PVP", value=pvpklass)
        embbr.add_field(name="Игровой класс на PVE", value=pveklass)
        await ctx.send(embed=embbr)


# Функция рандомного выбора класса
    @commands.command(aliases=['Класс', 'клас', 'Клас', 'КЛАСС'])
    async def класс(self, ctx):
        pistol = choice(['Browning High Power','Daewoo K5','Beretta M9','Steyr M9-A1','Beretta M93R','Calico M950','FN Five-seveN','COLT Python Elite','MPA 930DMG','Rhino 60DS','Walther P99','Mateba Autorevolver','H&K USP','QSZ-92','ПЯ «Грач»','Taurus Judge','M1911A1'])
        klass = choice(['штурмом','медом','инжом','снапом'])
        if klass == 'штурмом':
            gun = choice(['M4A1','Daewoo K2','Daewoo K3','M16A2 LMG','XM8','H&K G36K','H&K MG36','Calico M955A','Galil AR','Tavor TAR-21','АК‐103','SAI GRY AR-15','VHS-2','РПК','XM8 LMG','MG3','MSBS Radon','Type 97B','АС Вал','IMBEL IA2','M60E4','AUG A3','H&K MG4','Famas F1','FN F2000','SIG 551','AUG A3 Hbar','Type 97'])
        if klass == 'медом':
            gun = choice(['Remington Model 870','SPAS-12','Remington 870 CB','Сайга','Hawk Pump','Benelli Nova tactical','Benelli M4 Super 90','SRM 1216','Вепрь','Сайга H.G.C. Custom','SAP6','AA-12','Remington 870 RAS','Kel-Tec Shotgun','SPAS-15','Jackhammer','Anakon','Cobray Striker','Sidewinder Venom','UTAS UTS-15','Сайга Spike','Derya MK‐10 VR 102','Fabarm P.S.S.10'])
        if klass == 'инжом':
            gun = choice(['H&K MP5','M4 CQB','H&K G36C','Daewoo K1','АК-9','H&K MP7','AUG A3 9mm XS','Mini Uzi','ПП-19 Бизон','Kriss super V','H&K MP5A5 Custom','Uzi Pro','Daewoo K7','Skorpion vz. 83','B&T MP9','PM-84 Glauberyt Custom','СР-2 «Вереск»','Beretta MX4 Storm','ПП-2000','MPA10SST-X','SIG 552','Calico M960A','FN P90','JS 9mm'])
        if klass == 'снапом':
            gun = choice(['СВД','M16 SPR Custom','H&K SL8','XM8 Sharpshooter','ACR SPR','SIG 550','Alpine','AMP DSR-1','Tavor STAR-21 Navy Blue','AT308','QBU-88','ОРСИС Т-5000','Barrett M107','Barrett M98B','CheyTac M200','M40A5','AWM'])
        embed_klass = discord.Embed(color=discord.Color.light_grey(), title="Выбор игрового класса")
        embed_klass.add_field(name="Пользователь", value="{}".format(ctx.author.mention))
        embed_klass.add_field(name="Играет {}".format(klass), value="С основным оружием **{}**".format(gun), inline="false")
        embed_klass.add_field(name="\uFEFF", value="И пистолетом **{}**".format(pistol), inline="false")
        await ctx.send(embed=embed_klass, delete_after=60)
        await ctx.message.delete(delay=60)


# Функция рандомного выбора спецоперации
    @commands.command()
    async def спецоп(self, ctx):
        specop = choice(['Гидра','Затмение - Легко','Затмение - Сложно','Затмение - Профи','Вулкан - Легко','Вулкан - Сложно','Вулкан - Профи','Вулкан - Хардкор','Марс - Легко','Марс - Сложно','Марс - Профи','Ледокол - Легко','Ледокол - Сложно','Ледокол - Профи','Восход - Легко','Восход - Сложно','Восход - Профи','Черная Акула - Легко','Черная Акула - Сложно','Черная Акула - Профи','Припять - Лекго','Припять - Сложно','Припять - Профи','Анубис - Легко','Анубис - Сложно','Анубис - Профи','Белая Акула','Снежный бастион - Острие','Снежный бастион - Засада','Снежный бастион - Зенит','Снежный бастион - Марафон'])
        embed_so = discord.Embed(title = specop)
        await ctx.send(embed=embed_so, delete_after=7)
        await ctx.message.delete(delay=5)


def setup(client):
    client.add_cog(Warface(client))
