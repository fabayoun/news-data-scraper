import pytest

from news_data_scraper.scraper.scrape_article import scrape_all_urls, scrape_article_in_url
from news_data_scraper.scraper.scraper_classes import NewsArticle


@pytest.fixture
def input_data():
    return _INPUT_DATA

@pytest.fixture
def input_url():
    return _INPUT_URL

_INPUT_URL = "https://theenergyst.com/evs-range-anxiety-the-least-of-fleet-operators-concerns/"
_INPUT_DATA = """
    BusinessUnit|Url
    ER-RN|https://theenergyst.com/evs-range-anxiety-the-least-of-fleet-operators-concerns/
    ER-RN|https://theenergyst.com/ofgem-tightens-up-gas-and-power-transmission-spending-networks-aghast/
    ER-CGA|https://www.theguardian.com/business/2020/jun/29/make-covid-19-support-for-vulnerable-energy-customers-permanent-ofgem-tells-suppliers
    ER-RN|https://theenergyst.com/ofgem-tightens-up-gas-and-power-transmission-spending-networks-aghast/
    |https://theenergyst.com/ofgem-tightens-up-gas-and-power-transmission-spending-networks-aghast/
    xxx|https://theenergyst.com/ofgem-tightens-up-gas-and-power-transmission-spending-networks-aghast/
"""


def test_scrape_article_in_url(input_url):
    assert scrape_article_in_url(input_url) == NewsArticle(
        bu_tag=None,
        title="EVs: Range anxiety the least of fleet operators’ concerns",
        source="The Energyst",
        date="10/07/2020",
        text="""
            When it comes to electric vehicles, range anxiety appears to be the least of fleet operators’ 
            concerns, for small vans and cars at least. Polled by The Energyst, 34 fleet operators said they were 
            all planning to integrate EVs into their fleets within the next 12-24 months. Three quarters (76 per 
            cent) have at least 100 vehicles in their fleets and 58 per cent said small vans make up the majority 
            of their fleets, followed by cars as the majority (for 30 per cent).""",
        url=input_url
    )
