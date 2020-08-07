import requests
from bs4 import BeautifulSoup
import re 
import json
import time
import os

import multiprocessing
import itertools
import threading
import logging



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

timeStart = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
# print('\nStart at  ' + timeStart)

list_WorkProxy = []

def IP_Generator():
	for p in list_port:
		for a in range(1,10000):
			for b in range(1,10000):
				for c in range(1,10000):
					for d in range(1,1000):
						IP_proxy = str(a) + '.' + str(b)  + '.' + str(c)  + '.'  + str(d)  + ':' + p
						# print(number,IP_proxy,sep='. ')
						# print('{0}. process id: {1}   {2}'.format(number,proc,IP_proxy))

						yield IP_proxy

						# http_proxy = "http://" + IP_proxy
						# https_proxy = "https://" + IP_proxy 
						# try:
						# 	proxies = {"http": http_proxy,
						# 	"https":https_proxy}
						# 	response = requests.get(url,headers=headers,proxies=proxies,timeout=0.01)
						# 	response.encoding = 'utf-8'	
						# 	print(response.status_code)

						# except Exception as err:
						# 	pass
						# 	# print(err)


def make_all(IP_proxy):
	http_proxy = "http://" + IP_proxy
	https_proxy = "https://" + IP_proxy 
	print(IP_proxy)
	try:
		proxies = {"http": http_proxy,
		"https":https_proxy}
		response = requests.get(url,headers=headers,proxies=proxies,timeout=0.01)
		response.encoding = 'utf-8'	
		list_WorkProxy.append(IP_proxy)
		print(response.status_code)

	except Exception as err:
		pass
		# print(err)
	return list_WorkProxy

def main():
	timeStart = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
	print('Start at  ' + timeStart)
	for x in range(0,2):
		print('***************************	' + str(x) + '	************************************')
		ip_generator = IP_Generator()
		with multiprocessing.Pool(50) as pool:
			pool.map(make_all,list(itertools.islice(ip_generator,10**6*x,10**6*(x+1))))

		print('Найденные прокси:')
		print(list_WorkProxy)





if __name__ == '__main__':
	main()
