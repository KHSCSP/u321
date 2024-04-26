import pandas as pd

# using the pandas class
temp_data = pd.read_csv("u321/temperature_data.csv", header=0)

# print("\nyou may want to look at some of the following")
# print("\nthe pandas data frame\n", temp_data)
# print("\ntype of pandas data:", type(temp_data))
# print("length:", len(temp_data))
# print("length again:", len(temp_data["Anomaly"]))
# print("one column:\n", temp_data['Anomaly'])
# print("type of column:", type(temp_data['Anomaly'])) #idk, but it is iterable!


# add up all 'anomalys'
sum = 0
# TODO

print("the sum: ", sum)

