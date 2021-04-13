import requests 
import time
from bs4 import BeautifulSoup


#headers = {'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}


text = 'inurl:"/lib/editor/atto/plugins/managefiles/" | inurl:"calendar/view.php?view=month"'
url = 'https://www.google.com/search?q=' + text
headers = {'User-Agent': 'Mozilla/5.0'}



r = requests.get(url, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())