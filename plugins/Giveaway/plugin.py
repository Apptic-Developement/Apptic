from __future__ import annotations

from crescent import Group, Plugin, client, command, Context
from hikari import RESTBot, Permissions
from core import Embed

plugin = Plugin[RESTBot, None]()

@plugin.load_hook
def on_load():
    print(f"Loaded giveaway plugin.")

giveaway = Group(
    name="giveaway",
    description="Create awesome giveaways with apptic bot.",
    default_member_permissions=Permissions.MANAGE_MESSAGES,
    dm_enabled=False
)

@plugin.include
@giveaway.child
@command(
    name="start",
    description="Starts a new giveaway."
)
async def giveaway_start(ctx: Context):
    await ctx.respond("Started!")


@plugin.include
@giveaway.child
@command(
    name="reroll",
    description="Reroll a giveaway."
)
async def giveaway_reroll(ctx: Context):
    await ctx.respond("Rerolled")