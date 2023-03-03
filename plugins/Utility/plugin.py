from __future__ import annotations

from crescent import Plugin, command, Context
from hikari import RESTBot, Embed

plugin = Plugin[RESTBot, None]()

@plugin.load_hook
def on_load():
    print(f"Loaded utility plugin.")


@plugin.include
@command
async def embed(ctx: Context):
    embed = Embed()
    embed.title = "Ok"
    await ctx.respond(
        embed=embed,
        ephemeral=True
    )