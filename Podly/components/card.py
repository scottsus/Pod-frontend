"""Card component for the app."""

from Podly import styles
from Podly.db.client import cli
from typing import List

import reflex as rx


class CardProps:
    def __init__(
        self,
        interviewer: str,
        interviewee: str,
        insights: List[str],
        thumbnail_url: str,
        youtube_url: str,
    ):
        self.interviewer: str = interviewer
        self.interviewee: str = interviewee
        self.insights: List[str] = insights
        self.thumbnail_url: str = thumbnail_url
        self.youtube_url:str = youtube_url

def fetch_card_data():
    data_list = cli.fetch_data()
    
    cards_data = []
    for data in data_list:
        interviewer   = data["interviewer"]
        interviewee   = data["interviewee"]
        insight_1     = data["insight_1"]
        insight_2     = data["insight_2"]
        insight_3     = data["insight_3"]
        thumbnail_url = data["thumbnail_url"]
        youtube_url   = data["youtube_url"]

        insights = [insight_1, insight_2, insight_3]
        cards_data.append(CardProps(
            interviewer, interviewee, insights, thumbnail_url, youtube_url
        ))
    
    return cards_data

def card(
    interviewer: str,
    interviewee: str,
    insights: List[str],
    thumbnail_url: str,
    youtube_url: str,
) -> rx.Component:
    """The card.

    Returns:
        The card component.
    """
    def map_rx_item(insight: str):
        return rx.list.item(insight)

    return rx.link(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.heading(interviewee, size="6"),
                        rx.heading(f"Interviewed by {interviewer}", size="4"),
                    ),
                    rx.image(src=thumbnail_url, width="100px", border_radius="5px"),
                ),

                rx.list.ordered(
                    *map(map_rx_item, insights)
                )
            ),
            padding="1em",
            _hover={
                "opacity": "0.7",
                "transition": "opacity 0.3s ease-in-out",
            },
        ),
        href=youtube_url,
        target="_blank",
        text_decoration="none",
        color="inherit",
    )

def cards() -> rx.Component:
    cards_data = fetch_card_data()
    
    def map_cards(card_data: CardProps):
        return card(
            card_data.interviewer,
            card_data.interviewee,
            card_data.insights,
            card_data.thumbnail_url,
            card_data.youtube_url,
        )

    return rx.grid(
        *map(map_cards, cards_data),
        columns="3",
        width="100%",
    )
