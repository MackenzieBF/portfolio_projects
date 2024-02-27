from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

## My WEB API KEY: EFACCC9A917875228BE4E3A180D6F952

response = requests.get('https://steamdb.info/')
soup = BeautifulSoup(response.content, 'xml')
for element in soup.select('img[src]'):
    print(element)