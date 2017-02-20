'''
Calculate expectation of savings.

Start of as script. Migrate to OOP.

'''

import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import numpy as np

class account():
    def __init__(self, total, APR, fee = 0):
        self.total = total
        self.APR = APR
        self.fee = fee
        self.totalGrowth = 0
        self.history = pd.DataFrame(columns=['date', 'total', 'totalGrowth','growth','yearlyGrowth'])
        self.growth = None

    def invest(self, income):
        self.total = self.total + income

    def withdraw(self,outgoing):
        self.total - self.total - outgoing

    def compound(self,fractionOfYear):
        self.growth = self.total *self.APR/100 * fractionOfYear
        self.totalGrowth = self.totalGrowth +self.growth
        self.total = self.total + self.growth

    def appendHistory(self,date):
        self.yearlyGrowth = np.sum(self.history.growth.tail(12))
        self.history = self.history.append(pd.DataFrame([[date,self.total, self.totalGrowth,self.growth,self.yearlyGrowth]], columns=['date', 'total', 'totalGrowth','growth','yearlyGrowth']))


#initialise
basicAccount = account(5000,5)
modelPeriodYears = 15
monthlySaving = 1000
startDate = dt.date.today()
date = startDate
##ff
for y in range(1,modelPeriodYears+1,1):
    for m in range(12):
        basicAccount.invest(700)
        basicAccount.compound(float(1)/float(12))
        date = relativedelta(months =1) + date
        basicAccount.appendHistory(date)

# print (basicAccount.history)

df = basicAccount.history

# df.set_index(date, inplace=True)

# import seaborn as sb

a = plt.plot(df['date'], df['total'])
b = plt.plot(df['date'],df['totalGrowth'])
c = plt.plot(df['date'],df['yearlyGrowth'])
# basicAccount.history.plot()

plt.show()