import os

def load_file():
    cwd = os.getcwd()
    with open(f"{cwd}/input.txt") as f:
        lines = f.read().splitlines() 
    return lines

def parse(input_file):
    data = []
    for i in input_file:
        datadict = {
            'range': i.split(' ')[0].split('-'),
            'letter': i.split(' ')[1].rstrip(':'),
            'password': i.split(' ')[2]
        }
        data.append(datadict)
    return data

data = parse(load_file())

def get_number_of_valid_passwords_range(data):
    validity_tracker = []
    for i in data:
        if i['password'].count(i['letter']) in range(int(i['range'][0]),int(i['range'][1])+1):
            validity_tracker.append(f"'{i['password']}' is valid.")
    return len(validity_tracker)

print(f"Count of valid passwords is: {get_number_of_valid_passwords_range(data)}")

def get_number_of_valid_passwords_single_position(data):
    for i in data:
        i.update({'valid':0})
        try:
            if i['password'][int(i['range'][0])-1] == i['letter']:
                i['valid'] = i.get('valid') +1
            if i['password'][int(i['range'][1])-1] == i['letter']:
                i['valid'] = i.get('valid') +1
        except Exception:
            pass

    validity_tracker = []        
    for i in data:
        if i['valid'] == 1:
            validity_tracker.append(f"'{i['password']}' is valid.")
    return len(validity_tracker)

print(f"Count of valid passwords is: {get_number_of_valid_passwords_single_position(data)}")