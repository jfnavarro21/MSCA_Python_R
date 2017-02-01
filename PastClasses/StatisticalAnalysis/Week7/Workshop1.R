# Slope and Intercept
a<-.8; b<-.1
N.sample<-1000
X.mean<-3
X.sd<-2.5
set.seed(458769)
Eps.mean<-0
Eps.sd<-2
X <- rnorm(N.sample, 3, 2.5)
Eps <- rnorm(N.sample, Eps.mean, Eps.sd)
Y = b +a*X + Eps

LinearModel1<-cbind(X,Eps,Y)
head(LinearModel1)
plot(LinearModel1[,1],LinearModel1[,3])
Model1.lm<-lm(LinearModel1[,3]~LinearModel1[,1])
summary(Model1.lm)
Model1.lm.residuals <- Model1.lm$residuals
qqnorm(Model1.lm.residuals)
qqline(Model1.lm.residuals)
(my.Conf.Int<-confint(Model1.lm))
(my.Conf.Int[1,1]<=b)&(my.Conf.Int[1,2]>b)
(my.Conf.Int[2,1]<=a)&(my.Conf.Int[2,2]>a)
findInterval(.5,1:2)
findInterval(1.5,1:2)
findInterval(2.5,1:2)

Simulation.Experiment<-function(Intercept.b,Slope.a) {
  ##create norm dist Eps
  Eps.mean<-0
  Eps.sd<-2
  Eps <- rnorm(N.sample,Eps.mean, Eps.sd)
  ##Create linear model
  Y = Slope.a *X + Intercept.b + Eps
  LinearModel1<-cbind(X,Eps,Y)
  Model1.lm<-lm(LinearModel1[,3]~LinearModel1[,1])
  (my.Conf.Int<-confint(Model1.lm))
  ##return confidence interval
  return(c((findInterval(Intercept.b,my.Conf.Int[1,])==1),
           (findInterval(Slope.a,my.Conf.Int[2,])==1)))
  }
set.seed(94)
Repeated.Experiment<-replicate(10000,Simulation.Experiment(b,a))
dim(Repeated.Experiment)

Repeated.Experiment[,1:20]
Coverage.table<-rbind(Intercept=table(Repeated.Experiment[1,]),
                      Slope=table(Repeated.Experiment[2,]))
Coverage.table/c(sum(table(Repeated.Experiment[1,])),sum(table(Repeated.Experiment[2,])))

##Check if estimated probabilites are consistent w CI
#prop test checks uses normal distribution, binom uses exact binom
prop.test(Coverage.table[1,2],sum(Coverage.table[1,]),p=.95)
#Check with binomial test
binom.test(Coverage.table[1,2],sum(Coverage.table[1,]),p=.95)
#Check prop. test with slope
prop.test(Coverage.table[2,2],sum(Coverage.table[2,]),p=.95)
#Check with binom test
binom.test(Coverage.table[2,2],sum(Coverage.table[2,]),p=.95)
##for slope and obseverd slope, do not reject hypothesis that % coverage by conf int of the slope is 95%

set.seed(458769)
Eps <- runif(N.sample, -3,3.5)
Y = b +a*X + Eps
LinearModel2<-cbind(X,Eps,Y)
head(LinearModel2)
# Estimate linear model; evaluate the distribution of the residuals
Unif.lm<-lm(LinearModel2[,3]~LinearModel2[,1])
summary(Unif.lm)
qqnorm(Unif.lm$residuals,ylim=c(-5,5))
qqline(Unif.lm$residuals)
##new function
Simulation.Experiment<-function(Intercept.b,Slope.a) {
  ##create norm dist Eps
 
  Eps <- runif(N.sample, -3,3.5)
  ##Create linear model
  Y = Slope.a *X + Intercept.b + Eps
  LinearModel1<-cbind(X,Eps,Y)
  Model1.lm<-lm(LinearModel1[,3]~LinearModel1[,1])
  (my.Conf.Int<-confint(Model1.lm))
  ##return confidence interval
  return(c((findInterval(Intercept.b,my.Conf.Int[1,])==1),
           (findInterval(Slope.a,my.Conf.Int[2,])==1)))
}
set.seed(95)
Repeated.Experiment<-replicate(10000,Simulation.Experiment(b,a))
dim(Repeated.Experiment)
Repeated.Experiment[,1:20]
Coverage.table<-rbind(Intercept=table(Repeated.Experiment[1,]),
                      Slope=table(Repeated.Experiment[2,]))
Coverage.table/c(sum(table(Repeated.Experiment[1,])),
                 sum(table(Repeated.Experiment[2,])))
prop.test(Coverage.table[1,2],sum(Coverage.table[1,]),p=.95)
##Slope iss still95%, int is only 21% of cases because the mean of 
## unif dist is not zero
lm(formula = strength ~ limestone + water, data = concrete)
# Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  84.8167    12.2415   6.929 0.000448 ***
## limestone     0.1643     0.1431   1.148 0.294673    
## water       -79.6667    20.0349  -3.976 0.007313

##limestone not significant, water is

##anova lm1 and lm0. p value is small, reject NH of equivalence of 2 models
##means model 2 explains better than small model, bc big model has at least same residuals, cant be bigger
##if not equivalent, then bigger model is better
##if equivalent, then we prefer small model
##RSSsmall model is bigger than RSS big model
##Fstat and P value

##lm2 anova lm0
##rSS almost same for both
##excess sS 15.87  Pr 0.2947 so NH cannot be rejected that they are the same, pick smaller model
##lm3 lm0 anova
##RSS better, Pr 0.01746 NH will be rejected, 2 predictors is better than none
##lm4 lm0 anova
## sum of 2  vs 2 predictors
##RSS shows improvement, small P value, reject NH, in favor of big model
##lm5 lm0
##no INT, just limeston and water, big model is same
##very signif improvement in RSS, P value very small, big model better than model 
## with no intercept


VARIABLE SELECTION PART 3




