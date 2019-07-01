from gamesim import *
import pandas as pd
import csv


with open('scrapedData.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])