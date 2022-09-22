# Print the following pattern

# 1 2 3 4
#   2 3 4
#     3 4
#       4

n = int(input("Enter a number: "))

for i in range(1, n+1):
    space = i-1
    for j in range(space):
        print(" ", end='')
        space = space - 1
    # l = 1
    for k in range(1, n+1-i+1):
        print(i+k-1, end='')
    print("")
