AM <- read.csv(file = "angry_moodsc.csv")
  AM$Sports = as.factor(AM$Sports)
  AM$Gender = as.factor(AM$Gender)
  
  aov_Q19 = aov(Anger_Expression ~ Gender*Sports, data = AM)
  summary(aov_Q19)
  
