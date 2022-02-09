from docx.shared import Pt

from document_edits.add_horizontal_break import add_page_break
from document_edits.add_hyperlink import add_hyperlink


# --------------------------- Podcast and Website Links ------------------------------- #

###Add R&N podcast and website links

def add_RN_podcast_and_website_links(document):
    links = document.add_paragraph()
    ##Add "Energy News: "
    links_l = links.add_run("Energy News: ")
    links_l.font.size = Pt(11)
    links_l.font.name = 'Calibri'
    links_l.bold = True

    ##Add Energy News Links
    add_hyperlink(links, "Utility Week", "https://utilityweek.co.uk/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Current-News", "https://www.current-news.co.uk/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "New Power", "https://www.newpower.info/category/news/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Smart Energy", "https://www.smart-energy.com/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Green Tech Media", "https://www.greentechmedia.com/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Networks Online", "https://networks.online/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Water Briefing", "https://www.waterbriefing.org/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Water Online", "https://www.wateronline.com/")

    ##Add "Energy Podcasts: "
    links = document.add_paragraph()
    links_l = links.add_run("Energy Podcasts: ")
    links_l.font.size = Pt(11)
    links_l.font.name = 'Calibri'
    links_l.bold = True

    ##Add Energy Podcasts Links
    add_hyperlink(links, "GTM: The Energy Gang", "https://www.greentechmedia.com/podcast/the-energy-gang")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "GTM: The Interchange", "https://www.greentechmedia.com/podcast/the-interchange#gs.mJy36kyT")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Redefining Energy", "https://player.fm/series/redefining-energy")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Delta Energy Environment", "https://www.delta-ee.com/TalkingNewEnergy?_cldee=aGFycnkudGF5bG9yQGJhcmluZ2EuY29t&recipientid=contact-945bce7387bce61180ddf4d04bee4450-54ffb43a590b4b7db9e5d77716ddeff1&esid=ca1bc5af-d14f-e911-80e7-ef9585e40074")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Talking New Energy", "https://www.delta-ee.com/TalkingNewEnergy?_cldee=d3RrMzQzQGFvbC5jb20%3d&recipientid=contact-8652e76380a3e71180dffdb8b794821f-7681b9488773437cbea4592f91279093&esid=7b4eaa72-d270-e911-80e7-ef9585e40074")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Talking New Energy", "https://open.spotify.com/episode/4wqNzmaSozqVjukUgtBsP1?si=3BG654-IQW21-1Otgi2ktw")

    ##add page break line underneath podcast links
    add_page_break(links)

###Add CGA podcast and website links
def add_CGA_podcast_and_website_links(document):
    ##Add "CGA News: "
    links = document.add_paragraph()
    links_l = links.add_run("CGA News: ")
    links_l.font.size = Pt(11)
    links_l.font.name = 'Calibri'
    links_l.bold = True

    ##Add CGA News links
    add_hyperlink(links, "Civil Service World", "https://www.civilserviceworld.com/")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "Institute for Government", "https://www.instituteforgovernment.org.uk/")

    ##Add "CGA Podcasts: "
    links = document.add_paragraph()
    links_l = links.add_run("CGA Podcasts: ")
    links_l.font.size = Pt(11)
    links_l.font.name = 'Calibri'
    links_l.bold = True

    ##Add CGA Podcast links
    add_hyperlink(links, "Times Red Box", "https://soundcloud.com/times-comment")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "BBC Brexitcast", "https://www.bbc.co.uk/programmes/p05299nl/episodes/player")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "FT Politics", "https://www.ft.com/uk-politics-podcast")
    links_l = links.add_run(" // ")
    add_hyperlink(links, "One Team Gov", "https://www.oneteamgov.uk/podcast")

    ##add page break after CGA links
    add_page_break(links)