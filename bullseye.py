#!/usr/bin/python

from googlesearch import search
from bs4 import BeautifulSoup
import urllib.request
import sys
import re
from fake_useragent import UserAgent
from socket import timeout
from urllib.error import HTTPError, URLError


ua = UserAgent()


print('''
   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ 
 ( B | U | L | L | S | E | Y | E )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  
 EMAIL EXTRACTOR - Author Naved Anjum
''')  


def menu():
	try:
		print(" Enter URL to Search " )
  
		print("")
		print ("Example URL: http://www.google.com")
		url = str(input("Enter URL: "))
		print("")
		extractEmail(url)
		input("Press enter key to continue")
		menu()
        
	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print (e)
		input("Press enter to continue")
		menu()
  
		
def extractEmail(url):
	try:
		print ("Searching emails... please wait")
		print("")

		count = 0
		listUrl = []

		req = urllib.request.Request(
    			url, 
    			data=None, 
    			headers={
        		'User-Agent': ua.random
    		})

		try:
			conn = urllib.request.urlopen(req, timeout=10)

		except timeout:
			raise ValueError('Timeout ERROR')

		except (HTTPError, URLError):
			raise ValueError('Bad Url...')

		status = conn.getcode()
		contentType = conn.info().get_content_type()

		if(status != 200 or contentType == "audio/mpeg"):
    			raise ValueError('Bad Url...')


		html = conn.read().decode('utf-8')

		emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)

		for email in emails:
			if (email not in listUrl):
				count += 1
				print(email)
				listUrl.append(email)
				
		print("")
		print("***********************")
		print( count,"emails were found")
		print("***********************")



	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print (e)
		input("Press enter to continue")
		menu()

def exit1():
    sys.exit(0)	
    
menu()