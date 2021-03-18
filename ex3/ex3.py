# read full name from keyboard
full_name = input()

# initialize empty list to store each full name character as an entry
reversed_list = []
# initialize empty string to store the reversed full name
nome = ''

# run for all characters inside full name string
for i in range (len(full_name)):
    # insert the actual character always in the beggining of the reversed list
    reversed_list.insert(0, full_name[i])

# convert the list into a string
for x in reversed_list:
    nome += x

# print the reversed string
print("Reversed String is : ", nome)
