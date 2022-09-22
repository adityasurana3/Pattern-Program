# Write a program to print the following output

# 3 2 1
# 3 2 1
# 3 2 1
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print(n-j+1, end='')
    print("")
