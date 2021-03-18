# 1 - outputs a single value
# 2 - outputs two values separated by underscore, i.e. abc_xyz
# 3 - outputs one value or its alternative, in case the first one was not found in the Data. i.e. 123 or 345

# Construct a set of JSON files to retrieve:
# - Name of the first training
# - internal_id aggregated with gross salary: i.e. "12345_1560€"
# - internal issues. or if empty, list of all parties.

# NOTE: to run this in your console you can do python3 ex5.py < test_1 for req_1, python3 ex5.py < test_2 for req_2 and so on

import json

# receive from terminal the request to run, e.g. req1
input = input()

# loads the request file object and converts it into an json object 
with open(input + '.json') as f:
    req = json.load(f)

# loads the data file object and converts it into an json object 
with open('data.json') as d:
    data = json.load(d)

# this function assemble a string to be in the format " data['employee']['fullName'] "
def request(path):
    # initialize the assembled string with 'data'
    payload = 'data'
    # runs all elements that represent the path to the resource
    for i in range(len(path)):
        # if the element is a number then it should be an array position and cannot have the ' in it
        if path[i].isdigit():
            payload += "[{}]".format(path[i])    
        else:
            payload += "['{}']".format(path[i])
    return payload

# depending on the request the input treatment is diferent
if input == 'req_1':
    # separate each part of the path into a list of strings
    path = req['paths'].split('.')
    # uses 'eval' to execute the string as a python code, returns and prints the resource available at the request path
    print(eval(request(path)))
elif input == 'req_2':
    # colects the first and second paths and threat them the same way as the previous one
    path1 = req['paths'][0].split('.')
    path2 = req['paths'][1].split('.')
    # prints the first requests, the delimiter and the second request
    print(str(eval(request(path1))) + req['delimiter'] + str(eval(request(path2))))
else:
    # colects the same way before but in a quadratic matrix
    path1 = req['paths'][0][0].split('.')
    path2 = req['paths'][0][1].split('.')
    # if theres is anything in the path one prints it, otherwise prints what is in path two
    if eval(request(path1)) == []:
        print(eval(request(path2)))
    else:
        print(eval(request(path1)))
