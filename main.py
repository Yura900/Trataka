from bs4 import BeautifulSoup
from urllib2 import urlopen


url = "https://www.5gcamp.com/"

response = urlopen(url)
soup = BeautifulSoup(response, "html.parser")
elements = soup.find_all("div", {"class": "cont"})

for element in elements:
    subject = element.find("p", {"class": "subject"})
    if subject:
        print(subject.text)