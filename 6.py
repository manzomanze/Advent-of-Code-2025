import re
              
# Write an import of the text file  1_in_test
with open('6_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

number_list_of_lists = []


print(' '.join(lines[0].split()))
for line_cursor in range(len(lines)):
    number_list_of_lists.append(lines[line_cursor].split())
operators = number_list_of_lists.copy()[-1]    
number_list_of_lists = number_list_of_lists[:len(number_list_of_lists)-1]

print (operators)
print(number_list_of_lists)

print(number_list_of_lists[0])

total = 0
for column_number in range(len(number_list_of_lists[0])):
    if operators[column_number] == '+':
        result = 0
    elif operators[column_number] == '*':
        result = 1
    for number_list in number_list_of_lists:
        if operators[column_number] == '+':
            result = result + int(number_list[column_number])
        elif operators[column_number] == '*':
            result = result * int(number_list[column_number])
    total = total + result

    print (result)

print(total)