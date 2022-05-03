import datetime
from pathlib import Path

from news_data_scraper.config_logger import setup_logging
from news_data_scraper.document.create_document_contents import create_document_contents
from news_data_scraper.document.export.word.export_to_word import export_to_word
from news_data_scraper.scraper.scrape_article import scrape_all_urls

_DIRECTORY_ROOT = Path(__file__).parent.parent


def scrape_urls_and_create_word_document(
    run_cga: bool, input_filepath: str, output_filepath: str
) -> None:
    """
    Web scraper that creates a word document from url inputs in txt, scrapes title, date and 1st 3 sentences
    :return: document
    """
    setup_logging()

    # read txt and create dictionaries of R&N and CGA urls which will be scraped
    input_file_path = _DIRECTORY_ROOT / input_filepath
    all_articles = scrape_all_urls(input_file_path, run_cga)

    output_file_name = create_document_name(output_filepath)
    document_contents = create_document_contents(
        all_articles, output_file_name, run_cga
    )

    full_output_file_path = create_document_filepath(output_file_name)
    export_to_word(document_contents, output_file_name, full_output_file_path)
    pass


def create_document_name(output_file_name: str) -> str:
    now = datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm")
    output_file_name = f"{output_file_name.replace('.docx', '')}_{now}.docx"
    return output_file_name


def create_document_filepath(output_file_name: str) -> Path:
    return Path(f"{_DIRECTORY_ROOT}/{output_file_name}")


if __name__ == "__main__":
    scrape_urls_and_create_word_document(
        run_cga=True,
        input_filepath="input/DataScraperINPUT.txt",
        output_filepath="NewsDataScraperOutput.docx",
    )
