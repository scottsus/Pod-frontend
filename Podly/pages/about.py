"""The about page for the app."""

from Podly import styles
from Podly.templates import template

import reflex as rx


@template(route="/about", title="About")
def about():
    """The about page.

    Returns:
        The UI for the about page.
    """
    return rx.vstack(
        rx.hstack(
            rx.image(src="/imgs/bill.jpeg", height="300px", border_radius="1em"),
            rx.image(src="/imgs/wilson.jpeg", height="300px", border_radius="1em"),
            rx.image(src="/imgs/scott.jpeg", height="300px", border_radius="1em"),
            spacing="4",
        ),
        rx.heading(
            "Who are we?", size="9", color="white",
        ),
        rx.heading(
            "Just a bunch of pods (podcast-lovers) 🫘", size="8", color="white",
        ),
        rx.vstack(
            rx.text(
                """
                At Cocoa Pods, we leverage the Reflex framework and Gemini AI technology to transform how you experience podcasts.
                Reflex optimizes the user interface, making navigation both intuitive and fluid,
                while Gemini AI enhances content analysis, meticulously listening for and extracting key insights from each podcast.
                This synergy ensures that our platform not only simplifies discovery but also tailors personalized recommendations to your unique interests.
                """, size="5", color="white", width="40%",
            ),
            rx.text(
                """
                Understanding the challenges of the vast daily podcast releases, Cocoa Pods distills and condenses each podcast into concise insights.
                Starting from our minimalistic landing page, you can easily filter by date or topic to access podasts that offer unique insights, capturing the essence without the clutter.
                Join Cocoa Pods' community to connect deeply with the topics you care about, all through a platform that's as insightful as it is straightforward.
                """, size="5", color="white", width="40%",
            ),
            rx.text(
                "\n\nMay we too, cross paths in a podcast one day 👋", size="5", color="white", width="40%",
            ),
            style={
                "text-align": "justify",
                "alignItems": "center"
            },
        ),
        spacing="6",
        style={
            "width": "100vw",
            "min_height": "100vh",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center"
        },
    ),
