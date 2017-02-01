dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week9"
test_dat <- read.table(paste(dataPath,'Week9_Test_Sample.csv',sep = '/'), header=TRUE)
head(test_dat)
linMod <- lm(Resp~., data=test_dat)
summary(linMod)

#run PCA
test_dat_predictors <- test_dat[,-1]
head(test_dat_predictors)
test_dat_predictors_PCA <- princomp(test_dat_predictors)

#normalize predictors variances, sum the first 3
tdp.norm <- (test_dat_predictors_PCA$sdev^2)/(sum(test_dat_predictors_PCA$sdev^2))
sum(tdp.norm[1:3])
PCAFactors <- test_dat_predictors_PCA$scores
dataRotated <- as.data.frame(cbind(Resp=test_dat$Resp, PCAFactors))
head(dataRotated)
linModPCA <- lm(Resp~., data=dataRotated)
summary(linModPCA)
metrics <- calc.relimp(linModPCA, type = c("lmg","first", "last"))
metrics@lmg.rank
# Comp.1  Comp.2  Comp.3  Comp.4  Comp.5  Comp.6  Comp.7  Comp.8  Comp.9 Comp.10 
#1       4       8       9      10       2       3       5       7       6 


lm1 <- lm(Resp~Comp.1+Comp.6+Comp.7, data= dataRotated)
summary(lm1)