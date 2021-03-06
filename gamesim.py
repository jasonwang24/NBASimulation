import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics as st
import random as rnd

class Teams:

    def __init__(self,points={},opp_points={}):
        Teams.points=points
        Teams.opp_points=opp_points

        self.pointsMean(points)
        self.oppPtsMean(opp_points)
        self.pointsStd(points)
        self.oppPtsStd(opp_points)


    #calculate mean of team's points
    def pointsMean(self,points):
        return st.mean(points)

    #calculate mean of opponent team's points
    def oppPtsMean(self,opp_points):
        return st.mean(opp_points)

    #calculate standard deviation of team's points
    def pointsStd(self,points):
        return st.stdev(points)

    #calculate standard deviation of opponent team's points
    def oppPtsStd(self,opp_points):
        return st.stdev(opp_points)




