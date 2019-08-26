import csv
import json
import os

with open('D:/employee_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i in csv_reader:
            print((i))


#data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


with open('data1.txt', 'w') as file1, open('data2.txt', 'w') as file2:
    print('opened multiple file')




os.chdir('D:/new_dir')
cwd = os.getcwd()
print("Current working directory is:", cwd)