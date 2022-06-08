"""
This Python script is intended to retrieve important data from all trails listed on the WTA
website. 
"""

def makePageLinks():

    link_format = 'https://www.wta.org/go-outside/hikes?b_start:int='
    all_links = []

    #132 pages of hikes
    for i in range(132):
        pagelink = link_format + str(i * 30)
        all_links.append(pagelink)
    print(len(all_links))

makePageLinks()