import re

# dictionary which defines source, based on url. Useful for creating formatted source
URL_TO_NEW_SOURCE = {
    "current-news": "Current News",
    "thesun": "The Sun",
    "bbc": "BBC",
    "goodenergy": "Good Energy",
    "bnef": "BNEF",
    "instituteforgovernment": "Institute for Government",
    "civilserviceworld": "CSW",
    "theguardian": "The Guardian",
    "itv": "ITV",
    "thedrum": "The Drum",
    "independent": "The Independent",
    "Source": "Source",  # for template when article can't be downloaded (currently not in use)
    "sky": "Sky News",
    "thetimes": "The Times",
    "ft": "The Financial Times",
    "moneysavingexpert": "The Money Saving Expert",
    "telegraph": "The Telegraph",
    "theenergyst": "The Energyst",
    "engerati": "Engerati",
    "openaccessgovernment": "Open Access Government",
    "publictechnology": "Public Technology",
    "room151": "Room 515",
    "consultancy": "Consultancy.UK",
    "wired": "Wired",
    "itproportal": "ITProPortal",
    "tortoisemedia": "Tortoise Media",
    "zap-map": "Zap Map",
    "cityam": "City A.M.",
    "utilityweek": "Utility Week",
    "arstechnica": "Arstechnica",
    "bpchargemaster": "Bpchargemaster",
    "weforum": "Weforum",
    "politicshome": "Politicshome",
    "energyvoice": "Energy Voice",
    "ofwat": "Ofwat",
    "forbes": "Forbes",
    "theregister": "The Register"
}


def get_source(url):
    if "http" in url:
        source_split = re.split("[/.]", url)
        if "co" in source_split:
            n = source_split.index("co")
            check_source = source_split[n - 1]
        elif "com" in source_split:
            n = source_split.index("com")
            check_source = source_split[n - 1]
        elif "org" in source_split:
            n = source_split.index("org")
            check_source = source_split[n - 1]
        elif "net" in source_split:
            n = source_split.index("net")
            check_source = source_split[n - 1]
        else:
            check_source = url
    else:
        check_source = url

    if check_source in URL_TO_NEW_SOURCE:
        return URL_TO_NEW_SOURCE[check_source]
    else:
        return "Source"
