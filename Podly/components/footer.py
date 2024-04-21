"""Footer components for the app."""

from Podly import styles
from Podly.components.icon import icon

import reflex as rx

def link(text: str, href: str) -> rx.Component:
    return rx.text(
        rx.link(
            text,
            href=href,
        ),
        as_="span",
        color="inherit",
        target="_blank",
        text_decoration="none",
        _hover={
            "opacity": "0.7",
            "transition": "opacity 0.2s ease-in-out",
        }
    )


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Built by ",
                link("@scottsus", "https://github.com/scottsus"),
                ", ",
                link("@wilsonLimSet", "https://github.com/wilsonLimSet"),
                ", ",
                link("@billsusanto", "https://github.com/billsusanto"),
                ". ",
                color="rgb(173,173,173)",
                size="4",
            ),
            rx.spacer(),
            rx.hstack(
                icon("/icons/github.svg", "https://github.com/scottsus/Pod-frontend"),
                icon("/icons/linkedin.svg", "https://linkedin.com/in/wilsonLimSetiawan"),
                icon("/icons/twitter.svg", "https://x.com/susantoscott"),
                icon("/icons/discord.svg", "https://linkedin.com/in/bill-susanto"),
                spacing="5",
            ),
            width="94vw",
            padding="1em",
            style={"borderTop": "0.5px solid gray"},
        ),
        width="100vw",
        # background_color="#0b090a",
        align="center",
        padding_bottom="2em",
    )
