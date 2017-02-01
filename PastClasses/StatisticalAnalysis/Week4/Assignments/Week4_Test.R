datapath<-"C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week4/Assignments"
dat<-read.table(file=paste(datapath,"Week4_Test_Sample.csv",sep="/"),header = TRUE)
head(dat)
plot(dat$X, dat$Y)
Est.lm <- lm(dat$Y ~ dat$X,data=dat)
summary(Est.lm)

Est.Res <- Est.lm$residuals
plot(dat$X, Est.Res)
Probability.Density.Residuals <- density(Est.Res)
plot(Probability.Density.Residuals, ylim = c(0, 1))
lines(Probability.Density.Residuals$x, dnorm(Probability.Density.Residuals$x, 
                                             mean = mean(Est.Res), sd = sd(Est.Res)))

c(Left.Mean = mean(Est.Res[Est.Res < 0]), 
  Right.Mean = mean(Est.Res[Est.Res > 0]))

##Create Sequence of Residuals
Unscrambled.Selection.Sequence <- c()
for (i in 1:1000) {
  if(Est.Res[i]<0.0101774){
    Unscrambled.Selection.Sequence[i] <- 0
  } else{Unscrambled.Selection.Sequence[i] <- 1
  }  
}
head(Unscrambled.Selection.Sequence,30)
LinearModelData.Seq <- cbind(dat,Unscrambled.Selection.Sequence)

res <- list(Unscrambled.Selection.Sequence = Unscrambled.Selection.Sequence)
write.table(res, file=paste(dataPath, 'result.csv', sep = '/'), row.names = F)





