from __future__ import annotations

from crescent import Plugin, command, Context
from hikari import RESTBot
from core import Embed

plugin = Plugin[RESTBot, None]()

@plugin.load_hook
def on_load():
    print(f"Loaded utility plugin.")
