import click

from cli.generic_errors import common_error_handling
from main import data_scraper

CGA_DEFAULT = True


@click.command()
@click.option(
    "--run-cga",
    default=CGA_DEFAULT,
)
def run_data_scraper(run_cga):
    """
    Web scraper that creates a word document from url inputs in excel, scrapes title, date and 1st 3 sentences
    """
    return data_scraper(run_cga)


def main():
    with common_error_handling():
        run_data_scraper()
