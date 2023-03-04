from __future__ import annotations

from tortoise.models import Model
from tortoise.contrib.postgres.fields import ArrayField
from tortoise import fields


class Giveaway(Model):
    guild_id = fields.BigIntField(pk=True, index=True)
    host_id = fields.BigIntField()
    channel_id = fields.BigIntField()
    message_id = fields.BigIntField()
    winner_list = ArrayField(element_type="bigint", null=True)
    winners = fields.BigIntField()
    participants = ArrayField(element_type="bigint")
    duration = fields.DatetimeField()
    start_time = fields.DatetimeField(auto_now=True)
    rerolls = fields.BigIntField(null=True)
    min_message = fields.BigIntField(null=True)
    required_role = fields.BigIntField(null=True)
    winner_role = fields.BigIntField(null=True)

    class Meta:
        table = "giveaways"
