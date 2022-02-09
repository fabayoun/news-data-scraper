from newspaper import Article

from document_edits.add_article_text import add_article_text
from document_edits.add_title_source_date import add_title_source_date
from document_edits.add_hyperlink import add_hyperlink


def scrape_article_for_email(url, document):
    """
    Scrapes articles based on input 'url' and creates formatted output in given word document. Includes summary text
    :param url:
    :return: edited text
    """
    ##defines failed download state
    class ArticleDownloadState(object):
        NOT_STARTED = 0
        FAILED_RESPONSE = 1
        SUCCESS = 2

    ##defines object for each input "url", downloads and parses article if downloadable, and gives error message and template in word otherwise
    #define article object and download
    article = Article(url)
    article.download()

    #if not able to download, create template with "Title, Source, Date and Text" already formatted and hyperlink
    if article.download_state == ArticleDownloadState.FAILED_RESPONSE:
        print("Failed Download: " + url)

        #creates template paragraph with error message
        l = document.add_paragraph()
        l.add_run("Failed Download: ")

        #adds "Title", source(as usual) and "Date" and "Text"
        add_title_source_date("Title", url, "Date", document)
        add_article_text("Text", document)

        #adds hyperlink to article
        l_2 = document.add_paragraph()
        add_hyperlink(l_2, url, url)

        #add space after article
        space = document.add_paragraph()

    #if able to download, parse article and create summary
    else:
        article.parse()
        #add formatted title, source, date, and first 3 sentences to given document
        add_title_source_date(article.title, url, article.publish_date, document)
        add_article_text(article.text, document)

        #Add link to document
        l = document.add_paragraph()
        add_hyperlink(l, url, url)

        #Add space after article
        space = document.add_paragraph()
    pass