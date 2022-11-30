import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from numpy import random

rc('font', family="AppleGothic")
rc('axes', unicode_minus=False)

# Generate N random numbers from a normal distribution
N = 10000
MEAN = 5
DEVIATION = 3
data = random.normal(MEAN, DEVIATION, N)

plt.scatter(range(1, N + 1), data, marker='.', s=1)
plt.xlabel('N')
plt.ylabel('X')
plt.title('{0}개의 난수를 생성하여 표시한 결과'.format(N))
plt.show()

bin_width = MEAN + (2 * DEVIATION)
plt.title('변수 i의 히스토그램')
plt.hist(data, edgecolor='black', bins=bin_width)
plt.show()

y, x, _ = plt.hist(data, bins=500)
plt.title('histogram 함수 사용')
plt.show()

mean_data = np.mean(data)
var_data = np.var(data)

pdf_data = [i / N for i in y]
plt.plot(x[:-1], pdf_data)
plt.title('실제 i에 대한 PDF')
plt.show()

def gaussian(x, mean, var):
    return 1 / np.sqrt(2 * np.pi * var) * np.exp(- (x - mean) ** 2 / (2 * var))

pdf = gaussian(x[1:], mean_data, var_data)
plt.title('정규분포로 가정한 i에 대한 PDF')
plt.plot(x[1:], pdf)
plt.show()

def get_probability(min_val, max_val, x, pdf):
    return sum([pdf[i] for i in range(len(x))
        if min_val <= x[i] <= max_val]) * 100

print('P(2 <= X <= 8) =', get_probability(2, 8, x[1:], pdf_data))

print('P(x <= -4.2) =', get_probability(-np.inf, -4.2, x[1:], pdf_data))
