1
import math

def seriesSum(n):
    s = 0
    for i in range(1, n + 1):
        s += (math.pow(i, 2)) / math.factorial(i)
    return s

print(seriesSum(5))
print(seriesSum(20))