import requests 
from bs4 import BeautifulSoup

WEB_URL = 'https://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee'

# Reach out to the URL to grab the data
r = requests.get(WEB_URL)

# print(r.content)
# Make the content look beautiful using bs
soup = BeautifulSoup(r.content)
# print(soup)

links = soup.find_all("a")
print(links)

for link in links:
    print("<a href='%s'>%s</a>" %(link.get("href"),link.text))