import requests
from lxml import html
import csv
import pandas as pd
import csv

year = '2019'
team = 'TOR'

csvFile = open('scrapedData.csv', 'w+', newline='')

r = requests.get('https://www.basketball-reference.com/teams/' + team+ '/' + year + '/gamelog/')
data = html.fromstring(r.text)

length=len(data.xpath("//tbody/tr/td[@data-stat='date_game']/a[@href]/text()"))
date = zip(data.xpath("//tbody/tr/td[@data-stat='date_game']/a[@href]/text()"))
teamPoints = zip(data.xpath("//tbody/tr/td[@data-stat='pts']/text()"))
oppPoints = zip(data.xpath("//tbody/tr/td[@data-stat='opp_pts']/text()"))


newDate=[]
newTeamPts=[]
newOppPts=[]
currentTeam=[]

rowLines=[]

for i in date:
    newDate.append(i)

for i in teamPoints:
    newTeamPts.append(i)

for i in oppPoints:
    newOppPts.append(i)

try:
    writer = csv.writer(csvFile,delimiter=',')
    for i in range(length):
        currentLine=newDate[i]+newTeamPts[i]+newOppPts[i]
        rowLines.append(currentLine)

    writer.writerows(rowLines)


finally:
    csvFile.close()
