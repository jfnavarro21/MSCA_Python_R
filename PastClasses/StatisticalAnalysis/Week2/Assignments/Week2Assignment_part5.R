dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week2/Assignments"
dat <- read.table(paste(dataPath, 'Week2_Test_Sample.csv', sep = '/'), header = TRUE)$x
datNorm <- qnorm(dat[c(4:503)], mean = 0.0771813, sd = 0.8546440)
datExp <- qexp(dat[c(4:503)], rate = 0.8231119)
res <- cbind(datNorm=datNorm, datExp=datExp)
write.csv(res, file = paste(dataPath,'result.csv',sep="/"), 
          row.names = F)