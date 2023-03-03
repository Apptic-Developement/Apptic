from __future__ import annotations

from hikari import RESTBot, TokenType
from config import token, public_key
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

    
        