# source the data prep file
# setwd("/Users/gordondri/Desktop/OneDrive/MScA/Spring 2017 Quarter 3/MSCA 31006 - Time Series/Assignments/Final Project")
#setwd("C:/Users/Mary/OneDrive/MScA/Spring 2017 Quarter 3/MSCA 31006 - Time Series/Assignments/Final Project")

setwd("C:/Users/JohntheGreat/Documents/MSCA/TimeSeries/Course_Project")
source('Data_Preparation.R')
### Exploratory Analysis (Data Verification)

# add a season number column

# order alphabetically
game.log.all <- game.log.all[order(game.log.all$Team), ]
game.log.all$Team <- as.character(unclass(lapply(game.log.all$Team, as.character)))
# initialize counters 
start <- 1
game.log.all$Season.Num <- 0
game.log.all[1, "Season.Num"] <- 1
game.log.all$Season.Num[2:nrow(game.log.all)] <- sapply(2:nrow(game.log.all), function(z) {
  if (game.log.all[z, "Team"] == game.log.all[z-1, "Team"] & game.log.all[z, "Season"] == game.log.all[z-1, "Season"]){
    start
  } else if (game.log.all[z, "Team"] == game.log.all[z-1, "Team"] & game.log.all[z, "Season"] != game.log.all[z-1, "Season"]) {
    start <<- start + 1
    start
  } else {
    start <<- 1
    start
  }
})

# check how many seasons are represented for each team 
season.counter <- aggregate(Season.Num ~ Team, game.log.all, FUN = max)
head(season.counter)
sum(season.counter$Season)
# check how many games played in each season by each team
game.counter <- aggregate(G ~ Team + Season, game.log.all, FUN = max)
game.counter <- game.counter[order(game.counter$Team), ]
head(game.counter)

### Exploratory Analysis (Time Series)

# initialize libraries
library(TSA)
library(forecast)
library(tseries)

# function to check the plot of points scored by season for each team and check for stationarity
ts.analysis <- function(team.name, plot.type, plot.year = NULL){
  # create temp df
  temp <- subset(game.log.all, Team == team.name, select = c("GameType", "Season", "Date", "Tm", "Season.Num"))
  # subset by year if user selected a year
  if (!is.null(plot.year)){
    temp <- temp[temp$Season == plot.year, ]
  } else {
    plot.year <- "All Years"
  }
  # create reg season and playoffs for plotting 
  reg.season <- temp[temp$GameType == "RegularSeason", ]
  playoffs <- temp[temp$GameType == "Playoffs", ]
  # make time series (NOT SURE ABOUT THE FREQUENCY HERE)
  temp$Tm <- ts(temp$Tm, frequency = 82)
  reg.season$Tm <- ts(reg.season$Tm, frequency = 82)
  playoffs$Tm <- ts(playoffs$Tm, frequency = 82)
  
  # plot the correct graph
  if (plot.type == "All") {
    # check stationarity
    print(adf.test(temp$Tm)$p.value)
    # check periodicity
    
    # run auto arima
    temp.arima <- auto.arima(temp$Tm)
    summary(temp.arima)
    # plot
    plot(x = temp$Date, y = temp$Tm, type = "l", 
         xlab = "Date", ylab = "Team Points Scored by Game",
         main = paste("Points Scored by", team.name, plot.type, plot.year, sep = " "))
  } else if (plot.type == "Regular Season") {
    # check stationarity
    print(adf.test(reg.season$Tm)$p.value)
    # run auto arima
    temp.arima <- auto.arima(temp$Tm)
    summary(temp.arima)
    # plot
    plot(x = reg.season$Date, y = reg.season$Tm, type = "l",
         xlab = "Date", ylab = "Team Points Scored by Game",
         main = paste("Points Scored by", team.name, plot.type, plot.year, sep = " "))
  } else {
    # check stationarity
    print(adf.test(playoffs$Tm)$p.value)
    # run auto arima
    temp.arima <- auto.arima(temp$Tm)
    summary(temp.arima)
    # plot
    plot(x = playoffs$Date, y = playoffs$Tm, type = "l",
         xlab = "Date", ylab = "Team Points Scored by Game",
         main = paste("Points Scored by", team.name, plot.type, plot.year, sep = " "))
  }
}

# debug(ts.analysis)
ts.analysis("TOR", "Regular Season")
ts.analysis("TOR", "Regular Season", 2017)

for (i in 1991:2017){
  ts.analysis("ATL", i)
}

ts.analysis("ATL", "Regular Season", 2011)



LAL_1989 <- subset(game.log.basic, Team == "LAL" & Season == 1989 & GameType == "RegularSeason")
LAL_1989_Period <- periodogram(ts(LAL_1989$Tm))
LAL_1989_Period$freq
max_freq <- LAL_1989_Period$freq[which.max(LAL_1989_Period$spec)]
top_freq <- LAL_1989_Period$freq[which(LAL_1989_Period$spec>15000)]
top_freq
(top_freq)^-1
seasonality <- 1/max_freq
print(seasonality)
sea <- apply(top_freq, )
