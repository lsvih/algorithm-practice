##############################
#   Written By lsvih         #
#   2017-03-22               #
#   k-means                  #
##############################
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def generateDataAndShow():
    plt.figure(figsize=(8,5))
    plt.title("Dataset", fontsize='small')
    datas, class_info = make_blobs(n_samples=200 ,n_features=2, centers=3)
    plt.scatter(datas[:, 0], datas[:, 1], marker='o', c=class_info)
    plt.show()
    return datas

def distance(data, dots):
    rs = []
    for d in data:
        rs.append([])
        for dot in dots:
            rs[-1].append(((d[0]-dot[0])**2+(d[1]-dot[1])**2)**0.5)
    return rs

def classify(dis):
    return [i.index(min(i)) for i in dis]

def calCenters(data, clazz):
    clz = [[] for i in range(3)]
    for index,dot in enumerate(data):
        clz[clazz[index]].append(dot)
    return [sum(x)/len(x) for x in clz]

def equal(dots1,dots2):
    for i in range(len(dots1)):
        for j in range(len(dots1[i])):
            if dots1[i][j] != dots2[i][j]:return False
    return True

if __name__=='__main__':
    data = generateDataAndShow()
    [x_max, y_max], [x_min, y_min] = np.amax(data,axis=0),np.amin(data,axis=0)
    centers = np.random.rand(3,2)
    centers[0:,0] = (x_max-x_min)*centers[0:,0]+x_min
    centers[0:,1] = (y_max-y_min)*centers[0:,1]+y_min
    clazz = classify(distance(data, centers))
    while True:
        new_centers = calCenters(data, clazz)
        if equal(new_centers,centers):break
        else:
            centers = new_centers
            clazz = classify(distance(data,centers))
    plt.figure(figsize=(8,5))
    plt.title("Dataset", fontsize='small')
    datas, class_info = make_blobs(n_samples=200 ,n_features=2, centers=3)
    plt.scatter(data[:, 0], data[:, 1], marker='o', c=clazz)
    plt.show()
