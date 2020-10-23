import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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
		self.evolution = []

	def create_line(self, value):
		price = self.estimatePrice(self.km)
		km = self.destandardize(self.km, self.data[:, 0])
		price = self.destandardize(price, self.data[:, 1])
		tmpt1 = (price[0] - price[1]) / (km[0] - km[1])
		tmpt0 = -tmpt1 * km[0] + price[0]
		return tmpt0 + (tmpt1 * value)

	def estimatePrice(self, value):
		return self.theta0 + (self.theta1 * value)

	def standardize(self, l):
		return (l - np.mean(l)) / np.std(l)

	def destandardize(self, l, l_ref):
		return l * np.std(l_ref) + np.mean(l_ref)

	def transform(self):
		self.data = np.array(self.data)
		self.km = self.standardize(self.data[:, 0])
		self.price = self.standardize(self.data[:, 1])

	def untransform(self):
		self.price = self.estimatePrice(self.km)
		self.km = self.destandardize(self.km, self.data[:, 0])
		self.price = self.destandardize(self.price, self.data[:, 1])
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
			self.evolution.append([self.create_line(250000), self.create_line(100)])
			i += 1

	def display_cost(self):
		plt.ion()
		fig, ax = plt.subplots()
		x, y = [],[]
		sc = ax.scatter(x, y, c="r")
		plt.ylabel("cost function")
		plt.xlabel("iteration")
		plt.title("Learning Graph")
		plt.xlim(0,len(self.cost_fun))
		plt.ylim(min(self.cost_fun), max(self.cost_fun))
		plt.draw()
		for i in range(len(self.cost_fun)):
			x.append(i)
			y.append(self.cost_fun[i])
			sc.set_offsets(np.c_[x,y])
			fig.canvas.draw_idle()
			plt.pause(0.1)

def update(val):
	l1.set_data([250000, 100], lr.evolution[int(val)])
	plt.draw()

if __name__ == "__main__":
	np.seterr(divide='ignore', invalid='ignore') # ignore error
	lr = LinearRegression()
	lr.transform()
	if len(lr.price) == 1 or len(lr.km) == 1:
		print("not enought data to train")
	else :
		lr.train()
		lr.untransform()
		np.savetxt("data/theta.txt", lr.theta, delimiter = ',', fmt="%.10f")
		print ("Training is finished,\ntheta0: {0}\ntheta1: {1}".format(lr.theta[0], lr.theta[1]))
		lr.display_cost()
		### ANIMATION
		fig, main_ax = plt.subplots(figsize=(10, 8))
		for x in range(len(lr.data[:,0])):
			plt.plot(lr.data[:,0][x], lr.data[:,1][x], "b+")
		ax_slider = plt.axes([0.15, 0.01, 0.71, 0.03])
		slider = Slider(ax_slider, 'Epoch', 0, len(lr.evolution) - 1, valinit=0)
		slider.on_changed(update)
		l1, = main_ax.plot([250000, 0], lr.evolution[0], label="Estimated Price", lw=2)
		main_ax.set_xlabel('price')
		main_ax.set_ylabel('km')
		main_ax.set_title("Evolution of linear Regression")
		plt.show()


