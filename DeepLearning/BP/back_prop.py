# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : morindaz
# @FileName: back_prop.py
# @explanation: This file is for:

import numpy as np
import matplotlib.pyplot as plt


plot_x = np.linspace(-1, 6, 141) #模拟的自变量
ploy_y = (plot_x - 2.5) ** 2 -1 #模拟的损失函数
plt.plot(plot_x, ploy_y)


def dJ(theta): #损失函数的导数
    return 2 * (theta - 2.5)

def J(theta): #损失函数
    try:
        return (theta - 2.5) ** 2 -1
    except:
        return float('inf')

def gradient_descent(initial_theta = 0.0 , eta = 0.1, n_iter = 1e4, epsilon = 1e-8):
    theta_history = []
    gradient_history = [-10]

    theta = initial_theta #学习率
    theta_history.append(initial_theta) #用于记录自变量theta的变化情况
    i_iter = 0
    while i_iter < n_iter: #加入终止条件，如果循环次数大于预设，则跳出
        gradient = dJ(theta)
        print(gradient)
        last_theta = theta #上一次梯度
        theta = theta - eta * gradient #本次梯度更新的情况
        theta_history.append(theta) #记录下历史theta的更新情况
        gradient_history.append(gradient)
        # if abs(gradient)< epsilon: #如果损失函数大小基本不变化
        if(abs(J(theta) - J(last_theta))) < epsilon: #如果损失函数大小基本不变化
            break #退出循环
        i_iter += 1
    return theta_history, gradient_history

def plot_theta_history(theta_history, gradient_history):
    plt.plot(np.array(theta_history), J(np.array(theta_history)), color= 'r', marker ='+' )
    plt.show()
    plt.plot(np.array(theta_history), np.array(gradient_history), color= 'b', marker ='+' )
    plt.show()


if __name__ == '__main__':
    # theta_history, gradient_history = gradient_descent(0, 1.1, 10) #梯度爆炸的情况
    theta_history, gradient_history = gradient_descent() #梯度下降的情况
    plot_theta_history(theta_history, gradient_history)


## 参考链接：https://www.bilibili.com/video/av38405698?p=2