import os
import csv

wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

def print_percentages(wrestlerdata):

    name = str(wrestlerdata[0])
    wins = int(wrestlerdata[1])
    losses = int(wrestlerdata[2])
    draws = int(wrestlerdata[3])

    totalmatches = wins + losses + draws

    winpercent = (wins / totalmatches) * 100
    losspercent = (losses / totalmatches) * 100
    drawpercent = (draws / totalmatches) * 100

    if winpercent > 60:
        wrestlertype = "hold his own type of"
    else:
        wrestlertype = "questionable"
    
    print(f"Below are the stats for {name}:")
    print(f"{wrestlerdata[0]} is a {wrestlertype} fighter")
    print(f"Win %: {str(winpercent)}")
    print(f"Loss %: {str(losspercent)}")
    print(f"Draw %: {str(drawpercent)}")

with open(wrestling_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 
    header = next(csvreader)

    checkname = input("Name for data analysis extraction?")

    for row in csvreader:
        if checkname == row[0]:
            print_percentages(row)