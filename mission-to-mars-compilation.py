#!/usr/bin/env python
# coding: utf-8

# In[84]:


# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser 
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
import pandas as pd
import time


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
doc_container = soup.find('div', class_='list_text')
print(doc_container)


# In[ ]:


doc_title = doc_container.find('div', class_='content_title').text
print(doc_title)


# In[ ]:


doc_body = doc_container.find('div', class_='article_teaser_body').text
print(doc_body)


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)
requests_img = requests.get(url_image)
html = browser.html
soup = bs(html, 'html.parser')
start_carousel = soup.find_all('div', class_='carousel_items')
browser.links.find_by_partial_text('FULL IMAGE').click()
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')
#doc_img = soup.find('div', id='fancybox-lock')
doc_img = soup.select('.fancybox-image')[0]['src']
print(doc_img)


# In[ ]:


mars_img = "https://www.jpl.nasa.gov" + doc_img
print(mars_img)


# In[ ]:


url_facts = "https://space-facts.com/mars/"


# In[ ]:


tables = pd.read_html(url_facts)
tables


# In[ ]:


type(tables)


# In[ ]:


df_0 = tables[0]
df_1 = tables[1]
df_2 = tables[2]


# In[ ]:


html_table_0 = df_0.to_html()
html_table_1 = df_1.to_html()
html_table_2 = df_2.to_html()


# In[ ]:


html_table_0.replace('\n', '')
html_table_1.replace('\n', '')
html_table_2.replace('\n', '')


# In[85]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[88]:


url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemi)
html = browser.html
soup = bs(html, 'html.parser')


# In[89]:


browser.links.find_by_partial_text('Valles').click()
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')
img_hemi_path_va = soup.select('.downloads a')[1]['href']
img_hemi_path_va


# In[90]:


browser.visit(url_hemi)
html = browser.html
soup = bs(html, 'html.parser')
browser.links.find_by_partial_text('Schiaparelli').click()
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')
img_hemi_path_sc = soup.select('.downloads a')[1]['href']
img_hemi_path_sc


# In[91]:


browser.visit(url_hemi)
html = browser.html
soup = bs(html, 'html.parser')
browser.links.find_by_partial_text('Syrtis').click()
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')
img_hemi_path_sy = soup.select('.downloads a')[1]['href']
img_hemi_path_sy


# In[92]:


browser.visit(url_hemi)
html = browser.html
soup = bs(html, 'html.parser')
browser.links.find_by_partial_text('Cerberus').click()
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')
img_hemi_path_ce = soup.select('.downloads a')[1]['href']
img_hemi_path_ce


# In[106]:


hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": img_hemi_path_va}, {"title": "Schiaparelli Hemisphere", "img_url": img_hemi_path_sc}, {"title": "Syrtis Major Hemisphere", "img_url": img_hemi_path_sy}, {"title": "Cerberus Hemisphere", "img_url": img_hemi_path_ce}
print(hemisphere_image_urls)


# In[ ]:




