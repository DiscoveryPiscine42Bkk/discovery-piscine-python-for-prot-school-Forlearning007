First_array = [2, 8, 9, 48, 8, 22, -12, 2]

First_array = [x for x in First_array if x >= 5]

First_array = list(set(First_array))

Second_array = [x + 2 for x in First_array]

Second_array = list(set(Second_array))

print("First array:", First_array)
print("Second array:", Second_array)
