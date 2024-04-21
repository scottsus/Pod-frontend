"""Navbar component for the app."""

from Podly import styles
from Podly.components.callout import callout

import reflex as rx

def about_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.text(
                "About",
                font_size="21px",
                color="white",
                _hover={
                    "text-decoration": "underline",
                    "color": "#e93d83",
                    "transition": "color 0.2s ease-in-out",
                },
            ),
            padding_y="1.5em",
            border_radius="1em",
            background_color="transparent",
            cursor="pointer",
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
            border_radius="8px",
            height="42px",
            background_color="rgb(32,29,29)",
            style={"border-style": "solid", "border-width": "thin","border-color": "rgb(173,173,173)"},
            _hover={
                "opacity": "0.7",
                "transition": "opacity 0.2s ease-in-out",
            },
            cursor="pointer"
        ),
        href="https://github.com/scottsus/Pod",
        target="_blank",
    )

def github_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src="/icons/github.svg", width="24px"),
                rx.text("GitHub", font_size="16px", color="rgb(173,173,173)",),
                callout(">10+"),
                align="center",
            ),
            padding_y="1.5em",
            padding_x="2em",
            border_radius="8px",
            background_color="rgb(32,29,29)",
            style={"border-style": "solid", "border-width": "thin","border-color": "rgb(173,173,173)"},
            _hover={
                "opacity": "0.7",
                "transition": "opacity 0.2s ease-in-out",
            },
            cursor="pointer"
        ),
        href="https://github.com/scottsus/Pod",
        target="_blank",
    )

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.link(
                    rx.heading(
                        "🫘 CocoaPods",
                        size="7",
                        color="white",
                        cursor="pointer",
                        _hover={
                            "color": "#e93d83",
                            "transition": "color 0.2s ease-in-out",
                        }
                    ),
                    href="/",
                ),
                about_button(),
                align="center",
                spacing="6",
            ),
            rx.spacer(),
            rx.hstack(
                github_button(),
                discord_button(),
                spacing="4",
            ),
            width="90vw",
            align="center",
        ),
        height="5em",
        justify="center",
        align="center",
        padding="1em",
        background_color="#0b090a",
        style={
            "position": "sticky",
            "top": "0",
            "width": "100%"
        },
    )