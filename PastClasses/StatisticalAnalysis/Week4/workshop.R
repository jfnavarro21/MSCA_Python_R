u<-c(1,2,3)
v<-c(4,5,6)
u*v

(Dot.Product.1<-sum(u*v))

lVector<-function(vec){
  sqrt(vec%*%vec))
}
L
lVector(u)

u<-c(1.5,sqrt(3)/2)
v <- c(2,0)

##(Dot.Product.1<-sum(u*v))
(Dot.Product.2<-u%*%v)
Manual.Calculation.Projection.U.on.V <- (((u%*%v)/(lVector(v)^2))*v)


lVector(Manual.Calculation.Projection.U.on.V)




