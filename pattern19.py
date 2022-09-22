# Print the following pattern

#       1
#     2 2
#   3 3 3
# 4 4 4 4

n = int(input("Enter a number: "))
for i in range(1, n+1):
    space = n-i
    for j in range(space):
        print(" ", end='')
        space = space-1
    for k in range(i):
        print(i, end='')
    print("")
