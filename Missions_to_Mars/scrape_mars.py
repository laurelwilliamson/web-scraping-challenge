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
def scrape_title():
    browser = init_browser()
    news_title = {}
    news_p = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
    
    slide_elem = soup.select_one('ul.item_list li.slide')
    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_p = soup.find("div", class_="article_teaser_body").get_text()

    return news_title, news_p

#PANDAS setup
def scrape_table():
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    html_table = df.to_html()
    html_table.replace('\n', '')
    table = df.to_html('table.html')
    return table

browser = init_browser()
html = browser.html
soup = bs(html, "html.parser")
hemisphere_image_urls = {"title":[], "url":[]}
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
        
        
        hemisphere_image_urls["title"].append(title)
        hemisphere_image_urls["url"].append(img_url)
        
        
        return title, img_url

for result in results:
    scrape_imgs(result)

def scrape():
    init_browser()
    items = {"Title:":[], "Summary:":[], "Table:":[], "Photo:":[]}
    scrape_title()
    scrape_table()
    scrape_imgs(result)
    items["Title:"] = items["Title:"].append(news_title)
    items["Summary:"]= items["Summary:"].append(news_p)
    items["Table:"] = items["Table:"].append(table)
    items["Photo:"] = items["Photo:"].append(hemisphere_image_urls)

    return items



