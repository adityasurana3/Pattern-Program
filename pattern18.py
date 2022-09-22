# Print the following pattern

# 1 1 1 1
#   2 2 2
#     3 3
#       4

n = int(input("Enter a number: "))

for i in range(1, n+1):
    space = i - 1
    for j in range(space):
        print(" ", end='')
        space = space + 1
    for k in range(n-i+1):
        print(i, end='')
    print("")
