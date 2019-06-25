from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


year="2019"
team="TOR"
site="https://www.basketball-reference.com/teams/"+team+"/"+year+"/gamelog/"


res = urlopen(site)
rawpage = res.read().decode("utf-8")
page = rawpage.replace('<!-->', '')
bsObj = BeautifulSoup(page, "html.parser")

table = bsObj.find("table",{"class":"row_summable sortable stats_table now_sortable"}).find_all("tr",{"data-stat":"ranker"})

print (table)