#using csv
import csv

with open('../resources/test.csv') as csv_file:
    csv_data = csv.reader(csv_file)
    print("***** using csv *******")
    print(list(csv_data))

#using numpy
from numpy import genfromtxt

data = genfromtxt('../resources/test.csv', delimiter=",", dtype=None, encoding="UTF-8")
print("***** using numpy *******")
print(data)

#using pandas
import pandas as pd

df=pd.read_csv("../resources/test.csv", delimiter=",", dtype=None, header=None)
print("***** using pandas *******")
print(df)