numbers = [10, 15, 20, 25, 30]
for n in numbers:
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

#Factorial using while loop
n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial:", fact)