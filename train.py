import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def estimatePrice(theta0, theta1, km):
	return theta0 + (theta1 * km)

def train(km, price):
	theta0 = 0.0
	theta1 = 0.0
	cost = 0.0
	tmpcost = -1.0
	cost_sum = []
	m = len(km)
	learningRate = 0.3
	while round(tmpcost, 20) != round(cost, 20):
		tmpcost = cost
		theta0 = theta0 - learningRate * 1 / m * sum([(estimatePrice(theta0, theta1, km[i]) - price[i]) for i in range(m)]) #Σ
		theta1 = theta1 - learningRate * 1 / m * sum([(estimatePrice(theta0, theta1, km[i]) - price[i]) * km[i] for i in range(m)])
		cost = (1 / (2 * m)) * sum([(estimatePrice(theta0, theta1, km[i]) - price[i])**2 for i in range(m)]) ### MSE cost Function
		cost_sum.append(cost)
	return(theta0, theta1, cost_sum)

def destandardize(l, l_ref):
	return l * np.std(l_ref) + np.mean(l_ref)

def standardize(l):
	return (l - np.mean(l)) / np.std(l)

if __name__ == "__main__":
	data = pd.read_csv("data/data.csv")
	data = np.array(data)
	km = standardize(data[:, 0])
	price = standardize(data[:, 1])
	theta0, theta1, cost_sum = train(km, price)

	price = estimatePrice(theta0, theta1, km)
	km = destandardize(km, data[:, 0])
	price = destandardize(price, data[:, 1])

	theta1 = (price[0] - price[1]) / (km[0] - km[1]) # coef fonction affine
	theta0 = -theta1 * km[0] + price[0] # y(0) = T0 + T1*x(0) => T0 = -T1*x(0) + y(0)

	theta = [theta0, theta1]

	np.savetxt("data/theta.txt", theta, delimiter = ',');
	print ("Training is finished,\ntheta0: {0}\ntheta1: {1}".format(theta0, theta1))
	cost_sum = np.array(cost_sum)
	plt.plot(cost_sum)
	plt.ylabel("cost function")
	plt.xlabel("iteration")
	plt.title("Leaning Graph")
	plt.show()