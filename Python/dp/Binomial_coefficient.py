# A Dynamic Programming based solution that uses table dp[][] to calculate the Binomial Coefficient. A naive recursive approach with table Python3 implementation 
 
# Returns value of Binomial Coefficient C(n, k) 

def binomialCoeffUtil(n, k, dp):
     
    # If value in lookup table then return 
    if dp[n][k] != -1: 
        return dp[n][k] 
 
    # Store value in a table before return 
    if k == 0:
        dp[n][k] = 1
        return dp[n][k] 
     
    # Store value in table before return 
    if k == n: 
        dp[n][k] = 1
        return dp[n][k] 
     
    # Save value in lookup table before return 
    dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
                binomialCoeffUtil(n - 1, k, dp))
                 
    return dp[n][k] 
 
def binomialCoeff(n, k):
     
    # Make a temporary lookup table 
    dp = [ [ -1 for y in range(k + 1) ] 
                for x in range(n + 1) ] 
 
    return binomialCoeffUtil(n, k, dp)
 
# Driver code
n = 5
k = 2
 
print("Value of C(" + str(n) +
               ", " + str(k) + ") is",
               binomialCoeff(n, k)) 
 
