from news_data_scraper.document.document_classes import NewsDocument, BusinessUnitSection, BusinessUnitHeader
from news_data_scraper.document.export.other_document_features.store_website_links import \
    store_podcast_and_website_links
from news_data_scraper.scraper.bu_tags import BuTag
from news_data_scraper.scraper.scraper_classes import NewsArticles


def create_document_contents(all_articles: NewsArticles, output_file_name: str, run_cga: bool) -> NewsDocument:
    rn_articles = NewsArticles()
    cga_articles = NewsArticles()
    for article in all_articles.articles:
        if article.bu_tag == BuTag.ER_RN:
            rn_articles.articles.append(article)
        if run_cga and article.bu_tag == BuTag.ER_CGA:
            cga_articles.articles.append(article)

    rn_news_section = BusinessUnitSection(
        header=BusinessUnitHeader(header="Retail & Networks", author="Fabian Schomerus", bu_tag=BuTag.ER_RN),
        all_news_articles=rn_articles,
        all_news_websites=store_podcast_and_website_links(BuTag.ER_RN),
        bu_tag=BuTag.ER_RN,
    )
    news_document = NewsDocument(business_unit_sections=[rn_news_section], name=output_file_name)

    if run_cga:
        cga_news_section = BusinessUnitSection(
            header=BusinessUnitHeader(header="Central Governments Advisory", author="Harry Allport", bu_tag=BuTag.ER_CGA),
            all_news_articles=cga_articles,
            all_news_websites=store_podcast_and_website_links(BuTag.ER_CGA),
            bu_tag=BuTag.ER_CGA,
        )
        news_document.add_section(cga_news_section)
    return news_document
