"""The home page of the app."""

from Podly import styles
from Podly.templates import template
from Podly.components.card import cards

import reflex as rx
    

@rx.page(route="/", title="Home")
def index():
    class ClickState(rx.State):
        # when u press the button "tech" -> filter ONLY tech videos


        pass
        
            

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.button(
                    rx.text("🫘 Cocoa Pods", size="7", padding_top="1em", padding_bottom="2em", color="white",),
                    height="60px",
                    background_color="black", 
                ),
                rx.spacer(),
                # rx.button(
                #     rx.text(
                #         "Filter", size="4", padding_top="2em", padding_bottom="2em", color="white",
                #         ),
                #     background_color="gray",
                # ),
                rx.select(
                    ["Tech", "Finance", "Sport",],
                    placeholder="Filter",
                    size="3",
                    # on_change=lambda sort_value: State.sort_values(sort_value),
                    font_family="Inter",
                ),
                witdth="100px",
            ),
            cards(),
            align="center",
            padding_x="4em",
            padding_y="2em",
        ),
        background_color="black",
    )
