import requests 
from bs4 import BeautifulSoup

WEB_URL = 'http://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee'

# Reach out to the URL to grab the data
r = requests.get(WEB_URL)

# print(r.content)
# Make the content look beautiful using bs
soup = BeautifulSoup(r.content)
# print(soup)

links = soup.find_all("a")
print(links)
#list of all the links

for link in links:
    print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

g_data = soup.find_all("div",{"class":"info"})
# print(g_data)

for item in g_data:
    print(item.contents[0].find_all("a",{"class":"business-name"})[0].text)
    try:
        print(item.contents[1].find_all("p", {"class": "adr"})[0].text)
    except:
        pass
