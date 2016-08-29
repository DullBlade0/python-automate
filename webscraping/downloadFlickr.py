import requests, os, bs4

url = 'http://flickr.com'
os.makedirs('flickr', exist_ok=True)
for link in soup.find_all('.yui_3_16_0_1_1462999947596_16802'):