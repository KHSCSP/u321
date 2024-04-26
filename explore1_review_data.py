
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
sum = 0
# TODO

print("the sum: ", sum)



