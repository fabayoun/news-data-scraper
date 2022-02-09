import datetime
import math
from pathlib import Path
import logging

import pandas as pd
from docx import Document

from document_edits.add_page_headers import add_RN_heading, add_CGA_heading_author
from document_edits.add_podcasts_and_websites import add_RN_podcast_and_website_links, add_CGA_podcast_and_website_links
from scrape_article import scrape_article_for_email

VERSION_NUMBER = 15
DIRECTORY_ROOT = Path(__file__).parent
INPUT_URL = "Input/DataScraperINPUT.xlsx"
# r'/Users/Fabian.Schomerus/PycharmProjects/news-data-scraper/

def data_scraper():
    """
    Create Word Document for R&N News Round. Takes url inputs from excel, scrapes title, date and 1st 3 sentences
    :return: document
    """

    # read excel and create dictionaries of R&N and CGA urls which will be scraped
    input_url_df = pd.read_excel(DIRECTORY_ROOT / INPUT_URL, sheet_name=0)
    url_RN = input_url_df['RN News'].to_dict()
    url_CGA = input_url_df['CGA News'].to_dict()

    # Create document object from class to create a new word document for article summaries
    document = Document()

    # add R&N Heading
    add_RN_heading(document)

    # run loop to scrape article for each url in R&N dictionary
    for i in url_RN:
        news_RN = url_RN[i]
        # sorts out empty table entries within excel, useful when no. of rows for R&N and CGA are not equal.
        if type(news_RN) == str:
            scrape_article_for_email(news_RN, document)
        elif math.isnan(news_RN) == True:
            logging.info("R&N cell contains no link")
        else:
            logging.error("Input Url was neither a string or NaN")

    # add R&N podcast and news website links, and break line
    add_RN_podcast_and_website_links(document)

    # add CGA Heading and author
    add_CGA_heading_author(document)

    # run loop to scrape article for each url in CGA dictionary
    for k in url_CGA:
        news_CGA = url_CGA[k]
        # sorts out empty table entries within excel, useful when no. of rows for R&N and CGA are not equal.
        if type(news_CGA) == str:
            scrape_article_for_email(news_CGA, document)
        elif math.isnan(news_CGA) == True:
            logging.info("R&N cell contains no link")
        else:
            logging.error("Input Url was neither a string or NaN")

    # add podcast and news website links, and break line
    add_CGA_podcast_and_website_links(document)

    # Save document with new version number and current date
    # determine current date and turn into string
    now = datetime.datetime.now()
    now_str = now.strftime('%Y_%m_%d %Hh%Mm')

    # add version number
    version_number_str = str(VERSION_NUMBER)

    # save file
    file_name_email = f"R&N News Data Scraper Output v_{version_number_str}_{now_str}"
    file_path_email = f"/Users/Fabian.Schomerus/PycharmProjects/news-data-scraper/Output/{file_name_email}.docx"
    document.save(file_path_email)
    print(f"Completed: {file_name_email}")
    pass


if __name__ == '__main__':
    data_scraper()
