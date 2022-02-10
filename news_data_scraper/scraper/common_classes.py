from dataclasses import dataclass
from typing import List


@dataclass
class NewsArticle:
    """Class for scraped news article"""
    bu_tag: str
    title: str = "Title"
    source: str = "Source"
    date: str = "Date"
    text: str = "Text"
    url: str = "Url"


@dataclass
class AllNewsArticles:
    """Class containing all scraped news articles"""
    articles: List[NewsArticle]


@dataclass
class BusinessUnitHeader:
    """Class for business unit headers which are used to divide the articles into sections"""
    title: str
    author: str
    bu_tag: str


@dataclass
class AllBusinessUnitHeaders:
    """Class containing all Business Unit Headers"""
    headers: List[BusinessUnitHeader]


@dataclass
class NewsWebsite:
    """Class for useful news websites and podcasts"""
    name: str
    url: str
    website_type: str
    bu_tag: str

@dataclass
class AllNewsWebsites:
    """Class containing all News Websites"""
    websites: List[NewsWebsite]
