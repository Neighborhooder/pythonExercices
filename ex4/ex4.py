print("Insert three numbers separetad by commas: ")
numbers = input()

first, second, third = numbers.split(',')

if first == second and first == third:
    print("Equilateral Triangle")
elif first != second and second != third and first != third:
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")
