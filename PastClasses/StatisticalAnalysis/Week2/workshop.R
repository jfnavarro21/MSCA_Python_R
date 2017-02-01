a <- 1
b <- 2.5


set.seed(8402)
eps <- rnorm(500, mean = 0, sd = 1.5)
head(eps)

set.seed(8402)
X1 <- rnorm(500, 3, 2.5)
Y1 <- a*X1 + b + eps


Model1 <- as.data.frame(cbind(Y = Y1, X = X1))

head(Model1)

plot(Model1$X,Model1$Y)

set.seed(2048)
X1 <- rnorm(500, 3, 2.5)
Y1 <- a*X1 + b + eps


Model1 <- as.data.frame(cbind(Y = Y1, X = X1))

head(Model1)

plot(Model1$X,Model1$Y)

set.seed(8402)
X1 <- rexp(500, 0.5)
Y1 <- a*X1 + b + eps


Model1 <- as.data.frame(cbind(Y = Y1, X = X1))

head(Model1)
plot(Model1$X,Model1$Y)

