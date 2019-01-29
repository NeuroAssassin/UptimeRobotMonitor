from discord.ext import commands
import discord
from datetime import datetime
import aiohttp

class Admin:
    def __init__(self, bot):
        self.bot = bot

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return response.status

    @commands.command()
    async def check(self, ctx, service: str):
        if ctx.author.id == 473541068378341376:
            m = await ctx.send("**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[----------]`")
            if service.upper() in ['MU', 'MUSIC UNIVERSE']:
                async with aiohttp.ClientSession() as session:
                    status = await self.fetch(session, "https://Dog-Soprano--neuroassassin.repl.co")
                    await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[###-------]`")
                    if status != 200:
                        embed = discord.Embed(title="Monitor Webhook", description="Webhook monitor for: Music Univserse", color=0xff0000, timestamp=datetime.utcnow())
                        embed.add_field(name="Status:", value="DOWN")
                        embed.add_field(name="Code: ", value=status)
                        embed.set_footer(text="Monitor for Music Universe | Webhook created and used by Neuro Assassin")
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[#######---]`")
                        await ctx.send(embed=embed)
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[##########]` (Finished)")
                    else:
                        embed = discord.Embed(title="Monitor Webhook", description="Webhook monitor for: Music Univserse", color=0x006606, timestamp=datetime.utcnow())
                        embed.add_field(name="Status:", value="UP")
                        embed.add_field(name="Code: ", value=status)
                        embed.set_footer(text="Monitor for Music Universe | Webhook created and used by Neuro Assassin")
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[#######---]`")
                        await ctx.send(embed=embed)
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[##########]` (Finished)")
            elif service.upper() in ['ACR', 'LINE ACR', 'ACRONYM FINDER']:
                async with aiohttp.ClientSession() as session:
                    status = await self.fetch(session, "https://Acronym-Finder-LINE-bot--neuroassassin.repl.co")
                    await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[###-------]`")
                    if status != 200:
                        embed = discord.Embed(title="Monitor Webhook", description="Webhook monitor for: Acronym Finder LINE Bot", color=0xff0000, timestamp=datetime.utcnow())
                        embed.add_field(name="Status:", value="DOWN")
                        embed.add_field(name="Code: ", value=status)
                        embed.set_footer(text="Monitor for Acronym Finder LINE Bot | Webhook created and used by Neuro Assassin")
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[#######---]`")
                        await ctx.send(embed=embed)
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[##########]` (Finished)")
                    else:
                        embed = discord.Embed(title="Monitor Webhook", description="Webhook monitor for: Acronym Finder LINE Bot", color=0x006606, timestamp=datetime.utcnow())
                        embed.add_field(name="Status:", value="UP")
                        embed.add_field(name="Code: ", value=status)
                        embed.set_footer(text="Monitor for Acronym Finder LINE Bot | Webhook created and used by Neuro Assassin")
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[#######---]`")
                        await ctx.send(embed=embed)
                        await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[##########]` (Finished)")
            else:
                await m.edit(content="**Pinging: " + service + "**\nA message will be sent when this command has finished with the results.\n**Progress**: `[##########]`(Finished)\n**STATUS**: Invalid Service.")
        else:
            await ctx.send("You are not allowed to run that command.")

def setup(bot):
    bot.add_cog(Admin(bot))