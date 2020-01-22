import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip() # takes text in HTML element and strips whitespace


price = getAmazonPrice('https://www.amazon.com/Al-Sweigart/e/B007716TEG?ref_=dbs_p_pbk_r00_abau_000000')
print('The Price is ' + price)
