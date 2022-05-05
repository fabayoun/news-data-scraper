from dataclasses import dataclass, field
from typing import List, Dict

from news_data_scraper.scraper.bu_tags import BuTag
from news_data_scraper.scraper.scraper_classes import NewsArticles


@dataclass
class BusinessUnitHeader:
    """Class for business unit headers which are used to divide the articles into sections"""

    header: str
    author: str
    bu_tag: BuTag = BuTag.NONE


@dataclass
class NewsWebsites:
    """Class containing all News Websites"""

    news_sites: Dict[str, str] = field(default_factory=dict)
    podcast_sites: Dict[str, str] = field(default_factory=dict)
    bu_tag: BuTag = BuTag.NONE


@dataclass
class BusinessUnitSection:
    """Class containing all document features"""

    header: BusinessUnitHeader
    all_news_articles: NewsArticles
    all_news_websites: NewsWebsites
    bu_tag: BuTag = BuTag.NONE


@dataclass
class NewsDocument:
    business_unit_sections: List[BusinessUnitSection]
    name: str

    def add_section(self, new_section: BusinessUnitSection):
        self.business_unit_sections.append(new_section)
