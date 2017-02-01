dataPath <- "C:/Users/JohntheGreat/Documents/MSCA/StatisticalAnalysis/Week8/Assignments"
test_dat <- read.table(paste(dataPath,'Week8_Test_Sample.csv',sep = '/'), header=TRUE)
linmod <- lm(Output~Treatment, data=test_dat)
summary(linmod)
anova(linmod)
lm2 <-  lm(Output~Treatment-1, data=test_dat)
summary(lm2)
anova(lm2)
anova(linmod, lm2)

test_dat_loc <- test_dat
test_dat_loc$loc <- as.numeric(test_dat$Treatment)
test_dat_loc

linmod.loc <- lm(Output~1+(loc==2), data=test_dat_loc)
summary(linmod.loc)

anova(linmod.loc, linmod)
#loc==2 gives 86.214
linmod.loc <- lm(Output~1+(loc==3), data=test_dat_loc)
summary(linmod.loc)

anova(linmod.loc, linmod)
#loc==3 gives 53.199

#comparing A and B vs C
test_dat_loc$x1 <- with(test_dat_loc, (loc==1)+0.5*(loc==3))
test_dat_loc$x2 <- with(test_dat_loc, (loc==2)+0.5*(loc==3))
test_dat_loc

linmod.loc.3 <- lm(Output~-1+x1+x2, data=test_dat_loc)
summary(linmod.loc.3)
anova(linmod.loc.3, linmod)
#94.718
