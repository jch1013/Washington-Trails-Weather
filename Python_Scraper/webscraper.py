"""
This Python script is intended to retrieve important data from all trails listed on the WTA
website. 
"""

# imports
import bs4
import requests
import csv


# WTA has 132 pages of hikes, each page with 30 trails

# This function creates a link to each page of 30


def makePageList():
    link_format = 'https://www.wta.org/go-outside/hikes?b_start:int='
    all_links = []

    # 132 pages of hikes
    for i in range(132):
        page_link = link_format + str(i * 30)
        all_links.append(page_link)
    return all_links


# This function returns links to each trail on page containing 30 trails

def getFromPage(page_link):
    trail_links = []
    page_req = requests.get(page_link)
    html_content = bs4.BeautifulSoup(page_req.text, "html.parser")
    trails = html_content.select('.listitem-title a')
    for trail in trails:
        trail_links.append(trail['href'])
    return trail_links


# This function finds the hike coordinates, name, and region for each link passed
# and adds the data to a CSV file
def findHikeData(trail_link):
    trail_req = requests.get(trail_link)
    html_content = bs4.BeautifulSoup(trail_req.text, "html.parser")
    trail_name = html_content.select(".hike-major-section h1")[0].text
    trail_region = html_content.select('.wta-icon-headline__text')[0].text

    try:
        trail_image = html_content.select('.wta-ratio-figure__image')[0]['src']
    except:
        trail_image = None

    try:
        trail_coordinates = html_content.select('.latlong span')
        trail_lat = trail_coordinates[0].text
        trail_long = trail_coordinates[1].text
    except:
        trail_lat = None
        trail_long = None
    return [trail_name, trail_region, trail_image, trail_lat, trail_long, trail_link]


# --------------- calling functions ---------------


all_pages = makePageList()
for page in all_pages:
    trails = getFromPage(page)
    for trail in trails:
        trail_data = findHikeData(trail)
        print(trail_data[0])
        with open('hikeData.csv', 'a', encoding='UTF8', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(trail_data)




