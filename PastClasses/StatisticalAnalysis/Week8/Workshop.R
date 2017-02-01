datapath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week8"
pollutionData<-read.csv(paste(datapath,"airpollution.csv",sep="/"))
pollutionData
pollution.Group.Means<-aggregate(pollution~location,data=pollutionData,mean)
pollution.Group.Means
locationsNames<-as.character(pollution.Group.Means[,1])
pollution.Group.Means<-pollution.Group.Means[,2]
names(pollution.Group.Means)<-locationsNames
pollution.Group.Means
airp.model<-lm(pollution~location,data=pollutionData)
summary(airp.model)
#int should be significant , bc its mean value of first group, difference might be insignificant
# only if mean value of int is zero, it will be insignificant
#comparing r2 is much larger than adj R sq, sample is small
#NH for Pr t, that slop of locations is different than zero
#-6.00 is first slop diff from hill suburb to plain suburb
#B1 is diff between mean values, diff between city and 1st suburb
#is not significant too. bc slope =0 cannot be rejected
#both slopes are insignif, but fit is good

#B0 = mean of first group, ,B1 = diff mean values
#B2 is diff mean of first group and second group
# model Y = B0+B1X1+B2X2, X1 and X2 are either 1 or 0, X1 = 1 if suburb
# 0 otherwise, X2=1 if its city, 0 otherwise
#hill sub m=B0, plains sub m2=B0+B1, city m3=B0+B2
#if NH cannot be rejected(slope = 0) then B1 is zero, which means no diff between
#group 2 and group 1
#city, cannot reject, B2=0, means m3 = 0, same as m1
#differeneces are not signif, both cannot be rejected
#Fstat, NH cannot be rejected, all slopes equal zero, so all slopes equal zero, so all group mean values equal
anova(airp.model)
# one predictor, wont show coeff for dummy variables. 
#sum of squares for location categorical predictor 4680and residuals202
#not enough to reject nh, which means location is not a significant predictor
#Pvalue in anova and summary testing same hypothesis
#all slopes of dummy variables are equal to zero, cannot be rejected
Grand.mean<-mean(pollutionData$pollution)
Grand.mean
Hill.Suburb<-subset(pollutionData, location=="Hill Suburb")
Plains.Suburb<-subset(pollutionData, location=="Plains Suburb")
Urban.City<-subset(pollutionData, location=="Urban City")
# First way: find SS for each subset, then add them together
Within.SS<-sum(((Hill.Suburb$pollution-pollution.Group.Means[1])^2))+
  sum(((Plains.Suburb$pollution-pollution.Group.Means[2])^2))+
  sum(((Urban.City$pollution-pollution.Group.Means[3])^2))

# Second way: do the same, but in one line using sapply()
Within.SS.one.line<-sum(unlist(sapply(names(pollution.Group.Means),
                                      function(z) 
                                        (subset(pollutionData,location==z)$pollution-
                                           pollution.Group.Means[names(pollution.Group.Means)==z])^2)))
c(Within.SS=Within.SS, Within.SS.one.line=Within.SS.one.line)
sum((pollutionData$pollution-Grand.mean)^2)
Model.Groups<-c(rep(pollution.Group.Means[1],length(Hill.Suburb$pollution)),
                rep(pollution.Group.Means[2],length(Plains.Suburb$pollution)),
                rep(pollution.Group.Means[3],length(Urban.City$pollution)))
sum((Model.Groups-Grand.mean)^2)
#This is the between the groups sum of squares.
#what is conclusion of anova()?that location as a categorical predictor is not significant
#maybe not enough data to show significance

##Assume you reject, then move to contrasts

##Example 7.3.6 Contrasts
airp<-pollutionData
airp$loc<-as.numeric(airp$location)
airp
#create the mocel for contrast 1
airp.model2<- lm(pollution~1+(loc==3),data=airp)
#this is without B1
summary(airp.model2)
#What is the mean of the first two groups together?
#loc, pr t =0.0544, not significantat 95%, on the borderline, w/ 6% it is significant
#64%r sq , not eff bc adj R sq low, 
# if location 3 is not significant, the model y = B0 +Eps
mean(pollution.Group.Means[1:2])
#create the model that is implied by m1=m2, compare the models than B1=B0
#Calcu the within the groups SS for new grouping
Within.SS.Suburban.Urban<-sum(((Hill.Suburb$pollution-mean(pollution.Group.Means[1:2]))^2))+
  sum(((Plains.Suburb$pollution-mean(pollution.Group.Means[1:2]))^2))+
  sum(((Urban.City$pollution-pollution.Group.Means[3])^2))
Within.SS.Suburban.Urban
#Compare airp.model and airp.model2.
anova(airp.model2,airp.model)
#model 2 is removed B1, other is complete model
#looking at P value(.51)Hyptho that the 2 models are equivalent, cannot be rejected
#B1=0

#next combine first and second together vs the third
airp$x1<-with(airp,(loc==1)+0.5*(loc==3))
airp$x2<-with(airp,(loc==2)+0.5*(loc==3))
airp
airp.model3<-lm(pollution~-1+x1+x2,data=airp)
summary(airp.model3)
#removing interceptin this model0, 2 predictors, leaving x1&x2. if it fits well, then it is equivalent, then C2 =0
#X1 and X2 is significant, Pval = 0, both slopes are not equal to zero
#use anova to compare this model with the original model

anova(airp.model3,airp.model)
#RSS of model 1 > RSS model 2, but P value is not significant
#that we cannot reject null hypoth, that the 2 models are equivalent
#then c2 =0

#Examples 7.3.7-7.3.8
model.matrix(airp.model)
#the matrix of experiment is good for omnibus test, test B1=B2=0
#to test equivalence of locations, contrasts matrix
(contrastsMatrix<-cbind(Suburb1=c(1,1,0,0,0,0),Suburb2=c(0,0,1,1,0,0),City=c(0,0,0,0,1,1)))
#this is 2nd basis m1=B0, m2=B1, m3=B2
#easier to create contrasts from this matrix
#C1
(C1.vector<-contrastsMatrix[,1]-contrastsMatrix[,2])
#C2 combine col 1 and 2, subtr 2*col 3
(C2.vector<-contrastsMatrix[,1]+contrastsMatrix[,2]-2*contrastsMatrix[,3])
(n.vector<-c(2,2,2))
#we are not comparing groups to old model, bc we have basis vector per group

#to build a statistic for testing H0:C1=0
(vC1.vector<-C1.vector/n.vector)
#normailze it, divide by length of vector
(uC1.vector<-vC1.vector/sqrt(vC1.vector%*%vC1.vector))
#test hypothesis C1=0
#   
#Fstatis is dot prod UC1 and Y square/MSE
(F_1<-(uC1.vector%*%pollutionData$pollution)^2/(Within.SS/3))
(t_1<-sqrt(F_1))
#calc p values
1-pf(F_1,1,3)
1-pt(t_1,3)
#0.5175 large enoug not to reject NH(C1=0) contrast comparison m1 and m2
#pval are not the same, both tell us not to reject NH

#c2
(vC2.vector<-C2.vector/n.vector)
#normalize it. its orthogonal to 1
(uC2.vector<-vC2.vector/sqrt(vC2.vector%*%vC2.vector))
#calculat e F2 statistic 
(F_2<-(uC2.vector%*%pollutionData$pollution)^2/(Within.SS/3))
1-pf(F_2,1,3)
(t_2<-sqrt(F_2))
1-pt(t_2,3)
#with 8.6 both reject hypothesis, with 4% both do not reject hypothesis

#arbitrary contrasts general case
A<-factor(pollutionData$location)#create a factor
#location is categorical variable
contrasts(A) #default settings
aov(pollutionData$pollution~A)# running one aov equivalent to running lm and anova

#tells aov want to use this contrast
#SS, DF for A and for Residuals. 
summary.lm(aov(pollutionData$pollution~A))
#takes lin model and going straight to summary
#plains sub not signif Pt, city is not significant cannot reject NH of utility test or slopes
#utility test was that both were equal to zero, individual slopes equal 0
contrasts(A) <- cbind("l1 vs l2"=c(1,-1,0),"l12 vs l3"=c(1,1,-2))
A
aov(pollutionData$pollution~A)
summary.lm(aov(pollutionData$pollution~A))
#8.5% almost makes loc12 v l3 significant, but they are not,
#loc 1 v loc2, loc1/2 v loc3. both contrasts in the output. 
#
