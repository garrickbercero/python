#! /usr/bin/env python3
# comicDownloader.py - checks various webcomics and downloads the latest one if there's a new one.

import requests, bs4, os, datetime

# TODO: Create functions that check each webcomic site

def downloadLHT():
    comicLog = open('comics.txt', 'r')
    downloadedComicsList = comicLog.read().split('\n')
    comicLog.close()
    os.makedirs('./LHT', exist_ok=True)
    res = requests.get('http://www.lefthandedtoons.com')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('.comicimage')
    if comicElem == []:
        print('No image found')
        return
    else:
        comicLink = comicElem[0].get('src')
        comicRes = requests.get(comicLink) # check if http is needed
        comicRes.raise_for_status()
        comicImg = open(os.path.join('LHT', os.path.basename(comicLink)), 'wb')
        if os.path.basename(comicLink) in downloadedComicsList:
            print('No new LHT comic')
            return
        else:
            print('New LHT found')
            newComic = open('comics.txt', 'a')
            newComic.write(str(os.path.basename(comicLink)) + '\n')
            newComic.close()
            for chunk in comicRes.iter_content(100000):
                comicImg.write(chunk)
            comicImg.close()
            return os.path.basename(comicLink)

def downloadSavageChickens():
    comicLog = open('comics.txt', 'r')
    downloadedComicsList = comicLog.read().split('\n')
    comicLog.close()
    os.makedirs('./SavageChickens', exist_ok=True)
    res = requests.get('https://www.savagechickens.com/category/cartoons')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('.entry_content img')
    if comicElem == []:
        print('No image found')
        return
    else:
        comicLink = comicElem[0].get('src')
        comicRes = requests.get(comicLink) # check if http is needed
        comicRes.raise_for_status()
        comicImg = open(os.path.join('LHT', os.path.basename(comicLink)), 'wb')
        if os.path.basename(comicLink) in downloadedComicsList:
            print('No new Savage Chickens')
            return
        else:
            print('New Savage Chickens found')
            newComic = open('comics.txt', 'a')
            newComic.write(str(os.path.basename(comicLink)) + '\n')
            newComic.close()
            for chunk in comicRes.iter_content(100000):
                comicImg.write(chunk)
            comicImg.close()
            return os.path.basename(comicLink)    
        
# TODO: Download new webcomics
downloadLHT()
downloadSavageChickens()

