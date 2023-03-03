from __future__ import annotations

from tortoise.models import Model
from tortoise import fields


class Giveaway(Model):
    guild_id = fields.BigIntField(pk=True)