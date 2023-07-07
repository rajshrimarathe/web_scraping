#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"


# In[ ]:


#Headers for request
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language':'en-US, en;q=0.5'})


# In[ ]:


#HTTP Request
webpage = requests.get(URL, headers=HEADERS)


# In[ ]:


type(webpage.content)


# In[ ]:


#Soup object containing all data
soup = BeautifulSoup(webpage.content, 'html.parser')


# In[ ]:


#Fetch links as List of Tag Objects
links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline" target="_blank" href="/sspa/click?ie=UTF8&amp;spc=MTo0NDgwMTczOTcyNzM1Mjc0OjE2ODg3Mzk1NTE6c3BfYXRmOjIwMTI1ODk5OTIwNjk4OjowOjo&amp;url=%2Fuppercase-Professional-Backpack-resistant-sustainable%2Fdp%2FB0BWNBQXDZ%2Fref%3Dsr_1_1_sspa%3Fcrid%3D2M096C61O4MLT%26keywords%3Dbags%26qid%3D1688739551%26sprefix%3Dba%252Caps%252C283%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1"><div class="a-section aok-relative s-image-fixed-height"><img class="s-image" src="https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY218_.jpg" srcset="https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY218_.jpg 1x, https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY327_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY436_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY545_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/61dOp7bn3tL._AC_UY654_FMwebp_QL65_.jpg 3x" alt="Sponsored Ad - uppercase Apex Professional Laptop Backpack (15.6 Inch) 3x more water resistant sustainable bags with rain ..." data-image-index="1" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a>'})


# In[ ]:


link = links[0].get('href')


# In[ ]:


product_list = "https://amazon.com" + link


# In[ ]:


new_webpage = requests.get(product_list, headers=HEADERS)


# In[ ]:


#Soup object containing all data
new_soup = BeautifulSoup(new_webpage.content, 'html.parser')


# In[ ]:


new_soup.find{"span", attrs={"id":'productTitle'}}.text.strip{}


# In[ ]:


new_soup.find{"span", attrs={"class":'edp-feature-declaration'}}

