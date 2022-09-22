# Print the following pattern

#       1
#     2 3
#   4 5 6
# 7 8 9 10

n = int(input("Enter a number: "))
count = 1
for i in range(1, n+1):
    space = n-i
    for j in range(space):
        print(" ", end='')
        space = space-1
    for k in range(i):
        print(count, end='')
        count = count+1
    print("")
