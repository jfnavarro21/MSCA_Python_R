# Task 1
# print('That works')
# Task 2
# Part 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
#Simple Linear Regression
import statsmodels.formula.api as smf
from pandas_datareader import data

# Part 2

all_data = {}

for ticker in ['AAL', 'ALK', 'WTI']:
    all_data[ticker] = data.DataReader(ticker, 'yahoo', '2014-06-01', '2016-06-13')

print(all_data['WTI'].head())
print(all_data['AAL'].head())
print(all_data['ALK'].head())

# Part 3: Using dataframe

# Store the adjusted close prices into a DataFrame

price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})

print(price.head(5))

# Part 4: Calculate Return

daily_return = price.pct_change(1)
print(daily_return.head(5))

# Part 5: Scatter plot

plt.scatter(daily_return['AAL'], daily_return['WTI'])
plt.show()
# Part 6: Scatter plot

plt.scatter(daily_return['ALK'], daily_return['WTI'])
plt.show()
# Part 7: Using linear regression

# A Calculate the Intercept and coefficient for the linear regression
# between AAL and WTI


result = smf.ols(formula="WTI ~ AAL", data=price).fit()
print (result.params)


# A Calculate the Intercept and coefficient for the linear regression
# between ALK and WTI

result = smf.ols(formula="WTI ~ ALK", data=price).fit()





