import matplotlib.pyplot as plt
import pandas as pd


# ---- intro goals:
# 1, make a plot
# 2, review reading from a text file and analyzing data
# 3, use a pandas data frame to load and analyze data


# part 1 ---------------------------------------------------
ages = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
minutes = [10, 5, 3, 2, 2, 2, 3, 4, 5, 5, 5, 10, 10, 10, 15, 15, 15]
heights = [19.5, 40, 55, 61, 63, 64, 64, 64, 64, 64, 64, 63, 62, 62, 62, 62, 61] 

# at its most basic:
# we create a plot, configure the options, and show it
# TODO




# part 2 ---------------------------------------------------
# using the standard file reader
f = open("u321/temperature_data.csv")
my_list = []
for line in f:
    temp = line.strip()
    my_list.append(temp.split(','))   # append each row as a list
f.close()
# print("\nyou may want to look at the raw data: ")
# print("the list:", my_list)
# print("one row:", my_list[1])

# add up all 'anomalys'
# TODO



# part 3 ---------------------------------------------------
# using the pandas class
temp_data = pd.read_csv("u32SOLNS/u321SOLNS/temperature_data.csv", header=0)

# print("\nyou may want to look at some of the following")
# print("\nthe pandas data frame\n", temp_data)
# print("\ntype of pandas data:", type(temp_data))
# print("length:", len(temp_data))
# print("length again:", len(temp_data["Anomaly"]))
# print("one column:\n", temp_data['Anomaly'])
# print("type of column:", type(temp_data['Anomaly'])) #idk, but it is iterable!

# add up all 'anomalys'
# TODO

