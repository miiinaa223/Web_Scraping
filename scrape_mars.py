import pandas as pd
from sqlalchemy import create_engine
from splinter import Browser
from bs4 import BeautifulSoup

#1 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('div', class_='content_title').find('a').text
text = soup.find('div', class_='article_teaser_body').text
print(f'the latest title ="'+title+'"')
print(f'the paragrath = "'+text+'"')

#2
url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_image)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
featured_image_url = soup.find('div', class_='img').find('img')['src']
print(f'featured_image_url = https://www.jpl.nasa.gov'+featured_image_url)


#3
url_twitter = 'https://twitter.com/marswxreport?lang=en&lang=en'
browser.visit(url_twitter)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_weather = soup.find('div', class_='js-tweet-text-container').find('p').text
print(f'mars_weather = '+mars_weather)


#4
url_facts = "https://space-facts.com/mars/"

table = pd.read_html(url_facts)
table_pd = table[0]

table_pd.columns = ['Parameter','Values']
table_pd


#5
url_hemis = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url_hemis)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
Mars_list = []
# for x in range(50):
    # HTML object
html = browser.html
    # Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
articles = soup.find_all('div', class_='item')

    # Iterate through each book
for article in articles:
    Mars_dict = {}
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
    title = article.find('h3').text
    link = article.find('a')
    href = link['href']
    print(f'"title": '+title+",")
    print(f'"image_url :" https://astrogeology.usgs.gov' + href)
    Mars_list.append(Mars_dict)
    
    
    
