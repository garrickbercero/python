#! /usr/bin/env python3
# umbrellaReminder.py - scrapes weather.gov to check if you should bring an umbrella today

import requests, bs4, smtplib

site = 'https://weather.com/en-PH/weather/today/l/RPXX0017:1:RP'

res = requests.get(site)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('.today-daypart-precip')
print('Today\'s precipitation index is ' + elems[0].text)

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('gbercero@gmail.com', 'dbpkoxncrqsaiqfi')

if elems[0].text > '30%':
    body = 'Subject: It\'s probably going to rain\nYou should bring an umbrella today.'
    conn.sendmail('gbercero@gmail.com','gbercero@yahoo.com', body)
    print(body)

