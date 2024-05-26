import requests
from bs4 import BeautifulSoup
import re

CLEANR = re.compile('<.*?>')

def cleanhtml(raw_html):
    if raw_html is None:
        return ''
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

websiteToScrape = "https://www.ufc.com/news/prelim-results-highlights-winner-interviews-ufc-301-pantoja-vs-erceg"
response = requests.get(websiteToScrape)
soup = BeautifulSoup(response.content, "html.parser")

fight_result_sections = soup.find_all('div', class_='clearfix text-formatted field field--name-text field--type-text-long field--label-hidden field__item')

for section in fight_result_sections:
    result = section.find('h3')
    if result:
        cleanResult = cleanhtml(result.text)
        print(cleanResult)