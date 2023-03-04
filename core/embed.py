from __future__ import annotations

from hikari import Color, Embed as OriginalEmbed

__all__ = ("Embed",)


class Embed(OriginalEmbed):
    def __init__(self, colour: Color = Color.from_hex_code("#5450ff")) -> None:
        super().__init__(colour=colour)

    def watermark(self) -> None:
        self.set_footer(text="Made with ❤️ by Pranoy#3299")

