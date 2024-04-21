"""Navbar component for the app."""

from Podly import styles
from Podly.components.callout import callout

import reflex as rx


def discord_button() -> rx.Component:
    return rx.button(
        
    )

def github_button() -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.image(src="icons/github.svg", width="24px"),
            rx.text("GitHub", font_size="16px"),
            callout("15k"),
            align="center",
        ),
        padding_y="1.5em",
        padding_x="2em",
        border_radius="1em",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.logo(),
                rx.heading("About"),
            ),
            rx.spacer(),
            rx.hstack(
                github_button(),
                rx.heading("Discord"),
            ),
            width="100vw",
            align="center",
        ),
    )