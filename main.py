from __future__ import annotations


from core import Bot
from os import listdir
from crescent import Client

bot = Bot()
client = Client(bot)

for fn in listdir("plugins"):
    if not fn.startswith("_"):
        client.plugins.load(f'plugins.{fn}.plugin')

if __name__ == "__main__":
    bot.run()