#! /usr/bin/env python3
# redditSearch.py - Opens several tabs of reddit search results.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG, format = \
                    '%(asctime)s - %(levelname)s - %(message)s')

print('Searching…') # display text while downloading the reddit page
query = 'https://reddit.com/search/?q=' + ' '.join(sys.argv[1:])
res = requests.get(query)
logging.debug('searching for query %s' % res)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')
logging.debug('retrieving soup')

# Open a browser tab for each result.
linkElems = soup.select('[target="_blank"]')
# selects for css class SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE inside <a> tag
logging.debug('results: %s' % len(linkElems))
numOpen = min(5, len(linkElems)) # the range is either 5 or whatever is smaller
#for i in range(numOpen): # iterates over number of tabs
    #webbrowser.open('https://reddit.com' + linkElems[i].get('href'))
    # opens browser to DDG concatenated with what linkElems in the index i
    # and the attribute for href (which will not contain the domain)
    # remember that linkElems is a list of <a> tags with class r
