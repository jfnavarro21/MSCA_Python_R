

dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week3/Assignments"
df <- read.table(paste(dataPath, 'Week3_Test_Sample.csv', sep = '/'), header = TRUE)
head(df)
plot(df$X, df$Y)

lm.test <- lm(Y~X, data = df)

coef(lm.test)
-1.7072613
-0.5206628
mean(lm.test$residuals)
2.579317e-18
sd(lm.test$residuals)

2.061734



summary(lm.test)
lm.test$sigma

##Normal