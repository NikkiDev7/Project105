import csv
import math

with open("team_1.csv") as a:
    reader = csv.reader(a)
    file_data = list(reader)

data = []
for i in file_data[1:]:
    data.append(int(i[1]))

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total / n
    return mean

squared_list = []
for i in data:
    a = i - mean(data)
    a = a ** 2
    squared_list.append(a)

sum_of_squared_diff = 0
for i in squared_list:
    sum_of_squared_diff += i

result = sum_of_squared_diff / (len(data) - 1)
standard_deviation = math.sqrt(result)
print(f"The standard deviation is {standard_deviation}")