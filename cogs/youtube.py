from discord.ext import commands
import aiohttp
import re


class YouTube(commands.Cog):
    """Search YouTube for videos."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    async def _youtube_results(self, query: str):
        try:
            search_url = "https://www.youtube.com/results?"
            payload = {"search_query": "".join(query)}
            headers = {"user-agent": "Red-cog/3.0"}
            async with self.session.get(search_url, params=payload, headers=headers) as r:
                result = await r.text()
            yt_find = re.findall(r"href=\"\/watch\?v=(.{11})", result)

            url_list = []
            for track in yt_find:
                url = f"https://www.youtube.com/watch?v={track}"
                if url not in url_list:
                    url_list.append(url)

        except Exception as e:
            url_list = [f"Something went terribly wrong! [{e}]"]

        return url_list

    @commands.command()
    async def ютуб(self, ctx, *, query: str):
        """Поиск на Youtube."""
        result = await self._youtube_results(query)
        await ctx.send(result[0], delete_after=60)
        await ctx.send(result[1], delete_after=60)
        await ctx.send(result[2], delete_after=60)


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def youtube0001(self, ctx, *, query: str):
        """Search on Youtube, multiple results."""
        result = await self._youtube_results(query)
        await menu(ctx, result, DEFAULT_CONTROLS)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

def setup(client):
    client.add_cog(YouTube(client))