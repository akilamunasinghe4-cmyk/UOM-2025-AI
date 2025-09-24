'''
Total = 0
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        Total += num
print(Total)
'''



'''even Fibonacci numbers'''
'''
a, b = 0, 1
even_sum = 0
while b < 4000000:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b
print(even_sum)
'''