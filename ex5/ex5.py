#outputs a single value
#outputs two values separated by underscore, i.e. abc_xyz
#outputs one value or its alternative, in case the first one was not found in the Data. i.e. 123 or 345

#Construct a set of JSON files to retrieve:
#- Name of the first training
#- internal_id aggregated with gross salary: i.e. "12345_1560€"
#- internal issues. or if empty, list of all parties.

import json
import ast

input = input()

with open(input + '.json') as f:
    req = json.load(f)

with open('data.json') as d:
    data = json.load(d)

def request(path):
    payload = 'data'
    for i in range(len(path)):
        if path[i].isdigit():
            payload += "[{}]".format(path[i])
        else:
            payload += "['{}']".format(path[i])
    return payload

if input == 'req_1':
    path = req['paths'].split('.')
    print(eval(request(path)))
elif input == 'req_2':
    path1 = req['paths'][0].split('.')
    path2 = req['paths'][1].split('.')
    print(str(eval(request(path1))) + req['delimiter'] + str(eval(request(path2))))
else:
    path1 = req['paths'][0][0].split('.')
    path2 = req['paths'][0][1].split('.')
    if eval(request(path1)) == []:
        print(eval(request(path2)))
    else:
        print(eval(request(path1)))
