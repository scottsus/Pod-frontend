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
    )


def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Built by ",
            link("@scottsus", "https://github.com/scottsus"),
            ", ",
            link("@wilsonLimSet", "https://github.com/wilsonLimSet"),
            ", ",
            link("@billsusanto", "https://github.com/billsusanto"),
            ", ",
            link("@ethxn.io", "https://ethxn.io"),
            ".",
        ),
        rx.spacer(),
        rx.hstack(
            icon("icons/github.svg", "https://github.com/scottsus/Pod-frontend"),
            icon("icons/linkedin.svg", "https://linkedin.com/in/wilsonLimSetiawan"),
            icon("icons/twitter.svg", "https://x.com/susantoscott"),
            icon("icons/discord.svg", "https://x.com/susantoscott"),
            spacing="4",
        ),
        width="100vw",
        padding="1em",
    )
