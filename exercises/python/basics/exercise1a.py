
user_number = int(input("Enter a number: "))

fac = user_number

for i in range(user_number, 1, -1):
    fac *= (i-1)

print("Result of: " + str(user_number) + "! = " + str(fac))
