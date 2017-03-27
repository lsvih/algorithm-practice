##############################
#   Written By lsvih         #
#   2017-03-27               #
#   EM algorithm             #
##############################
import numpy as np
import matplotlib.pyplot as plt


mu1,mu2 = 40,20
sigma = 6

def generateDataAndShow():
    x1,x2 = mu1 + sigma * np.random.randn(500),mu2 + sigma * np.random.randn(500)
    x = np.append(x1,x2)
    plt.hist(x,50,normed=True)
    plt.show()
    return x

if __name__=='__main__':
    data = generateDataAndShow()
    Z = [[],[]]
    while True:
        o_mu1,o_mu2 = mu1,mu2
        Z = np.zeros([len(data),2])
        #E-Step:
        for i,X in enumerate(data):
            p1 = np.exp(-(X-mu1)**2/(2*sigma**2))/(sigma*(np.sqrt(2*np.pi)))
            p2 = np.exp(-(X-mu2)**2/(2*sigma**2))/(sigma*(np.sqrt(2*np.pi)))
            Z[i,0],Z[i,1] = p1/(p1+p2),p2/(p1+p2)
        #M-Step:
        mu1,mu2 = np.dot(np.array(data),np.array(Z))/np.sum(Z,axis=0)
        if abs(o_mu1-mu1)+abs(o_mu2-mu2) <= 0.001:
            print mu1,mu2
            break
    #Darw Gaussian function
    import matplotlib.mlab as mlab
    fig, ax = plt.subplots()
    n,bins,p = ax.hist(data,50,normed=True)
    y1,y2 = mlab.normpdf(bins, mu1, sigma), mlab.normpdf(bins, mu2, sigma)
    ax.plot(bins, y1/2)
    ax.plot(bins, y2/2)
    plt.show()
