from discord.ext import commands
import discord

class Evnts:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I do not have permission to do that.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("It seems you are missing an argument for that command.")
            return
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please ensure that you are sending the right argument.")
            return
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("That command is disabled.")
            return
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("An error occured inside the command while running it.  The error has been reported to the Bot Team.")
            whole_thing = f"**Error:** {error}\n**Message:** {ctx.message.content}\n**Author:** {ctx.author.display_name}"
            await self.bot.erch.send(whole_thing)
            return
        elif isinstance(error, commands.CheckFailure):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("That command is on cooldown.  Please check back later.")
        else:
            await ctx.send("An unknown error as occured while running the command.  The error has been reported to the Bot Team.")
        whole_thing = f"**Error:** {error}\n**Message:** {ctx.message.content}\n**Author:** {ctx.author.display_name}"
        await self.bot.erch.send(whole_thing)