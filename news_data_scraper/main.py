import datetime
from pathlib import Path
import logging

import pandas as pd
from docx import Document

from config_logger import setup_logging
from news_data_scraper.document_edits.format_document import format_document
from news_data_scraper.other_document_features.document_feature_classes import BusinessUnitHeader, NewsDocument, \
    NewsSection
from news_data_scraper.other_document_features.store_website_links import store_podcast_and_website_links
from news_data_scraper.scraper.bu_tags import BuTag
from news_data_scraper.scraper.scrape_article import scrape_all_urls

OUTPUT_FILE_NAME = "output/NewsDataScraperOutput"
DIRECTORY_ROOT = Path(__file__).parent.parent
INPUT_URL = "input/DataScraperINPUT.xlsx"


def document_creator(run_cga: bool) -> None:
    """
    Web scraper that creates a word document from url inputs in excel, scrapes title, date and 1st 3 sentences
    :return: document
    """
    setup_logging()

    # read excel and create dictionaries of R&N and CGA urls which will be scraped
    # TODO: Split out scraping
    document_contents = create_document_contents(run_cga)

    # Create word document
    # TODO: Export to word function
    document = Document()
    format_document(document, document_contents)

    # Save document with new version number and current date
    # TODO: Create generate_filename function, which is sent into export to word, document contents and file path
    now = datetime.datetime.now().strftime('%Y%m%d_%Hh%Mm')
    output_file_name = f"{OUTPUT_FILE_NAME}_{now}.docx"
    file_path_email = f"{DIRECTORY_ROOT}/{output_file_name}"
    document.save(file_path_email)
    logging.info(f"Completed: {output_file_name}")
    pass


def create_document_contents(run_cga: bool) -> NewsDocument:
    input_url_df = pd.read_excel(DIRECTORY_ROOT / INPUT_URL, sheet_name=0)
    urls_rn = input_url_df['RN News'].to_list()
    urls_cga = input_url_df['CGA News'].to_list()

    rn_bu_tag = BuTag.ER_RN
    rn_news_section = NewsSection(
        business_unit_header=BusinessUnitHeader(header="Retail & Networks", author="Fabian Schomerus", bu_tag=rn_bu_tag),
        all_news_articles=scrape_all_urls(urls_rn, rn_bu_tag),
        all_news_websites=store_podcast_and_website_links(rn_bu_tag),
        bu_tag=rn_bu_tag,
    )
    news_document = NewsDocument(news_sections=[rn_news_section])

    if run_cga:
        cga_bu_tag = BuTag.ER_CGA
        cga_news_section = NewsSection(
            business_unit_header=BusinessUnitHeader(header="Central Governments Advisory", author="Harry Allport", bu_tag=cga_bu_tag),
            all_news_articles=scrape_all_urls(urls_cga, cga_bu_tag),
            all_news_websites=store_podcast_and_website_links(cga_bu_tag),
            bu_tag=cga_bu_tag,
        )
        news_document.add_section(cga_news_section)
    return news_document


if __name__ == '__main__':
    document_creator(run_cga=True)
