from __future__ import annotations

from hikari import RESTBot, TokenType
from config import token, public_key, db_url
from tortoise import Tortoise

from os import listdir
__all__ = (
    "Bot",
)

class Bot(RESTBot):
    def __init__(self):
        super().__init__(
            token=token,
            public_key=public_key,
            token_type=TokenType.BOT,
            force_color=True
        )
        self.add_startup_callback(self.init_tortoise)

    @staticmethod
    async def init_tortoise(_):
        await Tortoise.init(
            db_url=db_url,
            modules={"models": [f"models.{i[:-3]}" for i in listdir("models") if not i.startswith("_")]}
        )
        await Tortoise.generate_schemas(safe=True)
        
    
        