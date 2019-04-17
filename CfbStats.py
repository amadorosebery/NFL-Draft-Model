import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import scipy
import xlrd
import math
import statistics
#import stats
from scipy.stats import norm
import seaborn as sns

#fig, ax = plt.subplots(1,1)

collegefile = ".\CFB_Stats_New_04022019.xlsx" #assigns our spreadsheet data to filename2017
cfbQb = pd.read_excel(collegefile,sheet_name = 'CFBND') #reads the data into python with pd.readexcel
cfbDQb = pd.read_excel(collegefile, sheet_name = 'CFBD1') #reads drafted stats into python

columnNames = list(cfbQb.head(0))

#STATS + Histograms
cTDINTratio = cfbQb['TD']/cfbQb['Int'] #College TD/INT ratio

cYPA = cfbQb['Y/A']                     #College Yards per attempt

cPCT = cfbQb['Pct']                     #College completion percentage

cTDPA = cfbQb['TD']/cfbQb['Att']        #Touchdowns per attempt

cTDpergame = cfbQb['TD']/cfbQb['G']     #Touchdowns per game

#cRushYdspergame = cfbQb['RYds']/cfbQb['G'] #rush yards per game

#cTtlYdspergame = (cfbQb['Yds']+cfbQb['RYds'])/cfbQb['G'] #total yards per game

cINTPA = 1/(cfbQb['Int']/cfbQb['Att']) #Calculates the inverse of interceptions per attempt

cAYPA = cfbQb['AY/A'] #College Average Yards per Attempt

'''((8.4 x Passing Yards) + (330 + Touchdown Passes) + (100 x Number of Completions) – (200 x Interceptions)) / Passing Attempts
'''

#######################################################

#Passer Rating
PR = ((8.4*cfbQb['Yds'])+(330+ cfbQb['TD'])+(100*cfbQb['Cmp'])-(200 * cfbQb['Int']))/ cfbQb['Att'] #College Passer Rating for All College QBs

#PR = pd.dataframe(PR)

#PR = PR.sort()

PRD = ((8.4*cfbDQb['Yds'])+(330+ cfbDQb['TD'])+(100*cfbDQb['Cmp'])-(200 * cfbDQb['Int']))/ cfbDQb['Att'] #College Passer Rating for Drafted Qbs

minPr = min(PRD)

#avgPr = sum(PR)/len(PR) #Average Passer Rating all college QBs

meanPr = np.mean(PR)

avgPrD = sum(PRD)/len(PRD) #Average Passer Rating of Drafted QBs

stdevPR = np.std(PR) #Sample-std deviation of College Passer Rating for college QBs

stdevPRD = np.std(PRD) #Sample-std deviation of College Passer Rating for Drafted QBs

normColl=norm.pdf(PR,meanPr,stdevPR) #Normal plot of college passer rating for all college QBs

normDraft=plt.plot(norm.pdf(PRD, avgPrD, stdevPRD)) #Normal plot of college Passer Rating for drafted QBs

fit = norm.pdf(PR, meanPr, stdevPR)  #this is a fitting indeed

fitd = norm.pdf(PRD, avgPrD, stdevPRD)

v1 = pd.Series(fit, name ='PR')
v2 = pd.Series(fitd, name = 'PR-Drafted')
#plt.plot(PR, fit, '-o')

#Histogram with line for College Passer Rating
'''
line_up=ax.hist(PR, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College') #Histogram

sns.kdeplot(PR) #Distribution line estimate

#Histogram with estimated Distribution Line for Drafted College Passer Rating

line_down=ax.hist(PRD, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College') #Histogram

sns.kdeplot(PRD) #Distribution line estimate

plt.legend()
'''
########                 
'''
#Plots stacked Passer Ratings
#plt.figure()
plt.hist([PR,PRD], histtype = 'barstacked' , density=True);
v3 = np.concatenate((PR, PRD))
sns.kdeplot(v3);
'''

###################################################################
#Yds comparision
#Total college Qb Yds 

cYds = cfbQb['Yds']

meancYds=np.mean(cYds)

stdevcYds = np.std(cYds)

#Drafted Qb yards

dYds = cfbDQb['Yds']

#Plots
'''
hist_dYds=ax.hist(dYds, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College Yds') #Histogram

sns.kdeplot(dYds)

hist_cYds=ax.hist(cYds, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College Yds') #Histogram

sns.kdeplot(cYds)
'''
##########STACKED
'''
plt.hist([cYds,dYds], histtype = 'barstacked' , density=True);
vYds = np.concatenate((cYds, dYds))
sns.kdeplot(vYds)
'''
###################################################################################
#Y/A Comparison

#College Total

cYPA

#College Drafted

dYPA = cfbDQb['Y/A']

#Plots

'''
hist_cYds=ax.hist(cYPA, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College Y/A') #Histogram

sns.kdeplot(cYPA)

hist_dYds=ax.hist(dYPA, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College Y/A') #Histogram

sns.kdeplot(dYPA)

plt.legend()
'''
###############################################################################
#Completion percentage comparision

#College Total
cPCT

#College Drafted
dPCT = cfbDQb['Pct']

#Plots
'''
hist_cYds=ax.hist(cPCT, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College Pct') #Histogram

sns.kdeplot(cPCT)

hist_dYds=ax.hist(dPCT, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College Pct') #Histogram

sns.kdeplot(dPCT)

plt.legend()
'''
###########################################################################################
#Touchdowns Per Attempt Comparison

#College Total
cTDPA

#College Drafted
dTDPA = cfbDQb['TD']/cfbDQb['Att']

#Plots

'''
hist_cYds=ax.hist(cTDPA, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College TD/Att') #Histogram

sns.kdeplot(cTDPA)

hist_dYds=ax.hist(dTDPA, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College TD/Att') #Histogram

sns.kdeplot(dTDPA)

plt.legend()
'''
#######################################################################################################
#Touchdowns Per Game Comparison

#College Total
cTDpergame

#College Drafted
dTDpergame = cfbDQb['TD']/cfbDQb['G']

#Plots

hist_cYds=ax.hist(cTDpergame, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College TD/G') #Histogram

#sns.kdeplot(cTDpergame)

hist_dYds=ax.hist(dTDpergame, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College TD/G') #Histogram

#sns.kdeplot(dTDpergame)

plt.legend()

##############################################################################################################################

#Total Yard per Game Comparison

#College Total
#cTtlYdspergame

#College Drafted
#dTtlYdspergame = (cfbDQb['Yds']+cfbDQb['RYds'])/cfbDQb['G']

#Plots
'''
hist_cYds=ax.hist(cTtlYdspergame, density=True, histtype='stepfilled', alpha=0.2, label = 'Total College Yds/G') #Histogram

sns.kdeplot(cTtlYdspergame)

hist_dYds=ax.hist(dTtlYdspergame, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College Yds/G') #Histogram

sns.kdeplot(dTtlYdspergame)

plt.legend()
'''

###############################################################################################################
'''
#Touchdown times Yds/ Attempts Comparision

#College Total
cTDYPA = (cfbQb['TD']*cfbQb['Yds'])/cfbQb['Att']

#College Drafted
dTDYPA = (cfbDQb['TD']*cfbDQb['Yds'])/cfbDQb['Att']

#Plots
hist_cTDYPA=ax.hist(cTDYPA,density=True, histtype='stepfilled',alpha=0.2, label = 'Total TD*Yds/Att') #Histogram

#plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
#sns.kdeplot(cTDYPA)

plt.xlabel('Touchdown times Yards divided by Attempts')

plt.ylabel('Probability Density')

hist_dTDYPA=ax.hist(dTDYPA, density=True, histtype='stepfilled', alpha=0.2, label = 'Drafted College TD*Yds/Att') #Histogram

#sns.kdeplot(dTDYPA)

plt.legend()

'''

