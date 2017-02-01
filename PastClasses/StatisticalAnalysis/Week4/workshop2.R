dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week4"
da<-read.csv(file=paste(dataPath,"LognormalSample.csv",sep="/"))
head(da$x)
plot(da$x)
hist(da$x)

mu <-  log(median(da$x))
sigma <- sqrt(2*((log(mean(da$x))- mu)))


c(mu=mu,sigma=sigma)