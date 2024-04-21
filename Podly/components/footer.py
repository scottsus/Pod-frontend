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
            rx.link("@scottsus", href="https://github.com/scottsus", target="_blank"),
            ", ",
            rx.link("@wilsonLimSet", href="https://github.com/wilsonLimSet", target="_blank"),
            ", ",
            rx.link("@billsusanto", href="https://github.com/billsusanto", target="_blank"),
            ". ",
            color="rgb(173,173,173)"
        ),
        rx.spacer(),
        rx.hstack(
            rx.link(rx.image(src="/icons/github.svg"), href="https://github.com/scottsus/Pod-frontend", target="_blank"),
            rx.link(rx.image(src="/icons/linkedin.svg"), href="https://linkedin.com/in/wilsonLimSetiawan", target="_blank"),
            rx.link(rx.image(src="/icons/twitter.svg"), href="https://x.com/susantoscott", target="_blank"),
            rx.link(rx.image(src="/icons/discord.svg"), href="https://x.com/susantoscott", target="_blank"),
            spacing="4",
        ),
        width="100vw",
        padding="1em",
        background_color="#0b090a",
        style={"borderTop": "2px solid white"},
    )
