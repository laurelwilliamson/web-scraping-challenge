#Imports
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import os
import pandas as pd
import pymongo
#Chromedriver Seup
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/laurelwilliamson/Downloads/chromedriver 2"}
    return Browser("chrome", **executable_path, headless=True)
#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# def scrape():
#     browser = init_browser()
#     news_title = {}
#     news_p = {}

#     url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
#     browser.visit(url)

#     html = browser.html
#     soup = bs(html, "html.parser")
    
#     slide_elem = soup.select_one('ul.item_list li.slide')
#     news_title = slide_elem.find("div", class_='content_title').get_text()
#     news_p = soup.find("div", class_="article_teaser_body").get_text()

#     return news_title, news_p
# #PANDAS setup
# url = "https://space-facts.com/mars/"
# tables = pd.read_html(url)
# df = tables[0]
# html_table = df.to_html()
# html_table.replace('\n', '')
# df.to_html('table.html')

# hemisphere_image_urls = {"photo":[]}
# results = soup.find_all('div', class_='item')

# def scrape_imgs(result):
#         browser = init_browser()
#         title = {}
#         img_url = {}
    
#         url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#         browser.visit(url)

#         html = browser.html
#         soup = bs(html, "html.parser")
    
#         contained = result.find("div", class_='collapsible results')
#         contents = result.find("div", class_='item')
#         img_url = result.img['src']
#         title = result.find("h3").get_text()
#         print("Title: ",title)
        
#         photo_info = title, img_url
        

#         hemisphere_image_urls["photo"].append(photo_info)
        
#         return title, img_url
# c = 0

# for result in results:
#     c +=1
#     scrape_imgs(result)

def scrape():

    # This part of the function will scrape the title and description from the website
    browser = init_browser()
    news_title = {}
    news_p = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
    
    slide_elem = soup.select_one('ul.item_list li.slide')
    news_title = soup.find("div", class_='content_title').get_text()
    news_p = soup.find("div", class_="article_teaser_body").get_text()
    


    #  This part of the function will create a table using the scraped data

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    html_table = df.to_html()
    html_table.replace('\n', '')
    table = df.to_html('table.html')

    #print("table: ", table)
    

    #  This part of the funciton will 

    hemisphere_image_urls = {"photo":[]}
    results = soup.find_all('div', class_='item')
    

    def scrape_imgs(result):
        browser = init_browser()
        title = {}
        img_url = {}

        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)

        html = browser.html
        soup = bs(html, "html.parser")

        contained = result.find("div", class_='collapsible results')
        contents = result.find("div", class_='item')
        img_url = result.img['src']
        title = result.find("h3").get_text()
        
        photo_info = title, img_url
        

        hemisphere_image_urls["photo"].append(photo_info)
        
        return title, img_url

    for result in results:
        scrape_imgs(result)


    return news_title, news_p, table, hemisphere_image_urls

print(scrape())


