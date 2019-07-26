import requests
from lxml import html
import csv
import csv


class Webscraper:

    def __init__(self,year,team):
        Webscraper.year=year
        Webscraper.team=team
        self.scraping(Webscraper.year,Webscraper.team)

    #scrapes NBA team stats data from a site and stores values in a csv file
    def scraping(self,year,team):
        csvFile = open('scrapedData.csv', 'w+', newline='')

        r = requests.get('https://www.basketball-reference.com/teams/' + team+ '/' + year + '/gamelog/')
        data = html.fromstring(r.text)

        #searching for specific data
        length=len(data.xpath("//tbody/tr/td[@data-stat='date_game']/a[@href]/text()"))
        date = zip(data.xpath("//tbody/tr/td[@data-stat='date_game']/a[@href]/text()"))
        teamPoints = zip(data.xpath("//tbody/tr/td[@data-stat='pts']/text()"))
        oppPoints = zip(data.xpath("//tbody/tr/td[@data-stat='opp_pts']/text()"))

        #create arrays to prepare for writing into csv
        newDate=[]
        newTeamPts=[]
        newOppPts=[]
        currentTeam=[]
        rowLines=[]
        tempTeam=[]

        for i in range(length):
            tempTeam.append(team)

        temp=zip(tempTeam)
        newTeam=[]

        for i in temp:
            newTeam.append(i)

        for i in date:
            newDate.append(i)

        for i in teamPoints:
            newTeamPts.append(i)

        for i in oppPoints:
            newOppPts.append(i)

        #write stored data into file
        try:
            writer = csv.writer(csvFile,delimiter=',')
            for i in range(length):
                currentLine=newTeam[i]+newDate[i]+newTeamPts[i]+newOppPts[i]
                rowLines.append(currentLine)

            writer.writerows(rowLines)

        finally:
            csvFile.close()


