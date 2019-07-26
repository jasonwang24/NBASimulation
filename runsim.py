from gamesim import *
from webscrape import *
import pandas as pd
import csv
import numpy as np
import statistics as st
import random as rnd
import matplotlib.pyplot as plt

points = []
opp_points = []

#open csv file to prepare for scraping
def dataCalc(statsYear, currentTeam):
    scrape = Webscraper(statsYear, currentTeam)
    scrape.scraping(statsYear, currentTeam)

    with open('scrapedData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            points.append(int(line[2]))
            opp_points.append(int(line[3]))

#calculate team's points
def mean():
    team = Teams(points, opp_points)
    return team.pointsMean(points)

#calculate opponent team's points
def opp_mean():
    team = Teams(points, opp_points)
    return team.oppPtsMean(opp_points)

#calculate team's point standard deviation
def std():
    team = Teams(points, opp_points)
    return team.pointsStd(points)

#calculate opponent team's point standard deviation
def opp_std():
    team = Teams(points, opp_points)
    return team.oppPtsStd(opp_points)


def pointsList():
    return points


statsYear = '2019'
currentTeam = 'TOR'
dataCalc(statsYear, currentTeam)
TORMean = mean()
TOROppMean = opp_mean()
TORStd = std()
TOROppStd = opp_std()

currentTeam = 'GSW'
dataCalc(statsYear, currentTeam)
GSWMean = mean()
GSWOppMean = opp_mean()
GSWStd = std()
GSWOppStd = opp_std()

count = 0
rapwins = 0
gswwins = 0

rapsFour = 0
rapsFive = 0
rapsSix = 0
rapsSeven = 0
gswFour = 0
gswFive = 0
gswSix = 0
gswSeven = 0

#run series simulation 1000 times
while (count != 1000):

    teamOneScore = 0
    teamTwoScore = 0
    gamecount = 0

    #for each 7 game series played, simulate scores and outcome
    while teamOneScore != 4 and teamTwoScore != 4 and gamecount != 7:
        teamOne = (rnd.gauss(TORMean, TORStd) + rnd.gauss(GSWOppMean, GSWOppStd)) / 2
        teamTwo = (rnd.gauss(GSWMean, GSWStd) + rnd.gauss(TOROppMean, TOROppStd)) / 2

        if teamOne != teamTwo:
            gamecount = gamecount + 1

        if int(round(teamOne)) > int(round(teamTwo)):
            teamOneScore = teamOneScore + 1
        elif int(round(teamOne)) < int(round(teamTwo)):
            teamTwoScore = teamTwoScore + 1

        print(str(gamecount) + ": ")
        print(int(round(teamOne)))
        print(int(round(teamTwo)))

    print(teamOneScore)
    print(teamTwoScore)

    combinedScore = teamOneScore + teamTwoScore

    if teamOneScore > teamTwoScore:
        if (combinedScore == 4):
            rapsFour += 1
        elif (combinedScore == 5):
            rapsFive += 1
        elif (combinedScore == 6):
            rapsSix += 1
        else:
            rapsSeven += 1
    else:
        if (combinedScore == 4):
            gswFour += 1
        elif (combinedScore == 5):
            gswFive += 1
        elif (combinedScore == 6):
            gswSix += 1
        else:
            gswSeven += 1

    count = count + 1


#display results of simulation
print(" ")
print("Raptors in 4: "+str(rapsFour/1000))
print("Raptors in 5: "+str(rapsFive/1000))
print("Raptors in 6: "+str(rapsSix/1000))
print("Raptors in 7: "+str(rapsSeven/1000))
print("Warriors in 4: "+str(gswFour/1000))
print("Warriors in 5: "+str(gswFive/1000))
print("Warriors in 6: "+str(gswSix/1000))
print("Warriors in 7: "+str(gswSeven/1000))
