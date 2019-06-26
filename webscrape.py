import requests
from lxml import html
import csv
import pandas as pd


year='2019'
teams=['TOR','GSW']






for team in teams:
    r = requests.get('https://www.basketball-reference.com/teams/' + team + '/' + year + '/gamelog/')
    data = html.fromstring(r.text)
    date = data.xpath("//tbody/tr/td[@data-stat='date_game']/a[@href]/text()")
    teamPoints = data.xpath("//tbody/tr/td[@data-stat='pts']/text()")
    oppPoints = data.xpath("//tbody/tr/td[@data-stat='opp_pts']/text()")
    print(team)
    print(date)
    print(teamPoints)
    print(oppPoints)