import requests
from bs4 import BeautifulSoup
import re 
import json



# r'((?:[0-9]{1,5}\.){3}[0-9]{1,3}(?::[0-9]{2,5})?)'
#    00000.00000.00000.  000        : 00000
#      a	 b	   c	  d				p
# 										80
#    									443

# url = "https://httpbin.org"
# url = "https://www.kinopoisk.ru/"
url = "https://2ip.ua/ru"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
list_port = ['80','443']

for p in list_port:
	for a in range(1,10000):
		for b in range(1,10000):
			for c in range(1,10000):
				for d in range(1,1000):
					IP_proxy = str(a) + '.' + str(b)  + '.' + str(c)  + '.'  + str(d)  + ':' + p
					print(IP_proxy)

					http_proxy = "http://" + IP_proxy
					https_proxy = "https://" + IP_proxy 
					try:
						proxies = {"http": http_proxy,
						"https":https_proxy}
						response = requests.get(url,headers=headers,proxies=proxies,timeout=0.01)
						response.encoding = 'utf-8'	
						print(response.status_code)

					except Exception as err:
						pass
						# print(err)
