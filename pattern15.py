# Print the following pattern

# D
# C D
# B C D
# A B C D
# 1st Method
# n = int(input("Enter a number: "))
# for i in range(n,1,-1):
#     for j in range(n-i):
#         print(chr(ord('A')+i+j-1)," ",end='')
#     print("")

# 2nd method
n = int(input("Enter a number: "))
for i in range(n+1):
    start = chr(ord('A')+n-i)
    for j in range(i+1):
        print(start, " ", end='')
        start = chr(ord(start)+1)
    print("")
