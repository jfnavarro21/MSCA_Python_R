dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week6/Assignments"
train_dat <- read.table(paste(dataPath,'Week6_Test_Sample_Train.csv',sep = '/'), header=TRUE)
main_dat <- read.table(paste(dataPath,'Week6_Test_Sample_Test.csv',sep = '/'), header=TRUE)

nSample.Training<-length(train_dat[,1])
head(train_dat)
plot(train_dat[,1],train_dat[,2], type="p",pch=19)
##Separate the models by using the 3rd column and plot the subsamples
LinearModel.Training.1<-cbind(train_dat[,1],rep(NA,nSample.Training))
LinearModel.Training.2<-cbind(train_dat[,1],rep(NA,nSample.Training))
LinearModel.Training.1[train_dat[,3]*(1:nSample.Training),2]<-
  train_dat[train_dat[,3]*(1:nSample.Training),2]
LinearModel.Training.2[(1-train_dat[,3])*(1:nSample.Training),2]<-
  train_dat[(1-train_dat[,3])*(1:nSample.Training),2]
head(cbind(train_dat,
           Training1=LinearModel.Training.1[,2],
           Training2=LinearModel.Training.2[,2]))

matplot(train_dat[,1],cbind(LinearModel.Training.1[,2],LinearModel.Training.2[,2]),
        pch=16,col=c("green","blue"),ylab="Subsamples of the training sample")
##Estimate linear model for training sample, look at the output
EstimatedLinearModel.Training <- lm(train_dat$Output ~ train_dat$Input)
summary(EstimatedLinearModel.Training)$coefficients
summary(EstimatedLinearModel.Training)$r.squared
summary(EstimatedLinearModel.Training)$sigma
EstimatedResiduals.Training<-EstimatedLinearModel.Training$residuals
plot(train_dat[,1],EstimatedResiduals.Training)
EstimatedResiduals.Training.1<-EstimatedResiduals.Training
EstimatedResiduals.Training.2<-EstimatedResiduals.Training
EstimatedResiduals.Training.1[(train_dat[,3]==0)*(1:nSample.Training)]<-NA
EstimatedResiduals.Training.2[(train_dat[,3]==1)*(1:nSample.Training)]<-NA
## Print first 10 rows
head(cbind(AllResiduals=EstimatedResiduals.Training,
           Training1Residuals=EstimatedResiduals.Training.1,
           Training2Residuals=EstimatedResiduals.Training.2,
           TrainingClass=train_dat[,3]))
# Plot the residuals corresponding to different models
matplot(train_dat[,1],cbind(EstimatedResiduals.Training.1, EstimatedResiduals.Training.2),pch=16,col=c("green","blue"),ylab="Separated parts of the training sample")
##1.2. Logistic regression#

Logistic.Model.Data<-data.frame(Logistic.Output=train_dat[,3], Logistic.Input=EstimatedResiduals.Training)
LinearModel.Training.Logistic<-glm(Logistic.Output~Logistic.Input,data=Logistic.Model.Data, family=binomial(link=logit))
summary(LinearModel.Training.Logistic)
names(LinearModel.Training.Logistic)
Predicted.Probabilities.Training<-predict(LinearModel.Training.Logistic,type="response")
plot(train_dat[,1],Predicted.Probabilities.Training)
Unscrambling.Sequence.Training.Logistic<-
  (predict(LinearModel.Training.Logistic,type="response")>.5)*1
##Create classified residuals
ClassifiedResiduals.Training.1<-EstimatedResiduals.Training
ClassifiedResiduals.Training.2<-EstimatedResiduals.Training
ClassifiedResiduals.Training.1[(Unscrambling.Sequence.Training.Logistic==0)*(1:nSample.Training)]<-NA
ClassifiedResiduals.Training.2[(Unscrambling.Sequence.Training.Logistic==1)*(1:nSample.Training)]<-NA
head(cbind(AllTraining=EstimatedResiduals.Training,
           Training1=ClassifiedResiduals.Training.1,
           Training2=ClassifiedResiduals.Training.2))
##Plot both classes of the residuals
matplot(train_dat[,1],cbind(ClassifiedResiduals.Training.1,
                                       ClassifiedResiduals.Training.2),
        pch=16,col=c("green","blue"),ylab="Classified residuals, X-axis at 0")
axis(1,pos=0)
Classification.Rule.Logistic <- -summary(LinearModel.Training.Logistic)$coefficients[1]/summary(LinearModel.Training.Logistic)$coefficients[2]
##Plot the data using the Classification.Rule.Logistic
matplot(train_dat[,1],cbind(ClassifiedResiduals.Training.1,
                                       ClassifiedResiduals.Training.2),
        pch=16,col=c("green","blue"),ylab="Classified residuals, X-axis at the rule level")
axis(1,pos=Classification.Rule.Logistic)

##1.3. Separate subsamples in the main sample using the classifier trained on the training sample#
###switched 2 and 1
EstimatedLinearModel<-lm(main_dat[,1]~main_dat[,2])
EstimatedLinearModel$coefficients
EstimatedResiduals<-EstimatedLinearModel$residuals
plot(main_dat[,1],EstimatedResiduals)
Unscrambling.Sequence.Logistic<-(predict(LinearModel.Training.Logistic,
                                         newdata=data.frame(Logistic.Output=EstimatedResiduals,
                                                            Logistic.Input=EstimatedResiduals),
                                         type="response")>.5)*1

res <- list(Unscrambling.Sequence.Logistic =  Unscrambling.Sequence.Logistic)
write.table(res, file = paste(dataPath,'result.csv',sep = '/'), row.names = F)

