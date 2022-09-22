# Print the following pattern

#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

n = int(input("Enter a number: "))
for i in range(1, n+1):
    space = n-i
    for j in range(space):
        print(" ", end='')
        space = space-1

    for k in range(1, i+1):
        print(k, end='')

    start = i - 1
    for l in range(start):
        print(start, end='')
        start = start-1
    print("")
