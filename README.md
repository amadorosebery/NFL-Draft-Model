# NFL-Draft-Model

### Abstract
-----------
A program that predicts which college football players should have the most success at the professional level. Our project aspires to determine the likelihood of a college-level quarterback to be successful upon being drafted into the NFL. Career stats of over 900 college quarterbacks from 2000 to 2016 were obtained in the form of a .csv file from pro-football-reference.com. This list was narrowed down to only include 87 players who were actually drafted into the NFL and played at least 10 games there.

### Contributors
-----------
-  Amado Rosebery
-  Joe Kinderman
-  Conor Levenson
-  Mihir Arya
-  Austin Miles
-  Kennard Peters


### Motivation
-----------
The NFL draft is a annual event where professional football teams take turns selecting college football players who will be added to their pro roster. Since the goal of an NFL football team to win as many games as possible, and ultimately win a championship, it makes sense that teams are always trying to draft the best college players possible who will help them win the most games. The problem is that some athletes perform extremely well in college but fail to find the same success at the pro level and vice versa. This is the motivation for our project. We wanted to build a computer program which, through the use of statistical analysis and modeling, would be able to help us predict which players were going to have the biggest impact in the NFL after coming out of college. There are many factors that go into projecting a player's skill at the NFL level, but we wanted to attempt to do so in a non-biased, scientific manner. Choosing the right college player to play for your team is decision that could lead to another year of mediocrity or a decade of success for your team, and for this reason we chose to build a program that can help teams make the most well informed decision possible. 

### Methodology - Data Wrangling
------------
We manually obtained all of our data from pro-football-reference.com. Each line of data contains a players’ college stats (and NFL stats if the QB played in both college and NFL).

We started with a .csv file containing all Division 1 FBS college football QBs who played between 2000 and 2017 (~2000). This list was then narrowed to 877 unique college QBs playing between 2000 and 2017 in D1. We then cross-referenced this data with all college QBs who were drafted into the NFL between 2000 and 2017, and created a subset list of these players.

### Methodology - Analysis
In order to build a model to predict which QB will perform best at the NFL level, we first wanted to determine which statistics were the best predictors of successful NFL QBs. We did this by creating several scatter plots comparing college stats to their NFL equivalent stats. For example, we created a scatter plot comparing college completion percentage to NFL completion percentage. Completion percentage is a useful measure of QB skill and thus we wanted to see if a high college completion percentage was correlated with a high NFL completion percentage. We then found the correlation coefficient for the plot and we were able to compare the correlation coefficients of all the plots to figure out which stats were the most important for predicting NFL success. We also made a correlation heat map to further help visualize which college and nfl stats had a high correlation. Box plots were also made comparing the success of NFL quarterbacks based on which conference they belonged to in college. 

For the second part of the project, we wanted to create a model which is able to determine which college players should be drafted and which ones should not be drafted based on their college stats. In order to accomplish this we were able to use a python library called SciKit Learn. We used a dataset including all college quarterbacks since 2000, their stats, and a column to specify whether they were drafted or not. We then used a classification model in the library to take in this dataset and return to us the statistics that it believed to be most important in determining whether or not a player gets drafted. The importance of the statistics is displayed in weights summing to one. We were then able to test the model by plugging in a dataset of 2017 college quarterbacks and their stats. The model returns a 1 if it believes the player should be drafted and a 0 if the player shouldn’t be drafted. We then compared our results with the actual 2017 nfl draft class to see how accurate the model was and how it can be improved. 

### Summary
Classification: We are still working on determining the best way to measure the accuracy of our model.

Weights: Based on the generated weight values using the SciKit Learn model, the three most relevant factors in predicting whether or not a player would be drafted were: total passing yards, touchdowns per game, interceptions per game.

Histograms: the approximate average of drafted college stats is greater than the approximate average of stats for all college players (as expected). Also validated the weightage of each of the 8 factors.


### Key Results

Data Visualization: 
Histograms (Refer to https://github.com/amadorosebery/NFL-Draft-Model/edit/master/TDYPA.png): In all graphs generated, all college QBs (blue) were compared to the subset of college QBs who actually were drafted into the NFL (green line). 

Scatterplots (Refer to Plots.pdf): Based on the scatter plots and the calculated correlation coefficients, we were able to determine that the most important stats for predicting whether a college football player would make a good NFL football player were completion percentage, yards per attempt, the inverse of interceptions per attempt, touchdown to interception ratio, and adjusted yards per attempt. The plot for draft age versus NFL passer rating also showed us that there is more uncertainty in the success of quarterbacks drafted at age 21 and quarterbacks drafted at age 23 were more consistent. 

Classification Model:
We used a decision tree, random forest, k nearest neighbor, and gradient boosted random forest classifiers to determine whether a college player will or will not be drafted. Using the python modeling libraries called SciKit-Learn and XGboost, combined with the dataset containing all QBs who played in college football, we determined weights for each of the 8 factors (columns). These weights essentially determined how relevant each metric was. Using these values, we used SciKit-Learn and XGboost to see whether players (from each year) would or would not be drafted into the NFL according to our model. We then compared this to whether the player was/was not drafted in actuality in that year. The most important factor based on the gradient boosted model was a Quarterback's Passing Yards. 


### Future Work
Include additional features such as weight and height of the quarterbacks.

