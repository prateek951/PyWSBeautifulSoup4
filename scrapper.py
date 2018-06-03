from urllib.request import urlopen as req

from bs4 import BeautifulSoup as soup


# Scrapping NEWEGG.com graphic cards

WEB_URL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card';


# Open up the connection, grab the HTML content 
WEB_CLIENT = req(WEB_URL)

RAW_HTML = WEB_CLIENT.read()

WEB_CLIENT.close()

PAGE_SOUP = soup(RAW_HTML,"html.parser")


print(PAGE_SOUP.h1)     # <h1 class="page-title-text">Video Cards &amp; Video Devices</h1>

print(PAGE_SOUP.p)  

# <p > Newegg.com - A great place to buy computers, computer parts, electronics, software, 
# accessories, and DVDs online. With great prices, fast shipping, and top-rated customer 
# service - Newegg shopping upgraded ™< /p >
