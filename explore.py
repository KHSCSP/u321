import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------
# at its most basic:
# we create a plot, configure the options, and show it
ages = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
minutes = [10, 5, 3, 2, 2, 2, 3, 4, 5, 5, 5, 10, 10, 10, 15, 15, 15]
plt.plot(ages, minutes)
plt.xlabel("Age")
plt.ylabel("Time (in minutes) it takes to cut your toe nails")
plt.title("Just goofin")
# plt.show()



# ---------------------------------------------------
# using the standard file reader
f = open("u321/temperature_data.csv")
my_list = []
for line in f:
    temp = line.strip()
    my_list.append(temp.split(','))   # append each row as a list
f.close()
print("\nthe raw data: ")
# print("the list:", my_list)
print("one row:", my_list[1])

# add up all 'anomalys'
sum = 0
for row in my_list[1:]:
    sum += float(row[1])
print("the sum: ", sum)


# ---------------------------------------------------
# using the pandas class
temp_data = pd.read_csv("u321/temperature_data.csv", header=0)

# print(temp_data)
print("\ntype of pandas data:", type(temp_data))
print("length:", len(temp_data))
print("length again:", len(temp_data["Anomaly"]))
print("one column:\n", temp_data['Anomaly'])
print("type of column:", type(temp_data['Anomaly'])) #idk, but it is iterable!

sum = 0
for item in temp_data['Anomaly']:
    sum += item

print("the sum: ", sum)

