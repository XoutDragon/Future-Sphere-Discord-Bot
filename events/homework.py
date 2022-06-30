import discord
from discord.ext import commands


class Homework(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            color=discord.Color.blurple(),
            title="✨ Welcome to Future Sphere Academy ✨",
            description="Hello, this is the discord server for Future Sphere Academy. If you have any questions "\
                        "related to homework, please only send in <#858453343545327625>. Before you do this, please "\
                        "remember to read and follow the rules in <#921179091204440154>."
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/690739145101803521/a7ec96a51e34df6d16472980c31fca31.webp?size=96"
        )

        await member.send(embed=embed)


def setup(client):
    client.add_cog(Homework(client))