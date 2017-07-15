import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.google.co.in/search?q=%22jagga+jasoos%22&oq=%22jagga+jasoos%22&aqs=chrome..69i57j0l5.293j0j9&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(page.content)
import re
links = soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print re.split(":(?=http)",link["href"].replace("/url?q=",""))