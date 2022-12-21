import time
import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_news_links_from_rep(url, section, headers):
    list_head_news = [] 

    r = requests.get(url+'/'+section, headers=headers)            
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #recent news
    general_search = soup.find_all('div', class_='CardSectionRight')
    link_tmp = ''
    if len(general_search) > 0:
        for item in list(general_search[0].children):
            content = item.find('div', class_ = 'CardMainContentLeft')
            if content is not None:
                title_tmp = content.find('a').text
                link_tmp = content.find('a')['href']
                
                list_head_news.append({'title':title_tmp, 'link':link_tmp, 'date':None})        
                print('size first list ', len(list_head_news))

    #all list 
    general_search_2 = soup.find_all('div', class_='col-12')
    print(len(general_search_2))
    for content in list(general_search_2[0].find_all('article', class_='PostSection')):
        if content is not None:
            title_tmp = content.find('a').text
            link_tmp = url+'/'+content.find('a')['href']

            date_tmp = content.find('span', class_ = 'PostSectionListSPAN')    
            if date_tmp is not None:    
                date_tmp = date_tmp.text        
            
            list_head_news.append({'title':title_tmp, 'link':link_tmp, 'date':date_tmp})
            print('size first second ', len(list_head_news))          
    #if len(list_head_news) == 0:
    #    print('\n Bing have detected unusual traffic from your computer network, change IP or try later')
    #    enable_to_scrap = False
        
    return list_head_news