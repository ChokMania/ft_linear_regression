import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import loadCSV


class LinearRegression() :

	def __init__(self):
		self.data = loadCSV("data/data.csv")
		self.theta0 = 0.0
		self.theta1 = 0.0
		self.km = ""
		self.price = ""
		self.learningRate = 0.1
		self.theta = [0.0, 0.0]
		self.cost_fun = []

	def estimatePrice(self, value):
		return self.theta0 + (self.theta1 * value)

	def standardize(l):
		return (l - np.mean(l)) / np.std(l)

	def destandardize(l, l_ref):
		return l * np.std(l_ref) + np.mean(l_ref)

	def transform(self):
		self.data = np.array(self.data)
		self.km = LinearRegression.standardize(self.data[:, 0])
		self.price = LinearRegression.standardize(self.data[:, 1])

	def untransform(self):
		self.price = self.estimatePrice(self.km)
		self.km = LinearRegression.destandardize(self.km, self.data[:, 0])
		self.price = LinearRegression.destandardize(self.price, self.data[:, 1])
		self.theta1 = (self.price[0] - self.price[1]) / (self.km[0] - self.km[1]) # coef fonction affine
		self.theta0 = -self.theta1 * self.km[0] + self.price[0] # y(0) = T0 + T1*x(0) => T0 = -T1*x(0) + y(0)
		self.theta = [self.theta0, self.theta1]

	def train(self):
		cost = 0.0
		tmpcost = -1.0
		m = len(self.km)
		i = 0
		while round(tmpcost, 20) != round(cost, 20) and i < 1000:
			tmpcost = cost
			self.theta0 = self.theta0 - self.learningRate * 1 / m * sum([(self.estimatePrice(self.km[i]) - self.price[i]) for i in range(m)]) #Σ
			self.theta1 = self.theta1 - self.learningRate * 1 / m * sum([(self.estimatePrice(self.km[i]) - self.price[i]) * self.km[i] for i in range(m)])
			cost = (1 / (2 * m)) * sum([(self.estimatePrice(self.km[i]) - self.price[i])**2 for i in range(m)]) ### MSE cost Function
			self.cost_fun.append(cost)
			i += 1

	def display(self):
		self.cost_fun = np.array(self.cost_fun)
		plt.plot(self.cost_fun)
		plt.ylabel("cost function")
		plt.xlabel("iteration")
		plt.title("Leaning Graph")
		plt.show()

if __name__ == "__main__":
	np.seterr(divide='ignore', invalid='ignore') # ignore error
	lr = LinearRegression()
	lr.transform()
	if len(lr.price) == 1 or len(lr.km) == 1:
		print("not enought data to train")
	else :
		lr.train()
		lr.untransform()
		np.savetxt("data/theta.txt", lr.theta, delimiter = ',');
		print ("Training is finished,\ntheta0: {0}\ntheta1: {1}".format(lr.theta[0], lr.theta[1]))
		lr.display()

