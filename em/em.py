##############################
#   Written By lsvih         #
#   2017-03-23               #
#   EM algorithm             #
##############################
import numpy as np
import matplotlib.pyplot as plt

def generateDataAndShow():
    mu1,mu2 = 50,120
    sigma1,sigma2 = 20,30
    x1,x2 = mu1 + sigma1 * np.random.randn(500),mu2 + sigma2 * np.random.randn(500)
    plt.hist([x1,x2],50)
    plt.show()
    return x1+x2

if __name__=='__main__':
    data = generateDataAndShow()
