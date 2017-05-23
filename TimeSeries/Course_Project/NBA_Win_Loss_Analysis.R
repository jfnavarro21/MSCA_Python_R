library(tseries)
library(forecast)
library(TSA)

# Read in game logs

df <- read.csv("C:/Users/JohntheGreat/Documents/MSCA/SportsClub/team_game_logs_basic_1987_2017.csv", header=TRUE, sep=",")
head(df)
str(df)
colnames(df)

#for (year in 1987:2017) {
  

# Subset team = LAL for entire df of game logs
LAL.year <- subset(df, df$Team == "LAL" & df$GameType =="RegularSeason")
# Check LAL.year
print(tail(LAL.year))

# Remove rows with no data
row.to.keep <- LAL.year$G>0
#print(row.to.keep)
LAL.year.clean <- LAL.year[row.to.keep, ]
# Check the number of rows 2494 = 66+50+(82*29)
dim(LAL.year.clean)

LAL.vec <- (LAL.year.clean$W.L) == "W"
length(LAL.vec)
# Separate into train and test sets

train <- LAL.vec[1:2412 ]
test <- LAL.vec[2413:2494] 

#create time series data

train.ts <- ts(train, frequency = 82)
test.ts <- ts(test, frequency = 82)

# check for stationarity
adf.test(train.ts)
eacf(train.ts)
tsdisplay(train.ts)
auto.arima(train.ts)
