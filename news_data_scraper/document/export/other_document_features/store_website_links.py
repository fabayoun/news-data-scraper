from news_data_scraper.document.document_classes import NewsWebsites
from news_data_scraper.scraper.bu_tags import BuTag

_ENERGY_NEWS_NAME_TO_URL = {
    "Utility Week": r"https://utilityweek.co.uk/",
    "Current-News": r"https://www.current-news.co.uk/",
    "New Power": r"https://www.newpower.info/category/news/",
    "Smart Energy": r"https://www.smart-energy.com/",
    "Green Tech Media": r"https://www.greentechmedia.com/",
    "Networks Online": r"https://networks.online/",
    "Water Briefing": r"https://www.waterbriefing.org/",
    "Water Online": r"https://www.wateronline.com/",
}
_ENERGY_PODCASTS_NAME_TO_URL = {
    "GTM: The Energy Gang": r"https://www.greentechmedia.com/podcast/the-energy-gang",
    "GTM: The Interchange": r"https://www.greentechmedia.com/podcast/the-interchange#gs.mJy36kyT",
    "Redefining Energy": r"https://player.fm/series/redefining-energy",
    "Delta Energy Environment": r"https://www.delta-ee.com/TalkingNewEnergy?_cldee=aGFycnkudGF5bG9yQGJhcmluZ2EuY29t&recipientid=contact-945bce7387bce61180ddf4d04bee4450-54ffb43a590b4b7db9e5d77716ddeff1&esid=ca1bc5af-d14f-e911-80e7-ef9585e40074",
    "Talking New Energy": r"https://www.delta-ee.com/TalkingNewEnergy?_cldee=d3RrMzQzQGFvbC5jb20%3d&recipientid=contact-8652e76380a3e71180dffdb8b794821f-7681b9488773437cbea4592f91279093&esid=7b4eaa72-d270-e911-80e7-ef9585e40074",
    "Spotify Talking New Energy": r"https://open.spotify.com/episode/4wqNzmaSozqVjukUgtBsP1?si=3BG654-IQW21-1Otgi2ktw",
}
_CGA_NEWS_NAME_TO_URL = {
    "Civil Service World": r"https://www.civilserviceworld.com/",
    "Institute for Government": r"https://www.instituteforgovernment.org.uk/",
}
_CGA_PODCASTS_NAME_TO_URL = {
    "Times Red Box": r"https://soundcloud.com/times-comment",
    "BBC Brexitcast": r"https://www.bbc.co.uk/programmes/p05299nl/episodes/player",
    "FT Politics": r"https://www.ft.com/uk-politics-podcast",
    "One Team Gov": r"https://www.oneteamgov.uk/podcast",
}


def store_podcast_and_website_links(bu_tag: BuTag) -> NewsWebsites:
    """
    Add R&N podcast and website links
    :param bu_tag: document object to be edited
    :return: edited document
    """
    # Add "Energy News: "
    if bu_tag == BuTag.ER_RN:
        return NewsWebsites(news_sites=_ENERGY_NEWS_NAME_TO_URL, podcast_sites=_ENERGY_PODCASTS_NAME_TO_URL, bu_tag=bu_tag)
    elif bu_tag == BuTag.ER_CGA:
        return NewsWebsites(news_sites=_CGA_NEWS_NAME_TO_URL, podcast_sites=_CGA_PODCASTS_NAME_TO_URL, bu_tag=bu_tag)
    elif bu_tag == BuTag.NONE:
        return NewsWebsites()
    else:
        raise Exception("This BU tag doesn't exist exists")
