from gamesim import *
import pandas as pd
import csv
import numpy as np
import statistics as st
import random as rnd

points=[]
opp_points=[]

with open('scrapedData.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        points.append(int(line[2]))
        opp_points.append(int(line[3]))

test=Teams(points,opp_points)
mean=test.pointsMean(points)
oppMean=test.oppPtsMean(opp_points)
std=test.pointsStd(points)
oppstd=test.oppPtsStd(opp_points)

print(mean)
print(oppMean)
print(std)
print(oppstd)