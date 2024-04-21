"""The search page of the app."""

from Podly import styles
from Podly.templates import template
from Podly.components.card import cards

import reflex as rx
    

@rx.page(route="/Search", title="Search")
def Search():
    return rx.box(
        rx.vstack(
            rx.button(
                rx.text("🫘 Cocoa Pods", size="7", padding_top="1em", padding_bottom="2em", color="white"),
                background_color="black", 
            ),
            cards(),
            align="center",
            padding_x="4em",
            padding_y="2em",
            background_color="black",
        )
    )
