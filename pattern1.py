# Write a program to print the following output

# 1 2 3
# 4 5 6
# 7 8 9

n = int(input("Enter a number:"))
k = 0
for i in range(n):
    for j in range(n):
        k = k+1
        print(k, " ", end='')
    print("")
