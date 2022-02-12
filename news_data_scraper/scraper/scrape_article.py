import logging
import math
import re
from pathlib import Path

import pandas as pd
from newspaper import Article

from news_data_scraper.scraper.get_source import get_source
from news_data_scraper.scraper.article_download_state import ArticleDownloadState
from news_data_scraper.scraper.bu_tags import BuTag
from news_data_scraper.scraper.scraper_classes import NewsArticle, NewsArticles


def scrape_all_urls(input_file_path: Path, run_cga: bool) -> NewsArticles:
    # TODO: Improve input file and logic with scraping R&N and CGA
    input_url_df = pd.read_excel(input_file_path, sheet_name=0)
    urls_rn = input_url_df['RN News'].to_list()
    urls_cga = input_url_df['CGA News'].to_list()

    all_news_articles = NewsArticles()

    bu_tag = BuTag.ER_RN
    for url in urls_rn:
        if isinstance(url, str):
            all_news_articles.articles.append(scrape_article_in_url(url, bu_tag))
        elif math.isnan(url):
            logging.info("Cell contains no link")
        else:
            logging.error("input was neither a url string or NaN")
    if run_cga:
        bu_tag = BuTag.ER_CGA
        for url in urls_cga:
            if isinstance(url, str):
                all_news_articles.articles.append(scrape_article_in_url(url, bu_tag))
            elif math.isnan(url):
                logging.info("Cell contains no link")
            else:
                logging.error("input was neither a url string or NaN")
    return all_news_articles


def scrape_article_in_url(url: str, bu_tag: BuTag = BuTag.NONE) -> NewsArticle:
    """
    Scrapes articles based on input 'url' and creates formatted output in given word document. Includes summary text
    :param url: url which will be scraped
    :param bu_tag: Business Unit for which the news article is for.
    :return: edited document object
    """
    scraped_article = Article(url)
    scraped_article.download()
    article_download_state = scraped_article.download_state

    if article_download_state == ArticleDownloadState.SUCCESS:
        scraped_article.parse()

        if scraped_article.publish_date is None:
            date_str = "No Date"
        else:
            date_only = scraped_article.publish_date.date()
            date_str = date_only.strftime('%d/%m/%Y')


        sentence_list = re.findall(r'.+', scraped_article.text)
        if len(sentence_list) > 3:
            three_sentences = [sentence_list[0], sentence_list[1], sentence_list[2]]
            sentences = ". ".join(three_sentences)

        else:
            sentences = scraped_article.text

        return NewsArticle(
            bu_tag=bu_tag,
            title=scraped_article.title,
            source=get_source(url),
            date=date_str,
            text=sentences,
            url=url
        )
    else:
        logging.error(f"Failed Download: {url}")
        return NewsArticle(bu_tag=bu_tag)
