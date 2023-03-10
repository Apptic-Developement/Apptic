from __future__ import annotations

from crescent import Plugin
import crescent
from hikari import RESTBot


plugin = Plugin[RESTBot, None]()

@plugin.load_hook
def on_load():
    print(f"Loaded utility plugin.")

@plugin.include
@crescent.command(name="test")
async def callback(ctx: crescent.Context):
    await ctx.respond("Okhh")