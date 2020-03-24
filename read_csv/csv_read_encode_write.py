# using csv
import csv
from typing import List

with open('../resources/test.csv') as csv_file:
    csv_data = csv.reader(csv_file)
    print("***** using csv *******")
    print(list(csv_data))

# using numpy
from numpy import genfromtxt

data = genfromtxt('../resources/test.csv', delimiter=",", dtype=None, encoding="UTF-8")
print("***** using numpy *******")
print(data)

# using pandas
import pandas as pd
print("***** using pandas *******")
input_data = pd.read_csv("../resources/test.csv", delimiter=",", dtype=None, header=None)
list_of_lists = []
for row in input_data.values:
    word = row[0]
    output = row[1]
    l: List[int] = [-1] * 51
    for i in range(0, len(word)):
        l[i] = ord(word[i])
    l[50] = output
    list_of_lists.append(l)
print(list_of_lists)
with open('encoded_data.csv', 'w', newline='') as output_csv_file:
    writer = csv.writer(output_csv_file)
    writer.writerows(list_of_lists)

output_data = pd.DataFrame(list_of_lists)
output_data.to_csv('encoded_data_pandas.csv', header=False, index=False)
