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
    return rx.box(
        rx.vstack(
            rx.heading(
                "About Us", size="9", color="white",
            ),
            rx.spacer(),
            rx.heading(
                "Discover the Heart of Podcasting!", size="8", color="white",
            ),
            rx.spacer(),
            rx.vstack(
                rx.heading(
                    "At Cocoa Pods, we leverage the Reflex framework and Gemini AI technology to transform how you experience podcasts. Reflex optimizes the user interface, making navigation both intuitive and fluid, while Gemini AI enhances content analysis, meticulously listening for and extracting key insights from each podcast. This synergy ensures that our platform not only simplifies discovery but also tailors personalized recommendations to your unique interests.", size="5", color="white", width="50%",
                ),
                rx.spacer(),
                rx.heading(
                    "Understanding the challenges of the vast daily podcast releases, Cocoa Pods distills and condenses each podcast into concise insights. Starting from our minimalistic landing page, you can easily filter by date or topic to access podasts that offer unique insights, capturing the essence without the clutter. Join Cocoa Pods' community to connect deeply with the topics you care about, all through a platform that's as insightful as it is straightforward.", size="5", color="white", width="50%",
                ),
                style={"text-align": "center", "alignItems": "center"},
            ),
            style={"text-align": "justify", "alignItems": "center"},
            gap="20px",
        ),
        style={"width": "100vw", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center", "alignItems": "center"},
        background_color="black",
    )
