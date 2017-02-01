# Load the germandata
AssignmentData<- read.csv("C:/Users/JohntheGreat/Documents/MSCA/DataMining/Assignment1/german_credit.csv", header=TRUE, sep=",")
head(AssignmentData)
# use sample() to separate the data into training/test
set.seed(555)
train_ind <- sample(seq_len(nrow(AssignmentData)), size = 632)
# separate into two data frames: train and test
train <- AssignmentData[train_ind, ]
test <- AssignmentData[-train_ind, ]
#Build a regression model to predict Credit Amount

modeltrain <- lm(Credit.Amount~Value.Savings.Stocks + Instalment.per.cent + Length.of.current.employment + Occupation, data=train)
summary(modeltrain)
r.sqd.train <- summary(modeltrain)$r.squared
r.sqd.train
#modeltest <- lm(V5~V7+V8+V17, data=test)
#summary(modeltest)

pv = 1155.66 + 108.87*Value.Savings.Stocks + (-703.23 * Instalment.per.cent) + 12.39 * Length.of.current.employment + 1362.64 * Occupation  




