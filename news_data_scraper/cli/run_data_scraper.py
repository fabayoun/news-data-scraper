from pathlib import Path

import click

from news_data_scraper.cli.generic_errors import common_error_handling
from news_data_scraper.main import scrape_urls_and_create_word_document

_CGA_DEFAULT = True
_INPUT_FILEPATH_FROM_DIRECTORY = "input/DataScraperINPUT.txt"
_OUTPUT_FILEPATH_FROM_DIRECTORY = "NewsDataScraperOutput.docx"


@click.command()
@click.option(
    "--run-cga",
    default=_CGA_DEFAULT,
)
@click.option(
    "--input-filepath",
    default=_INPUT_FILEPATH_FROM_DIRECTORY,
)
@click.option(
    "--output-filepath",
    default=_OUTPUT_FILEPATH_FROM_DIRECTORY,
)
def run_data_scraper(run_cga: bool, input_filepath: str, output_filepath: str) -> None:
    """
    Web scraper that creates a word document from url inputs in excel, scrapes title, date and 1st 3 sentences
    """
    return scrape_urls_and_create_word_document(run_cga, input_filepath, output_filepath)


def main() -> None:
    with common_error_handling():
        run_data_scraper()
