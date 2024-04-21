"""Callout component for the app."""

from Podly import styles

import reflex as rx


def callout(text: str) -> rx.Component:
    text_color = "#6051F3"
    background_color = "#252047"

    return rx.vstack(
        rx.text(text),
        width="28px",
        height="28px",
        justify="center",
        align="center",
        color=text_color,
        background_color=background_color,
        border_radius="6px",
    )
