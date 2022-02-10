import logging
import math

from newspaper import Article

from news_data_scraper.document_edits.add_article_text import add_article_text
from news_data_scraper.document_edits.add_title_source_date import add_title_source_date
from news_data_scraper.document_edits.add_hyperlink import add_hyperlink
from news_data_scraper.document_edits.article_download_state import ArticleDownloadState


def scrape_all_urls(urls, document):
    for url in urls:
        # sorts out empty table entries within excel, useful when no. of rows for R&N and CGA are not equal.
        if isinstance(url, str):
            scrape_article_in_url(url, document)
        elif math.isnan(url):
            logging.info("Cell contains no link")
        else:
            logging.error("input was neither a url string or NaN")
    pass


def scrape_article_in_url(url, document):
    """
    Scrapes articles based on input 'url' and creates formatted output in given word document. Includes summary text
    :param url: url which will be scraped
    :param document: document object
    :return: edited document object
    """
    article = Article(url)
    article.download()
    article_download_state = article.download_state

    # if not able to download, create template with "Title, Source, Date and Text" already formatted and hyperlink
    if article_download_state == ArticleDownloadState.FAILED_RESPONSE:
        logging.error(f"Failed Download: {url}")

        document.add_paragraph()
        document.add_run("Failed Download: ")

        title = "Title"
        date = "Date"
        text = "Text"

    if article_download_state == ArticleDownloadState.SUCCESS:
        article.parse()

        title = article.title
        date = article.publish_date
        text = article.text

    add_title_source_date(title, url, date, document, article_download_state)
    add_article_text(text, document, article_download_state)

    paragraph = document.add_paragraph()
    add_hyperlink(paragraph, url, url)
    document.add_paragraph()
    pass