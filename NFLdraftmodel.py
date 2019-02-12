import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy 
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
filename2017 = '~/Desktop/CFB2017-2.xlsx' #assigns our spreadsheet data to filename2017
mergeddata = '~/Desktop/NFL PLAYERS DRAFTED.xlsx'
QB2017 = pd.read_excel(filename2017,sheet_name = 'Sheet1') #reads the data into python with pd.readexcel
DraftedQBs = pd.read_excel(filename2017,sheet_name = 'Sheet3')
CFBNFL = pd.read_excel(mergeddata,sheet_name = 'Merged Data')

##############################
#CODE FOR THE OFFICIAL DATA SET
##############################

print(CFBNFL)
print(len(CFBNFL))
print(CFBNFL.loc[1,'GS'])

type(DraftedQB)
dfDraftedQB = pd.DataFrame(np.array(DraftedQB))
print(dfDraftedQB)
dfDraftedQB[1]
type(dfDraftedQB)

#STATS + Histograms
collegeTDINTratio = CFBNFL['cTD']/CFBNFL['cInt'] #College TD/INT ratio
nflTDINTratio = CFBNFL['TD']/CFBNFL['Int']       #NFL TD/INT ratio
print(nflTDINTratio)
plt.hist(nflTDINTratio,bins=20)

collegeYPA = CFBNFL['cY/A']           #College Yards per attempt
nflYPA = CFBNFL['Yds']/CFBNFL['Att']  #NFL Yards per Attempt
print(nflYPA)
plt.hist(nflYPA,bins=20)
 
collegePCT = CFBNFL['cPct']           #College completion percentage
nflPCT = CFBNFL['Cmp']/CFBNFL['Att']  #NFL completion percentage
print(nflPCT)
plt.hist(nflPCT,bins=20)

collegeTDPA = CFBNFL['cTD']/CFBNFL['cAtt']  #Touchdowns per attempt
nflTDPA = CFBNFL['TD']/CFBNFL['Att']
print(nflTDPA)

collegeTDpergame = CFBNFL['cTD']/CFBNFL['cG'] #Touchdowns per game
nflTDpergame = CFBNFL['TD']/CFBNFL['GS']
print(nflTDpergame)

collegeRushYdspergame = CFBNFL['crYds']/CFBNFL['cG'] #rush yards per game
nflRushYdspergame = CFBNFL['rYds']/CFBNFL['GS']

collegeTotalYdspergame = (CFBNFL['cYds']+CFBNFL['crYds'])/CFBNFL['cG'] #total yards per game
nflTotalYdspergame = (CFBNFL['Yds']+CFBNFL['rYds'])/CFBNFL['GS']
print(collegeTotalYdspergame)

collegeINTPA = 1/(CFBNFL['cInt']/CFBNFL['cAtt']) #Calculates the inverse of interceptions per attempt
nflINTPA = 1/(CFBNFL['Int']/CFBNFL['Att'])
print(nflINTPA)
plt.hist(nflINTPA,bins=20)

collegeAYPA = CFBNFL['AY/A']
nflAYPA = (CFBNFL['Yds']+(CFBNFL['TD']*20)+(CFBNFL['Int']*(-45)))/CFBNFL['Att']

prA = (nflPCT-0.3)*5
prB = (nflYPA-3)*0.25
prC = (CFBNFL['TD']/CFBNFL['Att'])*20
prD = 2.375-((CFBNFL['Int']/CFBNFL['Att'])*25)
PR = ((prA+prB+prC+prD)/6)*100                  #Calculate a list of passer ratings
print(PR)    

for i in range(len(CFBNFL)):
    print(str(CFBNFL.loc[i,'Player']) + ' ' + str(PR[i]))

#Scatterplots

plt.scatter(collegeTDINTratio,nflTDINTratio) #TD/INT ratio plot
regTDINT = np.polyfit(collegeTDINTratio,nflTDINTratio,deg=1)
plt.plot(collegeTDINTratio,(regTDINT[0]*collegeTDINTratio)+regTDINT[1])
np.corrcoef(collegeTDINTratio,nflTDINTratio)

plt.scatter(collegeYPA,nflYPA) #Yards per attempt plot
regYPA = np.polyfit(collegeYPA,nflYPA,deg=1)
plt.plot(collegeYPA,(regYPA[0]*collegeYPA)+regYPA[1])
np.corrcoef(collegeYPA,nflYPA)

plt.scatter(collegePCT,nflPCT,c='red') #Completion Percentage Plot
regPCT = np.polyfit(collegePCT,nflPCT,deg=1)
plt.plot(collegePCT,(regPCT[0]*collegePCT)+regPCT[1])
np.corrcoef(collegePCT,nflPCT)

plt.scatter(CFBNFL['DrAge'],PR) #Draft Age vs. Passer Rating graph
regDrAge = np.polyfit(CFBNFL['DrAge'],PR,deg=1)
plt.plot(CFBNFL['DrAge'],(regDrAge[0]*CFBNFL['DrAge'])+regDrAge[1])
np.corrcoef(CFBNFL['DrAge'],PR)

def ScatterPlusTrendline(a,b):
    plt.scatter(a,b) #TD/INT ratio plot
    regg = np.polyfit(a,b,deg=1)
    plt.plot(a,(regg[0]*a)+regg[1])
    cc = np.corrcoef(a,b)
    print('The correlation coefficient is ' + str(cc[0,1]))    
    
ScatterPlusTrendline(collegeYPA,nflYPA) #Test of the scatterplot trnedline function

ScatterPlusTrendline(collegeTDPA,nflTDPA) #College TD/ATT versus NFL TD/ATT

ScatterPlusTrendline(10*collegeTDpergame,10*nflTDpergame) #TD per game plot

ScatterPlusTrendline(collegeRushYdspergame,nflRushYdspergame) #rushing yards per game plot

ScatterPlusTrendline(collegeTotalYdspergame,nflTotalYdspergame) #total yards per game

ScatterPlusTrendline(collegeINTPA,nflINTPA) #inverse of int per attempt

ScatterPlusTrendline(collegeAYPA,nflAYPA)
######################################
#CONFERENCE ANALYSIS

conferencelist=[]
Big12PR=[]
Pac12PR=[]
SECPR=[]
ACCPR=[]
BigTenPR=[]
OtherConfPR=[]
f=0
for i in range(len(CFBNFL)):
    currentrow = CFBNFL.loc[f,'Conf']
    print(currentrow)
    if currentrow == 'Big 12':
        conferencelist.append(1)
        Big12PR.append(PR[f])
    if currentrow == 'Pac-12':
        conferencelist.append(2)
        Pac12PR.append(PR[f])
    if currentrow == 'Pac-10':
        conferencelist.append(2)
        Pac12PR.append(PR[f])
    if currentrow == 'SEC':
        conferencelist.append(3)
        SECPR.append(PR[f])
    if currentrow == 'ACC':
        conferencelist.append(4)
        ACCPR.append(PR[f])
    if currentrow == 'Big Ten':
        conferencelist.append(5)
        BigTenPR.append(PR[f])
    if currentrow !='Big 12' and currentrow !='Pac-12' and currentrow !='Pac-10' and currentrow !='SEC' and currentrow !='ACC' and currentrow !='Big Ten':
        conferencelist.append(6)
        OtherConfPR.append(PR[f])
    print(conferencelist[f])
    f += 1
print('Big 12 mean is ' + str(np.mean(Big12PR)))
print('Big 12 standard deviation is ' + str(np.std(Big12PR)))
print('Pac 12 mean is ' + str(np.mean(Pac12PR)))
print('Pac 12 standard deviation is ' + str(np.std(Pac12PR)))
print('SEC mean is ' + str(np.mean(SECPR)))
print('SEC standard deviation is ' + str(np.std(SECPR)))
print('ACC mean is ' + str(np.mean(ACCPR)))
print('ACC standard deviation is ' + str(np.std(ACCPR)))
print('Big Ten mean is ' + str(np.mean(BigTenPR)))
print('Big Ten standard deviation is ' + str(np.std(BigTenPR)))
print('Other Conferences mean is ' + str(np.mean(OtherConfPR)))
print('Other conferences standard deviation is ' + str(np.std(OtherConfPR)))
Power5meanPR=(sum(Big12PR)+sum(Pac12PR)+sum(SECPR)+sum(ACCPR)+sum(BigTenPR))/(len(Big12PR)+len(Pac12PR)+len(SECPR)+len(ACCPR)+len(BigTenPR))
print('The mean passer rating for Power 5 conference QBs is ' + str(Power5meanPR))

plt.scatter(conferencelist,PR)

Power5PR = [Big12PR,Pac12PR,SECPR,ACCPR,BigTenPR,OtherConfPR]
fig, ax = plt.subplots()
ax.boxplot(Power5PR)
plt.show()

#HEATMAP

CFBNFLcorrmatrix = CFBNFL.corr()
sns.heatmap(CFBNFLcorrmatrix)


#Z SCORES
#####################

#Yards per attempt zscores
YPAzscore = scipy.stats.zscore(collegeYPA)
np.mean(collegeYPA)
for i in range(len(CFBNFL)):
    currentrow2 = CFBNFL.loc[i,'Player']
    zscore1 = YPAzscore[i]
    if zscore1 > 0:
        print(str(currentrow2) + ' is ' + str(zscore1) + ' standard deviations above average for yards per attempt.')
    if zscore1 < 0:
        print(str(currentrow2) + ' is ' + str(zscore1) + ' standard deviations below average for yards per attempt.')
    if zscore1 == 0:
        print(str(currentrow2) + ' is 0 standard deviations above/below average for yards per attempt.')
    
#Completion Percentage zscores
PCTzscore = scipy.stats.zscore(collegePCT)
np.mean(collegePCT)
for i in range(len(CFBNFL)):
    currentrow3 = CFBNFL.loc[i,'Player']
    zscore2 = PCTzscore[i]
    if zscore1 > 0:
        print(str(currentrow3) + ' is ' + str(zscore2) + ' standard deviations above average for completion percentage.')
    if zscore1 < 0:
        print(str(currentrow3) + ' is ' + str(zscore2) + ' standard deviations below average for completion percentage.')
    if zscore1 == 0:
        print(str(currentrow3) + ' is 0 standard deviations above/below average for completion percentage.')


