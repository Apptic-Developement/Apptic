from __future__ import annotations

from crescent import Plugin
from hikari import RESTBot


plugin = Plugin[RESTBot, None]()

@plugin.load_hook
def on_load():
    print(f"Loaded utility plugin.")

