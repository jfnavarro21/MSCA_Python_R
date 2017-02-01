

###set.seed(847337465)
Binomial.sample<-rbinom(500,size=20,prob=.7)
Binomial.sample
mean(Binomial.sample)/20

library(fitdistrplus)

Binomial.fit<-fitdist(Binomial.sample,dist="binom",fix.arg=list(size=20), start=list(prob=0.5))
c(Binomial.fit$estimate,sd=Binomial.fit$sd)

##critical value of binomal dist
## what is prob of being greater than observed value or 
## below the negative/opposite value. if combined value 
##is less than 2.5% then reject

p.upper <- pbinom(6923, size = 10000, p = 0.7)
p.lower <- pbinom(7077, size = 10000, p =0.7, lower.tail = F)
Tail.probabilities <- p.lower + p.upper

binom.test(sum(Binomial.sample),500*20,p=.7)

c(Binomial.fit$estimate-1.96*Binomial.fit$sd,Binomial.fit$estimate+1.96*Binomial.fit$sd)

###Poisson

set.seed(847337465)
Poisson.sample<-rpois(500,7)
mean(Poisson.sample)

Poisson.fit<-fitdistr(Poisson.sample,"Poisson")
c(Poisson.fit$estimate,sd=Poisson.fit$sd)

##2.2. Testing the fit

(t<-table(Poisson.sample))
(Sample.frequencies<-t/sum(t))

(Poisson.probabilities<-dpois(as.numeric(names(t)),7))
matplot(as.numeric(names(t)),cbind(Sample.frequencies,Poisson.probabilities),type="l",lty=1,lwd=2,ylab="Probabilities",xlab="Counts")
legend("topright",legend=c("Estimated","Theoretical"),lty=1,col=c("black","red"))

chisq.test(Sample.frequencies,Poisson.probabilities)
###exponential
set.seed(847337465)
Exponential.sample<-rexp(500,.3)


##4. Normal distribution
##4.1 Simulation and estimatio

## param.sd 0.06908584 0.04885107
##sd of the estimates

##lculate p-value of H0:??=??0H0:??=??0 against Ha:???????0Ha:???????0.
##2sided

##5. Uniform distribution

