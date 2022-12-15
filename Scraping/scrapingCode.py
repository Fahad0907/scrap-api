from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from requests_html import HTMLSession
import json
import re

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def Scrap(product_item : str):
    url= [
        'https://www.foodpanda.com.bd/darkstore/w2lx/pandamart-gulshan-w2lx',
        'https://www.foodpanda.com.bd/darkstore/h9jp/pandamart-mirpur'
        ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
    }
    list = []
    for itr in range(len(url)):
        source=requests.get(url[itr], headers=headers).text
        soup = BeautifulSoup(source,'lxml')
        script_data = soup.find_all('script')[5].text
        index = script_data.index(';window.__PROVIDER_PROPS__=')
        script_data = script_data[27:index]
        script_data_json = json.loads(script_data)
        res = script_data_json['swimlanes']['shopDetailsSwimlanes']
        
        for i in res:
            dic = dict()
            if 'products' in i:
                product = i['products']
                
                for j in product:
                   
                    if findWholeWord( product_item.lower())(j['name'].lower()):
                        if itr == 0:
                            dic['darkStore'] = "Gulshan"
                        else:
                            dic['darkStore'] = "Mirpur"
                        dic['title'] = j['name']
                        dic['url'] = url[itr]+ "/product/" + j['id']  
                        if j['price'] == j['originalPrice']:
                            dic['price'] = j['price']
                            dic['priceAfterDiscount'] = None
                        else:
                            dic['price'] =  j['originalPrice']
                            dic['priceAfterDiscount'] = j['price']
                        if j['stockAmount']:
                            dic['stockStatus'] = 'IN STOCK'
                        else:
                            dic['stockStatus'] = 'OUT OF STOCK'
                        list.append(dic)
    return list
            
            




