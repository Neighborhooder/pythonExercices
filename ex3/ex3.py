full_name = input()

reversed_list = []
nome = ''

for i in range (len(full_name)):
    reversed_list.insert(0, full_name[i])

for x in reversed_list:
    nome += x

print("Reversed String is : ", nome)
