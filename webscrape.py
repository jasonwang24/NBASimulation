from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year="2019"
team="TOR"
url="https://stats.nba.com/teams/traditional/?sort=GP&dir=-1"
html =urlopen(url)
bsObj = BeautifulSoup(html,"lxml")

new = bsObj.find_all("div",{"class":"nba-stat-table__overflow"})

print(new)

