import math

sum=0.0
for i in range(0, 23):
    sum += math.pow(1/2, i+1) * 1

print(sum)

sum2 = 0.0
for i in range(24, 30):
    sum2 += math.pow(2, i-24) * 1

print(sum2)