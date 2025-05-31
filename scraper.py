import requests
from bs4 import BeautifulSoup

url = "https://ypdcrime.com/penal.law/article155.php"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# Example: print all statute titles on the page
for tag in soup.select("h3"):
    print(tag.text.strip())