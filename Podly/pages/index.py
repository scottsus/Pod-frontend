"""The home page of the app."""

from Podly import styles
from Podly.templates import template
from Podly.components.card import cards

import reflex as rx
    

@rx.page(route="/", title="Home")
def index():
    return rx.box(
        rx.vstack(
            rx.heading("🫘 Cocoa Pods", padding_bottom="2em"),
            cards(),
            align="center",
            padding_x="4em",
            padding_y="2em",
        )
    )
