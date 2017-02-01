case1.varianceX<-.1
case1.varianceEps<-6
case1.slopeA<-2
case1.interceptB<-1
case1.sampleX<-rnorm(500,mean=0,sd=sqrt(case1.varianceX))
case1.sampleEps<-rnorm(500,mean=0,sd=sqrt(case1.varianceEps))
case1.sampleY<-case1.slopeA*case1.sampleX+case1.interceptB+case1.sampleEps


case2.varianceX<-.1
case2.varianceEps<-6
case2.slopeA<-2
case2.interceptB<-1
case2.sampleX<-rnorm(500,mean=0,sd=sqrt(case1.varianceX))
case2.sampleEps<-rnorm(500,mean=0,sd=sqrt(case1.varianceEps))
case2.sampleY<-case1.slopeA*case1.sampleX+case1.interceptB+case1.sampleEps


case3.varianceX<-.1
case3.varianceEps<-6
case3.slopeA<-2
case3.interceptB<-1
case3.sampleX<-rnorm(500,mean=0,sd=sqrt(case1.varianceX))
case3.sampleEps<-rnorm(500,mean=0,sd=sqrt(case1.varianceEps))
case3.sampleY<-case1.slopeA*case1.sampleX+case1.interceptB+case1.sampleEps


case4.varianceX<-.1
case4.varianceEps<-6
case4.slopeA<-2
case4.interceptB<-1
case4.sampleX<-rnorm(500,mean=0,sd=sqrt(case1.varianceX))
case4.sampleEps<-rnorm(500,mean=0,sd=sqrt(case1.varianceEps))
case4.sampleY<-case1.slopeA*case1.sampleX+case1.interceptB+case1.sampleEps

datapath<-"C:/Your path"

Correlation.Data<-read.csv(file=paste(datapath,'Week1_Correlation_Comparison_Project_Data.csv',sep='/'),
                           header=TRUE,sep=",")
Correlation.Data[1:10,]

par(mfrow=c(2,2))
with (Correlation.Data,{ 
  plot(Case1.X,Case1.Y,ylim=c(-8,8))
  plot(Case2.X,Case2.Y,ylim=c(-6,6))
  plot(Case3.X,Case3.Y,ylim=c(-1,3))
  plot(Case4.X,Case4.Y,ylim=c(0,2.5))
})

par(mfrow=c(1,1))

with(Correlation.Data,{
  Correlation.Case1<-cor(Case1.X,Case1.Y)
  Correlation.Case2<-cor(Case2.X,Case2.Y)
  Correlation.Case3<-cor(Case3.X,Case3.Y)
  Correlation.Case4<-cor(Case4.X,Case4.Y)
  rbind(cbind(Correlation.Case1,Correlation.Case2,Correlation.Case3,Correlation.Case4),
        cbind(Correlation.Case1^2,Correlation.Case2^2,Correlation.Case3^2,Correlation.Case4^2))
})


dataPath <- "C:/Users/JohntheGreat/Downloads/statistics_01_data/"
df <- read.table(paste0(dataPath, 'sample.csv'), header=TRUE)
sdX <- sd(df$x)
print(sdX)
sdY <- sd(df$y)
print(sdY)
cXY <- cor(df$x, df$y)
print(cXY)
a <- .578713
result <- data.frame(sdX=sdX, sdY=sdY, cXY=cXY, a=a)
write.table(result, file = paste0(dataPath, 'result.csv'), row.names = F)
print(result)

