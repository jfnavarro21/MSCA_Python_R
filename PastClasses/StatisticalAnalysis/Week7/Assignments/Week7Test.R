dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week7/Assignments"
test_dat <- read.table(paste(dataPath,'Week7_Test_Sample.csv',sep = '/'), header=TRUE)
#fit the linear models
fit.1<-lm(Output~1,data=test_dat)
fit.1.2<-lm(Output~1+Input1,data=test_dat)
fit.1.3<-lm(Output~1+Input2,data=test_dat)
fit.1.2.3<-lm(Output~.,data=test_dat)
anova(fit.1.2)
anova(fit.1.3)
anova(fit.1, fit.1.2.3)
anova(fit.1.2.3)
1.99
484.57
310.28
176.28
439.69
6?
7?First