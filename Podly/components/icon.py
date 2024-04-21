"""Icon component for the app."""

from Podly import styles

import reflex as rx


def icon(path: str, href: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=path,
            width="25px",
            _hover={
                "opacity": "0.7",
                "transition": "opacity 0.3s ease-in-out",
            },
        ),
        href=href,
        target="_blank",
    )
