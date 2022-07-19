from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
# data = load_diabetes().data
# target = load_diabetes().target
#
# print("data shape : ",data.shape)
# print("target shape : ",target.shape)


data = load_iris().data
target = load_iris().target

# print("data shape : ",data.shape) #150,4
# print("target shape : ",target.shape) #150

trainData = data[:,:2]
# print(trainData[:,0],'\n',trainData[:,1])

#计算各个点之间的均差
def computeErrorForLineGivenPoints(param,points):
    totalError = 0
    m = param[0]
    b = param[1]
    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y-(m*x+b))**2
    return totalError/float(len(points))

#计算梯度下降的每一步下降的数值
def stepGradient(param,points,learningRate):
    mGradient = 0
    bGradient = 0
    n = float(len(points))
    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]
        bGradient += -(2/n)*(y-((mGradient * x)+bGradient))
        mGradient += -(2/n)*x*(y-((mGradient*x)+bGradient))
    newMGradient = param[0]-(learningRate*mGradient)
    newBGradient = param[1]-(learningRate*bGradient)
    return [newMGradient,newBGradient]

#n次迭代进行
def gradientDescentRunner(points,param,learningRate,iterations):
    b = param[1]
    m = param[0]
    for i in range(iterations):
        m,b = stepGradient(param,points,learningRate)
    return [m,b]

#绘图
def showplot(initParam,trainParam,trainData):
    plt.title("train before and after")
    xrange = np.arange(min(trainData[:,0]),max(trainData[:,0]),0.1)
    yBefore = initParam[0]*xrange+initParam[1]
    yAfter = trainParam[0]*xrange+trainParam[1]
    plt.plot(xrange,yBefore,label="before")
    plt.plot(xrange,yAfter,label="after")
    plt.scatter(trainData[:,0],trainData[:,1])
    plt.show()


def run():
    points = trainData
    learingRate = 0.0001
    init_b = 0
    init_m = 0
    iterations = 1000
    print("starting gradient descent at b = {0},m={1},error={2}".
          format(init_b,init_m,computeErrorForLineGivenPoints([init_m,init_b],points)))
    [m,b] = gradientDescentRunner(points,[init_m,init_b],learingRate,iterations)
    print(m,b)
    print("after gradient descent at b = {0},m={1},error={2}".
          format(b, m,computeErrorForLineGivenPoints([m, b],points)))

    showplot([0,0],[m,b],points)

if __name__ == '__main__':
    run()