import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import xlrd
import math
import statistics
from scipy.stats import norm


collegefile = "~\Desktop\DataScience\cfl_players.xlsx" #assigns our spreadsheet data to filename2017
cfbQb = pd.read_excel(collegefile,sheet_name = 'CFB') #reads the data into python with pd.readexcel
cfbDQb = pd.readexcel(collegefile, sheet_name = 'CFBD') #reads drafted stats into python

columnNames = list(cfbQb.head(0))

#STATS + Histograms
cTDINTratio = cfbQb['TD']/cfbQb['Int'] #College TD/INT ratio

cYPA = cfbQb['Y/A']                     #College Yards per attempt

cPCT = cfbQb['Pct']                     #College completion percentage

cTDPA = cfbQb['TD']/cfbQb['Att']        #Touchdowns per attempt

cTDpergame = cfbQb['TD']/cfbQb['G']     #Touchdowns per game

cRushYdspergame = cfbQb['RYds']/cfbQb['G'] #rush yards per game

cTtlYdspergame = (cfbQb['Yds']+cfbQb['RYds'])/cfbQb['G'] #total yards per game

cINTPA = 1/(cfbQb['Int']/cfbQb['Att']) #Calculates the inverse of interceptions per attempt

cAYPA = cfbQb['AY/A'] #College Average Yards per Attempt

'''((8.4 x Passing Yards) + (330 + Touchdown Passes) + (100 x Number of Completions) – (200 x Interceptions)) / Passing Attempts
'''
#Passer Rating
PR = ((8.4*cfbQb['Yds'])+(330+ cfbQb['TD'])+(100*cfbQb['Cmp'])-(200 * cfbQb['Int']))/ cfbQb['Att'] #College Passer Rating for All College QBs

PRD = ((8.4*cfbDQb['Yds'])+(330+ cfbDQb['TD'])+(100*cfbDQb['Cmp'])-(200 * cfbDQb['Int']))/ cfbDQb['Att'] #College Passer Rating for Drafted Qbs

minPr = min(PRD)

avgPr = sum(PR)/len(PR) #Average Passer Rating all college QBs

avgPrD = sum(PRD)/len(PRD) #Average Passer Rating of Drafted QBs

stdevPR = np.std(PR)

stdevPRD = np.std(PRD)

plt.plot(norm.pdf(PR,avgPr,stdevPR))







