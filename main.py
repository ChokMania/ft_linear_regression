import pandas as pd
import matplotlib.pyplot as plt

def loadCSV(path):
	df = pd.read_csv(path)
	return df

class File():
	def __init__(self):
		self.theta0 = 0
		self.theta1 = 0
		self.nb = 0

	def loadTheta(self, path):
		try:
			with open(path) as file:
				theta = file.read()
				theta = theta.split()
			self.theta0 = float(theta[0])
			self.theta1 = float(theta[1])
		except:
			self.theta0 = 0
			self.theta1 = 0

	def getValue(self):
		nb = ""
		while (not nb.isnumeric() or nb == ""):
			nb = input("Enter a mileage: ")
			if (not nb.isnumeric()):
				print('Wrong input, we need a number')
		self.nb = int(nb)

	def display(self, data):
		plt.figure(figsize=(10, 8))
		for x in range(len(data["km"])):
			plt.plot(data["km"][x], data["price"][x], "b+")
		plt.plot([250000, 100], [self.estimatePrice(250000), self.estimatePrice(100)], 'r-')
		plt.plot(self.nb, prog.estimatePrice(self.nb), "go")
		plt.ylabel('price')
		plt.xlabel('km')
		plt.title("Estimated Price Graph")
		plt.show()

	def estimatePrice(self, mileage):
		return (self.theta0 + (self.theta1 * mileage))

if __name__ == '__main__':
	prog = File()
	prog.loadTheta("data/theta.txt")
	if prog.theta0 == 0 and prog.theta1 == 0:
		print("Model not trained.")
	prog.getValue()
	print("With:", prog.nb, "km, the estimated price is : ", prog.estimatePrice(prog.nb), "")
	data = loadCSV("data/data.csv")
	prog.display(data)