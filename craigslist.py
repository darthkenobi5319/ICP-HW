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


def recordPrice(items):
    for i in items:
        nearby = i.find("span",class_ = "nearby")
        if nearby == None:
            price = int(i.find("span",class_="result-price").text.strip("$"))
            if price != 0:
                prices.append(price)
            
            
            
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

def setPriceRange(lower,upper):
    newPrice = list()
    for i in prices:
        if i >= lower and i <= upper:
            newPrice.append(i)
    return newPrice

searchString = search()
url = "https://newyork.craigslist.org/search/sss"
search_params = {"query": searchString,
                 "sort": "rel",
                 "srchType":"T"}
prices = []

while url != None:
    items = searchPage(url)[0]
    url = iterate(searchPage(url)[1])
    recordPrice(items)

    
print("To eliminate Outliers, please enter the lower and upper bound:")    
lower = int(input("Lower Bound:"))
upper = int(input("Upper Bound:"))
prices = setPriceRange(lower,upper)
calculateAverage()
displayPrices()
