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
    print("slide_elem", slide_elem)
    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_p = soup.find("div", class_="article_teaser_body").get_text()

    return news_title, news_p
    

#PANDAS setup
def scrape_table():
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df=df.rename(columns={0:'',1:'Mars'})
    table = df.to_html(index=False,classes='table table-striped', justify='left')  
    return table




# html = browser.html
# soup = bs(html, "html.parser")
# def scrape_imgs():
# browser = init_browser()
# pic_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
# titles = []
# photo_info = []
# results = soup.find_all('div', class_='item')
# for result in results:
#     title = result.find("h3").text
#     titles.append(title)

# for title in titles:

#     browser.links.find_by_partial_text(title).click()
#     next_html = browser.html
#     soup = BeautifulSoup(next_html, 'html.parser')
#     pic = soup.find_all('div', class_='downloads')[0].li.a['href']
#     half = soup.find('h2', class_='title').text
#     photo_info.append({'title':half, 'img_url':pic})
#     browser.visit(pic_url)
# mars_dictionary = {'featured': featured,'mars_facts':mars_html2, 'mars_images':image_info}   

# def scrape_imgs(result):
    
#     contained = result.find("div", class_='collapsible results')
#     contents = result.find("div", class_='item')
#     img_url = result.img['src']
#     header = result.find("h3")
#     title = header.get_text() 
#     header.click()
#     #supposed to have something here?
#     return title, img_url

# for result in results:
#     scrape_imgs(result)

def scrape():
    init_browser()
    # title =  img_url = ""
    # items = {"Title": "", "Summary":[], "Table":[], "Photo":[], "Desc":[]}
    news_title, news_p = scrape_title()
    table = scrape_table()
    # photo_info = scrape_imgs()

    html = browser.html
    soup = bs(html, "html.parser")
# def scrape_imgs():
# browser = init_browser()
# pic_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    pic_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    titles = []
    photo_info = []
    results = soup.find_all('div', class_='item')
    for result in results:
        title = result.find("h3").text
        titles.append(title)

    for title in titles:

        browser.links.find_by_partial_text(title).click()
        next_html = browser.html
        soup = BeautifulSoup(next_html, 'html.parser')
        pic = soup.find_all('div', class_='downloads')[0].li.a['href']
        half = soup.find('h2', class_='title').text
        photo_info.append({'title':half, 'img_url':pic})
        browser.visit(pic_url)
    # url = "https://space-facts.com/mars/"
    # tables = pd.read_html(url)
    # df = tables[0]
    # html_table = df.to_html()
    # html_table.replace('\n', '')
    # table = df.to_html('table.html')


    # hemisphere_image_urls = []
    # browser = init_browser()
    # title = {}
    # img_url = {}

    # url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # browser.visit(url)

    # html = browser.html
    # soup = bs(html, "html.parser")
    # results = soup.find_all('div', class_='item')
    # for result in results:
    #     title, img_url = scrape_imgs(result)
    #     hemisphere_image_urls.append({
    #         "title": title, "img_url": img_url
    #     })

    # items["Title"].append(news_title)
    # items["Summary"].append(news_p)
    # items["Table"].append(table)
    # items["Photo"].append(img_url)
    # items["Desc"].append(title)

    items = {
        "Title": news_title,
        "Summary": news_p,
        "Table": table,
        "URL": photo_info[title],
        "Title": photo_info[img_url]
    }

    return items



