i = 1
while i<=5:
    print(i)
    i+=1

#Sum until user enter 0
total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))
print("Total sum:", total)
