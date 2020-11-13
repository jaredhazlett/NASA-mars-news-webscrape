
from bs4 import BeautifulSoup as bs
from splinter import Browser 
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
import pandas as pd
import time


def init_browser():
	executable_path = {'executable_path': '/Applications/chromedriver_2'}
	return Browser('chrome', **executable_path, headless=False)


# In[3]:

def scrape_web():
	browser = init_browser()

	url = "https://mars.nasa.gov/news/"
	browser.visit(url)
	html = browser.html
	soup = bs(html, 'html.parser')
	time.sleep(2)
	doc_container = soup.find('div', class_='list_text')
	print(doc_container)


# In[4]:


	doc_title = doc_container.find('div', class_='content_title').text
	print(doc_title)


# In[5]:

	doc_body = doc_container.find('div', class_='article_teaser_body').text
	print(doc_body)


# In[6]:


	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless=False)


# In[7]:


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


# In[8]:


	mars_img = "https://www.jpl.nasa.gov" + doc_img
	print(mars_img)


# In[9]:


	url_facts = "https://space-facts.com/mars/"


# In[10]:


	tables = pd.read_html(url_facts)
	tables


# In[11]:


	type(tables)


# In[12]:


	df_0 = tables[0]
	df_1 = tables[1]
	df_2 = tables[2]


# In[13]:


	html_table_0 = df_0.to_html()
	html_table_1 = df_1.to_html()
	html_table_2 = df_2.to_html()


# In[14]:


	html_table_0.replace('\n', '')
	html_table_1.replace('\n', '')
	html_table_2.replace('\n', '')


# In[15]:


	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


	url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(url_hemi)
	html = browser.html
	soup = bs(html, 'html.parser')


# In[17]:


	browser.links.find_by_partial_text('Valles').click()
	time.sleep(1)
	html = browser.html
	soup = bs(html, 'html.parser')
	img_hemi_path_va = soup.select('.downloads a')[1]['href']
	img_hemi_path_va


# In[18]:


	browser.visit(url_hemi)
	html = browser.html
	soup = bs(html, 'html.parser')
	browser.links.find_by_partial_text('Schiaparelli').click()
	time.sleep(1)
	html = browser.html
	soup = bs(html, 'html.parser')
	img_hemi_path_sc = soup.select('.downloads a')[1]['href']
	img_hemi_path_sc


# In[19]:


	browser.visit(url_hemi)
	html = browser.html
	soup = bs(html, 'html.parser')
	browser.links.find_by_partial_text('Syrtis').click()
	time.sleep(1)
	html = browser.html
	soup = bs(html, 'html.parser')
	img_hemi_path_sy = soup.select('.downloads a')[1]['href']
	img_hemi_path_sy


# In[20]:


	browser.visit(url_hemi)
	html = browser.html
	soup = bs(html, 'html.parser')
	browser.links.find_by_partial_text('Cerberus').click()
	time.sleep(1)
	html = browser.html
	soup = bs(html, 'html.parser')
	img_hemi_path_ce = soup.select('.downloads a')[1]['href']
	img_hemi_path_ce


# In[21]:


	hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": img_hemi_path_va}, {"title": "Schiaparelli Hemisphere", "img_url": img_hemi_path_sc}, {"title": "Syrtis Major Hemisphere", "img_url": img_hemi_path_sy}, {"title": "Cerberus Hemisphere", "img_url": img_hemi_path_ce}
	print(hemisphere_image_urls)


	browser.quit()
	return hemisphere_image_urls
# In[ ]:




