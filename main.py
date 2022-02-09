import datetime
from pathlib import Path
import logging

import pandas as pd
from docx import Document

from document_edits.add_page_headers import add_RN_heading, add_CGA_heading_author
from document_edits.add_podcasts_and_websites import add_RN_podcast_and_website_links, add_CGA_podcast_and_website_links
from scrape_article import scrape_article_for_email, scrape_all_urls

OUTPUT_FILE_NAME = "Output/NewsDataScraperOutput"
DIRECTORY_ROOT = Path(__file__).parent
INPUT_URL = "Input/DataScraperINPUT.xlsx"


def data_scraper():
    """
    Create Word Document for R&N News Round. Takes url inputs from excel, scrapes title, date and 1st 3 sentences
    :return: document
    """

    # read excel and create dictionaries of R&N and CGA urls which will be scraped
    input_url_df = pd.read_excel(DIRECTORY_ROOT / INPUT_URL, sheet_name=0)
    urls_rn = input_url_df['RN News'].to_list()
    urls_cga = input_url_df['CGA News'].to_list()

    # Create document object from class to create a new word document for article summaries
    document = Document()

    # add R&N Heading
    add_RN_heading(document)

    # run loop to scrape article for each url in R&N dictionary
    scrape_all_urls(urls_rn, document)

    # add R&N podcast and news website links, and break line
    add_RN_podcast_and_website_links(document)

    # add CGA Heading and author
    add_CGA_heading_author(document)

    # run loop to scrape article for each url in CGA dictionary
    scrape_all_urls(urls_cga, document)

    # add podcast and news website links, and break line
    add_CGA_podcast_and_website_links(document)

    # Save document with new version number and current date
    # determine current date and turn into string
    now = datetime.datetime.now().strftime('%Y_%m_%d %Hh%Mm')

    # save file
    output_file_name = f"{OUTPUT_FILE_NAME}_{now}.docx"
    file_path_email = f"{DIRECTORY_ROOT}/{output_file_name}"
    document.save(file_path_email)
    logging.info(f"Completed: {output_file_name}")
    pass


if __name__ == '__main__':
    data_scraper()
