from gamesim import *
import pandas as pd
import csv
import numpy as np
import statistics as st
import random as rnd

points=[]
opp_points=[]

with open('scrapedData.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        points.append(int(line[2]))
        opp_points.append(int(line[3]))

    #plt.hist(points)
    #plt.show()
    #print(st.mean(points))
    #print(st.stdev(points))

    #plt.hist(opp_points)
    #plt.show()
    #print(st.mean(opp_points))
    #print(st.stdev(opp_points))

    print(rnd.gauss(st.mean(points),st.stdev(points)))