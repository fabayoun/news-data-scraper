from dataclasses import dataclass
from typing import List, Dict

from news_data_scraper.scraper.bu_tags import BuTag
from news_data_scraper.scraper.scraper_classes import AllNewsArticles


@dataclass
class BusinessUnitHeader:
    """Class for business unit headers which are used to divide the articles into sections"""
    header: str
    author: str
    bu_tag: BuTag


@dataclass
class AllBusinessUnitHeaders:
    """Class containing all Business Unit Headers"""
    headers: List[BusinessUnitHeader]


@dataclass
class AllNewsWebsites:
    """Class containing all News Websites"""
    news_sites: Dict[str, str]
    podcast_sites: Dict[str, str]
    bu_tag: BuTag


@dataclass
class NewsSection:
    """Class containing all document features"""
    business_unit_header: BusinessUnitHeader
    all_news_articles: AllNewsArticles
    all_news_websites: AllNewsWebsites
    bu_tag: BuTag


@dataclass
class NewsDocument:
    news_sections: List[NewsSection]

    def add_section(self, news_section: NewsSection):
        self.news_sections.append(news_section)
