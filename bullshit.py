def photo():
    import urllib3
    URL = "https://kpolyakov.spb.ru/cms/images/3652.gif"
    p = urllib3.urlopen(URL)
    return p
