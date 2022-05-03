from dataclasses import dataclass, field
from typing import List

from news_data_scraper.scraper.bu_tags import BuTag


@dataclass
class NewsArticle:
    """Class for scraped news article"""

    bu_tag: BuTag = BuTag.NONE
    title: str = "Title"
    source: str = "Source"
    date: str = "Date"
    text: str = "Text"
    url: str = "Url"


@dataclass
class NewsArticles:
    """Class containing all scraped news articles"""

    articles: List[NewsArticle] = field(default_factory=list)
