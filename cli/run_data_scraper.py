import click

from cli.generic_errors import common_error_handling
from main import data_scraper


@click.command()
def run_data_scraper():
    return data_scraper()


def main():
    with common_error_handling():
        run_data_scraper()
