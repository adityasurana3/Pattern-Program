# Print the following pattern

# 1
# 2 2
# 3 3 3

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print("")
