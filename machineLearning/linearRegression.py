from sklearn.datasets import load_diabetes
from sklearn.datasets import load_iris
import numpy as np
# data = load_diabetes().data
# target = load_diabetes().target
#
# print("data shape : ",data.shape)
# print("target shape : ",target.shape)


data = load_iris().data
target = load_iris().target

# print("data shape : ",data.shape) #150,4
# print("target shape : ",target.shape) #150

x = data[:,:1]
y = target

x_train = x[:-20]
y_train = y[:-20].reshape((-1,1))
x_test = x[-20:]
y_test = y[-20:].reshape((-1,1))

# print("y_test shape : " ,y_train.shape) #130,1

class linear(object):
    def __init__(self):
        # 可以扩展想象为二元方程组中的系数以及偏差，及y=ax+b，此处a即为self.w，b即为self.b
        self.w = None
        self.b = None

    def loss(self,lossX,lossY):
        num_feature = lossX.shape[1] #特征数量
        num_train = lossX.shape[0] #训练数量

        h = lossX.dot(self.w)+self.b #当前拟合函数带入特征后得到的结果
        loss = 0.5*np.sum(np.square(h-lossY))/num_train #损失函数，均方误差
        dW = lossX.T.dot((h-lossY))/num_train #本轮修正之后的self.w
        db = np.sum((h-lossY))/num_train #本轮修正之后的self.b

        return loss,dW,db

    def train(self,trainX,trainY,learn_rate=0.0001,iters=500):
        numFeature = trainX.shape[1]
        self.w = np.zeros((numFeature,1))
        self.b = 0

        lossList = []

        for i in range(iters):
            loss,dw,db = self.loss(trainX,trainY)
            lossList.append(loss)
            self.w += -learn_rate*dw
            self.b += -learn_rate*db

            if(i%50==0):
                print("iters = %d,loss = %f,w = %f,b = %f" % (i,loss,self.w,self.b))

        return lossList

    def predict(self,testX):
        predY = testX.dot(self.w)+self.b
        return predY

    pass

classify = linear()
print("start!")
loss_list = classify.train(x_train,y_train)
print("end")
print(classify.w,classify.b)