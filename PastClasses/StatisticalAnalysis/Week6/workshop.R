datapath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week6"
trebuchetData<-read.csv(file=paste(datapath,"trebuchetdata.csv",sep="/"),header=TRUE,sep=",")
head(trebuchetData)

trebModel<-lm(distance~projectileWt,data=trebuchetData)
summary(trebModel)

anova(trebModel)


tasteData<-read.csv(file=paste(datapath,"tastetest.csv",sep="/"),header=TRUE,sep=",")
tasteData
taste.model<-lm(score~scr,data=tasteData)
summary(taste.model)
##mean of first group (coare) Intercept  B0
##mean of 2nd group (fine) estimate of scrfine/slope B1 + mean of first group. 
##rsqu could be better, residual sError looks big 20.9, F stat # df, p value small enough to reject
##null hypoth , predictor is significant
##calc B0 and B1 without using lm()
##mean value of first, and diff. tastemodel$coefficients

