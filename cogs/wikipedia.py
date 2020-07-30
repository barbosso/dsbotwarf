import aiohttp
import discord
from discord.ext import commands

class Wikipedia(commands.Cog):
    """Look up stuff on Wikipedia."""

    base_url = "https://ru.wikipedia.org/w/api.php"
    headers = {"user-agent": "Red-DiscordBot/"}
    footer_icon = (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Wikimedia-logo.png"
        "/600px-Wikimedia-logo.png"
    )

    @commands.command(aliases=["wiki"])
    async def wikipedia(self, ctx: commands.Context, *, query: str):
        """Wikipedia."""
        payload = self.generate_payload(query)
        conn = aiohttp.TCPConnector()
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(
                self.base_url, params=payload, headers=self.headers
            ) as res:
                result = await res.json()

        try:
            # Get the last page. Usually this is the only page.
            for page in result["query"]["pages"]:
                title = page["title"]
                description = page["extract"].strip().replace("\n", "\n\n")
                url = "https://ru.wikipedia.org/wiki/{}".format(title.replace(" ", "_"))

            if len(description) > 1500:
                description = description[:1500].strip()
                description += "... [(read more)]({})".format(url)

            embed = discord.Embed(
                title="Wikipedia: {}".format(title),
                description=u"\u2063\n{}\n\u2063".format(description),
                color=discord.Color.blue(),
                url=url,
            )
            embed.set_footer(
                text="Wikipedia", icon_url=self.footer_icon
            )
            await ctx.send(embed=embed)

        except KeyError:
            await ctx.send(
                ("Не найдено \"{}\" на Wiki".format(query)), delete_after=7
            )
        except discord.Forbidden:
            await ctx.send(
                warning("I'm not allowed to do embeds here...\n{}".format(url))
            )

    @staticmethod
    def generate_payload(query: str):
        """Generate the payload for Wikipedia based on a query string."""
        payload = {}
        payload["action"] = "query"
        payload["titles"] = query.replace(" ", "_")
        payload["format"] = "json"
        payload["formatversion"] = "2"  # Cleaner json results
        payload["prop"] = "extracts"  # Include extract in returned results
        payload["exintro"] = "1"  # Only return summary paragraph(s) before main content
        payload["redirects"] = "1"  # Follow redirects
        payload["explaintext"] = "1"  # Make sure it's plaintext (not HTML)
        return payload

def setup(client):
    client.add_cog(Wikipedia(client))