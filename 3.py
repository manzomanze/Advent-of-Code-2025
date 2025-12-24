import re


def find_joltage(line):
    print(line)
    first_position = 0
    first_value = int(line[0])
    for i in range(0, len(line)-1):
        if int(line[i]) > first_value:
            first_value = int(line[i])
            first_position = i
    
    second_position = first_position + 1
    second_value = int(line[second_position])
    for i in range(second_position, len(line)):
        if int(line[i]) > second_value:
            second_value = int(line[i])
            second_position = i
    joltage = int(first_value)*10 + int(second_value)
    print(joltage)
    return joltage
        # Do something with joltage



# Write an import of the text file  1_in_test
with open('3_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]
sum_of_joltage = 0
for line in lines:
    joltage = find_joltage(line)
    sum_of_joltage += joltage
#     sum_of_invalid_ids += sum_invalid_ids(invalid_ids)
print("The sum of all joltage is {}.".format(sum_of_joltage))
# print("The sum of all invalid IDs is {}.".format(sum_of_invalid_ids))



