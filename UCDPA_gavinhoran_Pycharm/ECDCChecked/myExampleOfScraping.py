# This is my example of scraping a webpage. I have used re to create a regular expression which pulls out the .csv file
# from the html. I used pandas to create the .csv file which this program produces. urllib.request was pointed at the
# webpage, and I used a function I had already created myself to name the file containing the csv.
#
# Basically, it sucks in the html from the ecdc page; turns this into http.client.HTTPResponse type html_page
# BeautifulSoup then does it's thing and parses html_page with lxml, or the other way around;I dunno; it's not hugely
# important here.
# The soup.findall pulls all html links out of this;
# These then go into the links list. I used a list because it was easy to run over all the values, the order didn't
# matter to me at all in this case, I wanted to run through all the values.
# One thing I didn't like about the list was that it can have a variety of types and not have a problem with this.
# Well, I did have a problem because I can't run a regex on ints and floats. I think. Anyways, I converted all entries
# in links to strings, and then ran a regex to find those ending in .csv. I knew there would be at least one. There may
# be more in future; that is the joy of this, I can run this program again to find or indeed "scrape" as many .csv
# files as  a page holds.
# Next I converted the list to a dataframe, because I find it easier to manipulate these.
# I then used a function I had already written to push this out to a .csv file. This includes the date and time
# appended at the end using a function which I prepared already.

import pandas as pd
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from UCDPA_gavinhoran_Pycharm.functionFile import csv_time_namer

req = Request("https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

links = str(links)

pattern = r'[A-Z0-9:/._-]+\.csv'
regex = re.compile(pattern,flags=re.IGNORECASE)
csvlink = regex.findall(links)

csvToDownload = pd.DataFrame (csvlink, columns = ['targetCSV'])
#this produces a small but beautiful dataframe, containing my target for the next program!
csvToDownload.to_csv(csv_time_namer('targetsForAnalysis'))