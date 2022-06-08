"""
This Python script is intended to retrieve important data from all trails listed on the WTA
website. 
"""

# WTA has 132 pages of hikes, each page with 30 trails
# This function creates a link to each page of 30

def makePageList():

    link_format = 'https://www.wta.org/go-outside/hikes?b_start:int='
    all_links = []

    #132 pages of hikes
    for i in range(132):
        page_link = link_format + str(i * 30)
        all_links.append(pagelink)
    return all_links



# This function retrieves links to each trail on page containing 30 trails
def getPage(all_links):
    pass

# This function finds the hike coordinates, name, and region for each link passed
# and adds the data to a CSV file
def findHikeData(trail_link):
    pass



#--------------- calling functions ---------------

all_pages = makePageList()