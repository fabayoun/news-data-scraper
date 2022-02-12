import click

from news_data_scraper.cli.generic_errors import common_error_handling
from news_data_scraper.main import scrape_urls_and_create_word_document

_CGA_DEFAULT = True


@click.command()
@click.option(
    "--run-cga",
    default=_CGA_DEFAULT,
)
def run_data_scraper(run_cga: bool) -> None:
    """
    Web scraper that creates a word document from url inputs in excel, scrapes title, date and 1st 3 sentences
    """
    return scrape_urls_and_create_word_document(run_cga)


def main() -> None:
    with common_error_handling():
        run_data_scraper()
