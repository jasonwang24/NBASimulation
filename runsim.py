from gamesim import *
from webscrape import *
import pandas as pd
import csv
import numpy as np
import statistics as st
import random as rnd
import matplotlib.pyplot as plt


points=[]
opp_points=[]

def dataCalc(statsYear,currentTeam):

    scrape=Webscraper(statsYear,currentTeam)
    scrape.scraping(statsYear,currentTeam)

    with open('scrapedData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            points.append(int(line[2]))
            opp_points.append(int(line[3]))

def mean():
    team=Teams(points,opp_points)
    return team.pointsMean(points)

def opp_mean():
    team=Teams(points,opp_points)
    return team.oppPtsMean(opp_points)

def std():
    team=Teams(points,opp_points)
    return team.pointsStd(points)

def opp_std():
    team=Teams(points,opp_points)
    return team.oppPtsStd(opp_points)

def pointsList():
    return points


statsYear='2019'
currentTeam='TOR'
dataCalc(statsYear,currentTeam)
TORMean=mean()
TOROppMean=opp_mean()
TORStd=std()
TOROppStd=opp_std()

'''
print(TORMean)
print(TOROppMean)
print(TORStd)
print(TOROppStd)
print(TORPts)
'''

currentTeam='GSW'
dataCalc(statsYear,currentTeam)
GSWMean=mean()
GSWOppMean=opp_mean()
GSWStd=std()
GSWOppStd=opp_std()

'''
print(GSWMean)
print(GSWOppMean)
print(GSWStd)
print(GSWOppStd)
print(GSWPts)
'''

teamOneScore=0
teamTwoScore=0
gamecount=0

while teamOneScore!=4 and teamTwoScore!=4 and gamecount<7:
    gamecount=gamecount+1
    teamOne=(rnd.gauss(TORMean,TORStd)+rnd.gauss(GSWOppMean,GSWOppStd))/2
    teamTwo=(rnd.gauss(GSWMean,GSWStd)+rnd.gauss(TOROppMean,TOROppStd))/2

    if int(round(teamOne))>int(round(teamTwo)):
        teamOneScore=teamOneScore+1
    elif int(round(teamOne))<int(round(teamTwo)):
        teamTwoScore=teamOneScore+1

    print (str(gamecount)+": ")
    print (int(round(teamOne)))
    print (int(round(teamTwo)))


print(teamOneScore)
print(teamTwoScore)