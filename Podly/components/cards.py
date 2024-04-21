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
        publish_date: str,
        tag: str,
    ):
        self.interviewer: str = interviewer
        self.interviewee: str = interviewee
        self.insights: List[str] = insights
        self.thumbnail_url: str = thumbnail_url
        self.youtube_url: str = youtube_url
        self.publish_date: str = publish_date
        self.tag: str = tag

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
        publish_date  = data["publish_date"]
        tag           = data["tag"]

        insights_list = [insight_1, insight_2, insight_3]
        insights = [insight for insight in insights_list if insight != ""]
        cards_data.append(CardProps(
            interviewer, interviewee, insights, thumbnail_url, youtube_url, publish_date, tag,
        ))
    
    return cards_data

def card(
    interviewer: str,
    interviewee: str,
    insights: List[str],
    thumbnail_url: str,
    youtube_url: str,
    publish_date: str,
) -> rx.Component:
    """The card.

    Returns:
        The card component.
    """
    def map_rx_item(insight: str):
        MAX_INSIGHT_LEN = 80
        if len(insight) >= MAX_INSIGHT_LEN:
            insight = insight[:MAX_INSIGHT_LEN] + "..."

        return rx.list.item(
            rx.text(
                insight,
            ),
            padding_y="1em",
            height="4em",

            # this may be unsupported by reflex for now
            # text_overflow="ellipsis",
        )
    
    return rx.vstack(
            rx.box(
                rx.image(
                    src=thumbnail_url,
                    width="100%",
                    margin_y="-2.4em",
                ),
                height="12em",
                overflow="hidden",
            ),
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.heading(interviewee, size="8", color="black"),
                        rx.heading(f"Interviewed by {interviewer}", size="4"),

                        rx.box(
                            rx.list.ordered(
                                *map(map_rx_item, insights),
                            ),
                            rx.spacer(),
                        ),
                    ),
                ),
                rx.spacer(),
                rx.box(
                    rx.hstack(
                        rx.text(publish_date),
                        rx.spacer(),
                        rx.link(
                            rx.button(
                                rx.text("Watch podcast", color="#343a40"),
                                background_color="#6c757d",
                                cursor="pointer",
                                _hover={
                                    "opacity": "0.8",
                                    "transition": "opacity 0.2s ease-in-out",
                                }
                            ),
                            href=youtube_url,
                            target="_blank",
                            text_decoration="none",
                            color="inherit",
                        ),
                        align="center",
                    ),
                    width="100%",
                    padding_x="0.2em",
                    padding_y="0.4em",
                    border_top="2px solid black",
                ),
                align="center",
                padding_x="1em",
                height="23em",
            ),
            height="36em",
            _hover={
                "scale": "1.01",
                "transition": "scale 0.25s ease-in-out",
            },
            background_color="#adb5bd",
            border_radius="11px",
            overflow="hidden",
        )

def cards(FilterState) -> rx.Component:
    cards_data = fetch_card_data()
    
    def map_cards(card_data: CardProps):
        return rx.cond(
            FilterState.filter_type == "",
            card(
                card_data.interviewer,
                card_data.interviewee,
                card_data.insights,
                card_data.thumbnail_url,
                card_data.youtube_url,
                card_data.publish_date,
            ),
            rx.cond(
                FilterState.filter_type == card_data.tag,
                card(
                    card_data.interviewer,
                    card_data.interviewee,
                    card_data.insights,
                    card_data.thumbnail_url,
                    card_data.youtube_url,
                    card_data.publish_date,
                ),
                None,
            ),
        )

    def filter_nones(items):
        return [item for item in items if item is not None]

    return rx.grid(
        *filter_nones(map(map_cards, cards_data)),
        columns="4",
        width="100%",
        gap="20px",
    )
