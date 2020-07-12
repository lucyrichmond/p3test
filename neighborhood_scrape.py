import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.chicagomag.com/Chicago-Magazine/Neighborhood-Guides/'
response = requests.get(url)

