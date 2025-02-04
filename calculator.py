def addition(P, Q):
    return P + Q
def subtraction(P, Q):
    return P - Q
def multiplication(P, Q):
    return P * Q
def division(P, Q):
    return P / Q

print("Choose (a/b/c/d) for the calculation")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")

choice = input("Enter (a/b/c/d): ")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", addition(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtraction(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiplication(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", division(num_1, num_2))
else:
    print("Invalid Input")