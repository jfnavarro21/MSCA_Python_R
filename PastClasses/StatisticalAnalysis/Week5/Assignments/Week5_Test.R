datapath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week5/Assignments"
dat<-read.table(file=paste(datapath,"Week5_Test_Sample.csv",sep="/"),header=TRUE)
head(dat)
nSample<-length(dat$Input)

GeneralModel <- lm(dat$Output~dat$Input)
matplot(dat$Input,cbind(dat$Output,GeneralModel$fitted.values),type="p",pch=16,ylab="Sample and Fitted Values")

estimatedResiduals<-GeneralModel$residuals
plot(dat$Input,estimatedResiduals)
Probability.Density.Residuals<-density(estimatedResiduals)
plot(Probability.Density.Residuals,ylim=c(0,.5))
lines(Probability.Density.Residuals$x,
      dnorm(Probability.Density.Residuals$x,mean=mean(estimatedResiduals),sd=sd(estimatedResiduals)))



##Method 2
plot(dat$Input,(dat$Output-mean(dat$Output))^2, type="p",pch=19,
     ylab="Squared Deviations")
##Create clustering parabola
y.bar <- mean(dat$Output)

B0.hat <- GeneralModel$coefficients[1]
B1.hat <-GeneralModel$coefficients[2]
y.i = B0.hat + B1.hat*dat$Input
clusteringParabola <- (y.i-y.bar)^2

plot(dat$Input,(dat$Output-mean(dat$Output))^2, type="p",pch=19,
     ylab="Squared Deviations")
points(dat$Input,clusteringParabola,pch=19,col="red")

Unscrambling.Sequence.Steeper.var <- (dat$Output-mean(dat$Output))^2 > clusteringParabola
head(Unscrambling.Sequence.Steeper.var,10)

##Separate the samples into two data frames
Subsample.Steeper.var<-
  data.frame(steeperInput.var=dat$Input,steeperOutput.var=rep(NA,nSample))
Subsample.Flatter.var<-
  data.frame(flatterInput.var=dat$Input,flatterOutput.var=rep(NA,nSample))
##Fill in the unscrambled outputs instead of NAs where necessary
Subsample.Steeper.var[Unscrambling.Sequence.Steeper.var,2]<-
  dat[Unscrambling.Sequence.Steeper.var,2]
Subsample.Flatter.var[!Unscrambling.Sequence.Steeper.var,2]<-
  dat[!Unscrambling.Sequence.Steeper.var,2]
##Print head of sample
head(cbind(dat,Subsample.Steeper.var,Subsample.Flatter.var),10)
plot(dat$Input,
     (dat$Output-mean(dat$Output))^2,
     type="p",pch=19,ylab="Squared Deviations")
points(dat$Input,clusteringParabola,pch=19,col="red")
points(dat$Input[Unscrambling.Sequence.Steeper.var],
       (dat$Output[Unscrambling.Sequence.Steeper.var]-
          mean(dat$Output))^2,
       pch=19,col="blue")
points(dat$Input[!Unscrambling.Sequence.Steeper.var],
       (dat$Output[!Unscrambling.Sequence.Steeper.var]-
          mean(dat$Output))^2,
       pch=19,col="green")
##mFlat <- lm(Subsample.Flatter.var$flatterOutput.var~Subsample.Flatter.var$flatterInput.var)
##mSteep <- lm(Subsample.Steeper.var$steeperOutput.var~Subsample.Steeper.var$steeperInput.var)
mSteep <- lm(dat$Output[Unscrambling.Sequence.Steeper.var]~dat$Input[Unscrambling.Sequence.Steeper.var],dat)
mFlat <- lm(dat$Output[!Unscrambling.Sequence.Steeper.var]~dat$Input[!Unscrambling.Sequence.Steeper.var],dat)

res <- list(GeneralModel = GeneralModel, mSteep = mSteep , mFlat = mFlat)
saveRDS(res, file = paste(datapath, 'result.rds', sep = '/'))
