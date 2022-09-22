# Print the following pattern

# 1
# 2 3
# 3 4 5
# 4 5 6 7

n = int(input("Enter a number: "))

for i in range(0, n):
    for j in range(i):
        # print(j,end='')
        print("i+j", i)
        print(i+j-1, " ", end='')
        # i = i+1
    print("")
