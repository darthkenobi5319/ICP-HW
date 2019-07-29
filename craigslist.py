# -*- coding: utf-8 -*-
"""
https://newyork.craigslist.org/

Created on Mon Jul 29 16:34:00 2019

@author: Harry
"""
import bs4
import requests



def search():
    string = input("What do you want to look up?")
    return string


def recordPrice(items,search):
    for i in items:
        nearby = i.find("span",class_ = "nearby")
        title = i.parent.find("a",class_ = "result-title hdrlnk" ).text
        if search.upper() in title.upper(): 
            if nearby == None:
                prices.append(int(i.find("span",class_="result-price").text.strip("$")))
            
            
            
def displayPrices():
    print(prices)
    
    
    
def calculateAverage():
    print(sum(prices)/len(prices))
    
    
def iterate(soup):
    link = soup.find("link",rel="next")
    if link != None:
        nextUrl = link['href']
        return nextUrl
    return None




def searchPage(url):
    r = requests.get(url,search_params)
    if r.status_code != 200:
        print("Page not found!")
    html = r.text
    soup = bs4.BeautifulSoup(html,'html.parser')
    items = soup.find_all("span",class_ = "result-meta")
    return items,soup



searchString = search()
url = "https://newyork.craigslist.org/search/sss"
search_params = {"query": searchString,
                     "sort": "rel"}
prices = []

while url != None:
    items = searchPage(url)[0]
    url = iterate(searchPage(url)[1])
recordPrice(items,searchString)
calculateAverage()
displayPrices()
