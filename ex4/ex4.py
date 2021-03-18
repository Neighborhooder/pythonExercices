print("Insert three numbers separetad by commas: ")
numbers = input()

# takes the inputed string and split it into 3 different variables
first, second, third = numbers.split(',')

#if every size length is equal, it is an Equilateral, if all different Scalene, otherwise Isosceles
if first == second and first == third:
    print("Equilateral Triangle")
elif first != second and second != third and first != third:
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")
