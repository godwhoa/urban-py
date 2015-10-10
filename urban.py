#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup

limit = 1
term = sys.argv[1]
if len(sys.argv) > 2:
    limit = sys.argv[2]

r = requests.get('http://www.urbandictionary.com/define.php?term='+term).text
soup = BeautifulSoup(r,"lxml")
count = 0

#Remove links
def replace(element):
    ix= element.parent.contents.index(element)
    for child in reversed(element.contents):
        element.parent.insert(ix, child)
    element.extract()
for link in soup.findAll('a'):
    replace(link)

for m in soup.find_all('div',class_='meaning'):
    #Remove div tags
    tmp = str(m).strip('<div class="meaning">').strip('</div>')
    #Replace break with newline
    m = tmp.replace("<br/>","\n")
    count += 1
    # Blue number to indicate definition number
    print '\033[1;34m'+str(count)+'\033[1;m'
    print m
    if limit != 'all':
        if count == int(limit):
            break

#TODO:
#Remove links  eg. <a href="/define.php?term=digg">digg</a> status: DONE
#Add limit status: DONE