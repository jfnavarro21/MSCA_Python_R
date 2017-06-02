dat <- sp500ret$sp500RET
ts.plot(dt)
acf(dat) # doesnt tell you to look at 2nd order
acf(dat^2)
McLeod.Li.test(y=dat) # want to reject the null hypothesis
McLeod.Li.test(y=mod$residuals)

# fGarch uses ljung box
# https://quant.stackexchange.com/questions/11019/garch-model-and-prediction


