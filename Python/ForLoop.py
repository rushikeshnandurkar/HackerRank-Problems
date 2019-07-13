'''
Read an integer n. For all non-negative integers < n , print their squares.
'''
n = int(input().strip())
for num in range(0, n):     # Using for loop
    print(num ** 2)

'''    Using while loop
num = 0
while num < n:
    print(num ** 2)
    num += 1
'''