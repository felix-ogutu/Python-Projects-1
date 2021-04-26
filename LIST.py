thislist = ["felix", "Vincent", "Erick", "Cynthia"]
print(thislist)
print(len(thislist))  # This is to print the length of the list
print(thislist[0])  # this is to access the first item of the list
print(type(thislist))

numbers = [1, 2, 3, 4, 6]
boolean = [True, True, False]

print(boolean)
print(numbers)

# python if statements
a = 33
b = 200
if b > a:
    print(" b is greater than a ")

    # python elif statement
    a = 45
    b = 77
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

# python while loops
i = 0
while i <= 100:
    i = i + 1
    print(i)

    # Program to find the sum of all numbers stored in a list

    # List of numbers
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

    # variable to store the sum
    sum = 0

    # iterate over the list
    for val in numbers:
        sum = sum + val

    print("The sum is", sum)


# Creating a function
def my_function():
    print("Print hello from a function ")
    my_function()

    def my_names(fname):
        print(fname + "Omondi")
        my_names("Felix")
        my_names("Vincent")
        my_names("Erick")
