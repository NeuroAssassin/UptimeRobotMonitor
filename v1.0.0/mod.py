from discord.ext import commands
import discord

class Mod:
    def __init__(self, bot):
        self.bot = bot

    # Commands

    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason="Action Requested"):
        if ctx.author.id in [473541068378341376]:
            try:
                await user.ban(reason=reason)
            except Exception as e:
                await ctx.send("Failed to ban user: " + str(e))
            else:
                await ctx.send("Done.  That user has been banned.")
        else:
            pass

    @commands.command()
    async def hackban(self, ctx, user: int, *, reason="Action Requested"):
        if ctx.author.id in [473541068378341376]:
            try:
                user = discord.Object(id=user)
                await ctx.guild.ban(user, reason=reason)
            except Exception as e:
                await ctx.send("Failed to hackban user: " + str(e))
            else:
                await ctx.send("Done.  That user has been banned.")
        else:
            pass

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason="Action Requested"):
        if ctx.author.id in [473541068378341376]:
            try:
                await user.kick(reason=reason)
            except Exception as e:
                await ctx.send("Failed to kick user: " + str(e))
            else:
                await ctx.send("Done.  That user has been kicked.")
        else:
            pass

def setup(bot):
    bot.add_cog(Mod(bot))