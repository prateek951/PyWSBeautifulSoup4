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

IMAGE_CONTAINERS = PAGE_SOUP.findAll("div",{"class":"item-container"})
print(len(IMAGE_CONTAINERS))


for container in IMAGE_CONTAINERS:
    GRAPHIC_CARD_BRAND  = container.div.div.a.img['title']
    TITLE_CONTAINER = container.findAll("a",{"class":"item-title"})
    PRODUCT_NAME = TITLE_CONTAINER[0].text
    SHIPPING_CONTAINER = container.findAll("li",{"class":"price-ship"})
    SHIPPING_PRICING = SHIPPING_CONTAINER[0].text
    print(SHIPPING_PRICING)