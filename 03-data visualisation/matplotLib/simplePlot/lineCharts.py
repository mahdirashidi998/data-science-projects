from matplotlib import pyplot as plt
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
totalError = [x + y for x,y in zip(variance, bias_squared)]
xs = [i for i in range(len(variance))]
plt.plot(xs, variance, 'g-', label = 'variance')
plt.plot(xs, bias_squared, 'r-.', label = 'bias^2')
plt.plot(xs, totalError, 'b:', label = 'total error')
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")

plt.show()