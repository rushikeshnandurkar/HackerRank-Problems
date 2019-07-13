'''

Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers

'''

n = int(input().strip())
m = int(input().strip())

print(n + m)
print(n - m)
print(n * m)
print(n // m)   # integer division
print(n / m)    # float division