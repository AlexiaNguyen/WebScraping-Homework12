from bs4 import BeautifulSoup 
import os
import requests
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def mars_all():
    browser = init_browser()
    mars_data = {}

url = 'https://mars.nasa.gov/news/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('div', class_="content_title").text
print(title)

paragraph = soup.find('div', class_="rollover_description").text
print(paragraph)





url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

image = soup.find('img', class_='thumb')['src']

image_url = "https://jpl.nasa.gov" + image
print(image_url)

url = 'https://twitter.com/marswxreport?lang=en'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

result3 = soup.find('div', class_="js-tweet-text-container")

weather = result3.find('p').text

print(weather)



url = 'https://space-facts.com/mars/'

facts = pd.read_html(url)
facts

df = facts[0]
df.columns = ['Info', 'Data']
df.head()

html_facts = df.to_html()
html_facts

df.to_html('html_facts.html')




executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
hemisphere=[]

links = soup.find_all('div', class_='item')
for link in links:
    url1 = link.find('a')['href']
    url2 = 'https://astrogeology.usgs.gov'+ url1
    browser.visit(url2)
    html1 = browser.html
    soup1 = BeautifulSoup(html1, 'html.parser')
    downloads = soup1.find('div', class_='downloads')
    image_url = downloads.find('a')['href']
    image_title = soup1.find('h2', class_="title").text
    dictionary={'title':image_title,'image_url':image_url}
    hemisphere.append(dictionary)
    browser.back()
   
print(hemisphere)
