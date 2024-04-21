"""The home page of the app."""

from Podly import styles
from Podly.templates import template
from Podly.components.cards import cards

import reflex as rx
    

@template(route="/", title="Home")
def index():
    class FilterState(rx.State):
        filter_type: str = ""

        def apply_filter(self, filter_type: str):
            self.filter_type = filter_type

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.spacer(),
                rx.select(
                    ["Tech", "Business", "Sports",],
                    placeholder="💃 Select your favorite category",
                    size="3",
                    on_change=FilterState.apply_filter,
                ),
                padding_y="2em",
            ),
            cards(FilterState),
            align="center",
            padding_x="4em",
            padding_y="2em",
            background_color="#161a1d"
        ),
    )
