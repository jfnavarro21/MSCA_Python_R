import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('ggplot')

# Task 1: Loading the data

# Read the data in, but make sure it turns the Month column from strings to a datetime object
volume_data = pd.read_csv('volume_per_year.csv', index_col=0, parse_dates=True)
print((volume_data).head())
# print(volume_data.dtypes)
# print(volume_data.index)

# Task 2. Stationarity

# Question A
volume_data.plot()
plt.xlabel('Month')
plt.ylabel('Volume')
plt.title('Volume over Time')
plt.show()
# Task 2. Question B - What do you deduce from the plot?
# It looks like as time increases there is an uptrend in the volume.
# Also, the data appears cyclical, with larger swings over time.

# Task 2. Question C - Testing Stationarity
## Step 1 Calculate the moving average
ma = pd.rolling_mean(volume_data, 12)
#print(ma.head(12))

## Step 2 Calculate the moving standard deviation
msd = pd.rolling_std(volume_data, 12)
#print(msd.head(12))

##Step 3. Plot on the same graph Volume(blue), ma(green) and msd(red)
vol = plt.plot(volume_data, color='blue', label='Volume')
mean = plt.plot(ma, color='green', label='Rolling Moving Avg')
std = plt.plot(msd, color='red', label='Rolling Standard Dev')
plt.legend(loc='best')
plt.title('Rolling Moving Avg and St Dev')
plt.show(block=False)

# Task 2. Question C.
## Step 4. What do you conclude?
# The moving average(rolling mean) is trending upwards. Similarly, the rolling
# standard deviation is also trending upwards. The data does not look stationary

## Step 5. Run Dickey-Fuller Test on the data
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.stattools import adfuller

volume_data_test = adfuller(volume_data['volume'], autolag='AIC')
volume_data_output = pd.Series(volume_data_test[0:4],
                               index=['Test Statistic', 'p-value', '#Lags Used', '#Observations Used'])
for key, value in volume_data_test[4].items():
    volume_data_output['Critical Values (%s)' % key] = value

print(volume_data_output)


# What is the null hypotheisis of the Dickey Fuller test? What do you conclude?
# The NH of the DF test is whether a unit root is present in the data. Here it is present, so we cannot reject the NH
# and say that the data does NOT show stationarity

# Task 3. Make a Time Series Stationary
# Question A - Plot the log of the volume
vol_data_log = np.log(volume_data)
plt.plot(vol_data_log)
plt.show()
# Question B - What do you observe?
# It looks like the data is still trending upwards, but the total range of
# the y axis has shrunk

# Task 3. Question C - Smooth the data
logvolume = np.log(volume_data)
mavolume = pd.rolling_mean(logvolume, 12)
#Plot the graph
logvol = plt.plot(logvolume, color='blue', label='logVolume')
mean = plt.plot(mavolume, color='red', label='Rolling Moving Avg')
plt.legend(loc='best')
plt.title('Rolling Moving Avg of log of Volume')
plt.show(block=False)
volume_without_trend = logvolume - mavolume
plt.plot(volume_without_trend)
plt.title('Volume without trend')
plt.show()

# Task 3. Question D - Retest stationarity. Again, this was run in Pycharm

import statsmodels.tsa.stattools as ts
from statsmodels.tsa.stattools import adfuller
#
vol_wo_trend_test = adfuller(volume_without_trend['volume'], autolag='AIC')
vol_wo_trend_output = pd.Series(vol_wo_trend_test[0:4],
                                index=['Test Statistic', 'p-value', '#Lags Used', '#Observations Used'])
for key, value in vol_wo_trend_test[4].items():
    vol_wo_trend_output['Critical Values (%s)' % key] = value

print(vol_wo_trend_output)


# Question E - Redo the study with an exponentially weighted MA with a half period of one year
logvolume = np.log(volume_data)
ewma = pd.ewma(logvolume, halflife=12)
plt.plot(logvolume, color = 'blue')
plt.plot(ewma, color = 'red')
plt.title('Log volume with exp weighted Moving average')
plt.show()

# Question F - Retest Stationarity for ewma
vol_wo_ewma= logvolume - ewma
vol_wo_ewma.dropna(inplace=True)

import statsmodels.tsa.stattools as ts
from statsmodels.tsa.stattools import adfuller

vol_wo_ewma_test = adfuller(vol_wo_ewma['volume'], autolag='AIC')
vol_wo_ewma_output = pd.Series(vol_wo_ewma_test[0:4],
                                index=['Test Statistic', 'p-value', '#Lags Used', '#Observations Used'])
for key, value in vol_wo_ewma_test[4].items():
    vol_wo_ewma_output['Critical Values (%s)' % key] = value

print(vol_wo_ewma_output)


# Question G - What do you conclude with this different method
# It seems like the series using the ewma gives a smaller pvalue and a larger t statistic
# We can conclude that the data is stationary


# Task 4 - Removing trend and seasonality with differencing
# Question A - Remove the stationarity apply differencing to the log vol data

vol_log_diff = logvolume - logvolume.shift()
# Question B - Plot the graph
plt.plot(vol_log_diff)
plt.title('Differenced Log of Volume Data')
plt.show()

# Task 5 - Forecast Time Series
from statsmodels.tsa.stattools import acf, pacf
vol_log_diff.dropna(inplace=True)
print(vol_log_diff.head())
lag_acf = acf(vol_log_diff, nlags=20)
lag_pacf = pacf(vol_log_diff, nlags=20, method='ols')

#Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(vol_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(vol_log_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

# Task 5 continued
# Question B - load ARIMA
from statsmodels.tsa.arima_model import  ARIMA

# Question C - Run the model using p=2, d=1, q=2

model = ARIMA(logvolume, order=(2,1,2))
# Question D - store the results
results_AR = model.fit(disp=-1)
# Question E - plot the log volume with results_ARIMA
plt.plot(vol_log_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('results_AR.fittedvalues and Log diff of volume')
plt.show()

# Question F - Convert the predicted values into original scale
predictions_AR_diff = pd.Series(results_AR.fittedvalues, copy=True)
print(predictions_AR_diff.head())
predictions_AR_diff_cumsum = predictions_AR_diff.cumsum()
print(predictions_AR_diff_cumsum.head())

# Question G - Apply exponential to go back to the initial scale
predictions_AR_log = pd.Series(logvolume.ix[0], index=logvolume.index)
predictions_AR_log = predictions_AR_log.add(predictions_AR_diff_cumsum,fill_value=0)
predictions_AR_log.head()
predictions_ARIMA = np.exp(predictions_AR_log)