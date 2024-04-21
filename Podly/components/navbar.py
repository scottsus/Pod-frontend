"""Navbar component for the app."""

from Podly import styles
from Podly.components.callout import callout

import reflex as rx

def about_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.text("About", font_size="16px", color="rgb(173,173,173)",),
                align="center",
                color="white",
            ),
            padding_y="1.5em",
            border_radius="1em",
            background_color="rgb(32,29,29)",
            style={"border-style": "solid", "border-width": "thin","border-color": "rgb(173,173,173)"},
        ),
        href="/about"
    )

def discord_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src="/icons/discord.svg", width="24px"),
                align="center",
            ),
            padding_y="1.5em",
            border_radius="1em",
            height="42px",
            background_color="rgb(32,29,29)",
            style={"border-style": "solid", "border-width": "thin","border-color": "rgb(173,173,173)"},
        ),
        href="https://github.com/WilsonLimSet/PodcastTest",
        target="_blank",
    )

def github_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src="/icons/github.svg", width="24px"),
                rx.text("GitHub", font_size="16px", color="rgb(173,173,173)",),
                callout("15k"),
                align="center",
            ),
            padding_y="1.5em",
            padding_x="2em",
            border_radius="1em",
            background_color="rgb(32,29,29)",
            style={"border-style": "solid", "border-width": "thin","border-color": "rgb(173,173,173)"},
        ),
        href="https://github.com/WilsonLimSet/PodcastTest",
        target="_blank",
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.logo(),
                about_button(),
                align="center",
            ),
            rx.spacer(),
            rx.hstack(
                github_button(),
                discord_button(),
            ),
            width="100vw",
            align="center",
        ),
        background_color="rgb(32,29,29)",
        style={"position": "fixed", "top": "0", "width": "100%"},
    )