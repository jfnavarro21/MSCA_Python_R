#rel imp function ehich most importnat for the output, previously pca was looking
#at relationship for predictors

#fit to smaller # of predictors, m<n. leaving original predictors, using new ones

#B=LBf  make vectors shorter. unmix them to find original slopes, mult vector of loadings onto new slopes
#gives original slopes
#L and Bf need to be reordered into importance of factors
#most im)PCA.rank <- metrics.swiss.pca@last.rank
  orderedLoadings <- swissPCALoadings[,order(PCA.rank)]
  #ordered CoefficientsPCA, from earlier  linmodPCA, before ran PCA, need to reorder to be consistent w loadings
  #dot product of loadings %*% coefficients
  #after pca when fit linear model, use meta features, bc fewer predictors than original predictors
  
  #after PCA use last, not lmg since its fast
  #decide how many factors we want, to describe the old predictors, not the output
  #explores relationships between predictors, nothing to do with linear model fitting
  #eigenvector is factor loading, weights of predictors
  #factor loading #1 is first eigenvector of covariance matrix
  #mix loadings w/ original predictors which gives us factors
  #L is the egenvector for Tao, also as weights for original predictors
  #Y0 = F%*%L^T,  F = Y0%*%L
  #L vectors are orthonormal
  #COv matrix is square, size of original predictors, 
  #Loading gets multiplied by a factor, if you see sign of loading, thats opposite
  #just happens, means sign of factor is opposite
  
  #fit linear model, look at summary, not all significant, out of order
  #different components are importnat to explain response
  
  
  #homework
  #centerd matrix, cova matrix, eigen decomp