# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:33:01 2019

@author: Harry Zhenghan Zhang
"""

"""
Exercise to do at home:
Based on the code above, write a short program that creates a dictionary called
 'news'. This dictionary should be structured as follows:
key: title of a news article value: URL of that news article
Your code should extract this information for all news articles on the Stern News 
and Events page and insert it into the dictionary.
Then, write a simple program that prints to the user all titles currently on the 
Stern News and Events page and asks them to indicate which article they want to 
see the URL for (so that they can click on the link and open it in a browser).
Extension/more advanced:
If you want a bigger challenge, notice that at the bottom of the page there are 
links for other pages with additional (older) news articles. They show up in the
familiar format: 1 2 3 ... . Each of these numbers is a link to another page with
another batch of news articles. Try to have your code extract some additional news
articles by having it automatically visit those other pages and also extracting 
news articles from them.
"""
import sys
import requests
import bs4
news = dict()

# This function parses a url into a clickable form
# @param:   url: The original url. May start with "/" or nothing
# @return:  returns the clickable url.   
def urlParse(url):
    if url == None:
        return ""
    if not (url.startswith("http://") or url.startswith("https://")):
        if url.startswith("/"):
            url = "https://www.stern.nyu.edu" + url
        else:
            url = "https://" + url
    return url

# This function gets the 
# @param:   page: The clickable url for the webpage: has to start with "http" or "https"
# @return:  i.string: the title of the news
#           url: the corresponding url
#           hasNextPage: Boolean value indicating whether the next page exists.
#           nextPageUrl: the parsed url of next page. Can be empty string
def getNews(page):
    hasNextPage = True
    r = requests.get(page)
    html = r.text
    soup = bs4.BeautifulSoup(html,'html.parser')
    newsTemp = soup.find_all("h2",class_ = "title")
    for i in newsTemp:
        url =  urlParse(i.a["href"])
        news[i.string] = url        
    temp = soup.find("a", class_ = "pager-next")
    if temp == None:
        hasNextPage = False
    nextPageUrl = urlParse(temp["href"])
    return i.string,url,hasNextPage,nextPageUrl


# This function displays all the news titles, and allows the user to look up urls.
# @param:   none
# @return:  none     
def displayNews():
    cont = True
    index = 0
    indexTitle = dict()
    for i in news.keys():
        index += 1
        print(index,"). ",i)
        indexTitle[str(index)] = i
    while cont == True:
        if index > 0:
            selection = input("Please enter the number of news you want to check: ")
            if selection in indexTitle.keys():
                print(news[indexTitle[selection]])
                cont = False
            else: 
                print("Invalid entry.")


# This function iterates over several pages, gathering all news displayed.
# @param:   maximumPage: upper bound of the pages to check
#           minimumPage: lower bound of pages to check. Default is 1            
# @return:  none              
def iterate(maximumPage,minimumPage = 1):
    if minimumPage >= maximumPage:
        print("Exception: Lower bound must be smaller than upper bound!")
        return
    elif minimumPage < 1:
        print("Exception: Lower bound must be greater or equal to 1!")
        return
    for i in range(minimumPage - 1,maximumPage):
        if i == 0:
            result = getNews("https://www.stern.nyu.edu/experience-stern/news-events")
            hasNextPage = result[2]
            nextUrl = result[3]
        elif i == minimumPage - 1:
            result = getNews("https://www.stern.nyu.edu/experience-stern/news-events?page={number}".format(number = minimumPage))
            hasNextPage = result[2]
            nextUrl = result[3]
        elif hasNextPage:
            result = getNews(nextUrl)
            hasNextPage = result[2]
            nextUrl = result[3]
        else :
            print("This is the last page!")
            
            
            
            
#Main Program            

while True:
    print("------------------------------------")
    print("What do you want to do?")
    print("1).View the first page of Stern News")
    print("2).View selected page of Stern News")
    print("3).View url of Stern News")
    print("4).Clear newsboard")
    print("5).Quit")
    print("-----------------------------")
    command = input("Please make your selection: ")
    if command == '1':
        getNews("https://www.stern.nyu.edu/experience-stern/news-events")
        continue
    
    elif command == '2':
        start = input("Do you want to start from page 1?(Y/N)").upper()
        if start == "Y":
            end = input("Which page do you want to end with?")
            try:
                endNum = int(end)
                iterate(endNum)
            except:
                print("You did not enter a integer number!")
        elif start == "N":
            lower = input("Which page do you want to start with?")
            end = input("Which page do you want to end with?")
            try:
                startNum = int(lower)
                endNum = int(end)
                iterate(endNum,startNum)
            except:
                print("You did not enter a integer number!")
        else:
            print("You need to enter Y or N")
        continue
    
    elif command == '3':
        displayNews()
        news = dict()
        continue
    
    elif command == '4': 
        news = dict()
        
    elif command == '5': 
        sys.exit(1)
    else:
        print("Invalid input!")
        continue