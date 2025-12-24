import re
              
# Write an import of the text file  1_in_test
with open('6_in_test', 'r') as file:
    lines = [line.rstrip('\n') for line in file]

number_list_of_lists = []


print(' '.join(lines[0].split()))
for line in lines:
    temp_line = []
    for char in line:
        temp_line.append(char)
    number_list_of_lists.append(temp_line)
operators = number_list_of_lists.copy()[-1]
number_list_of_lists = number_list_of_lists[:len(number_list_of_lists)-1]

operators_without_spaces = operators.copy()
operators_without_spaces = [i for i in operators_without_spaces if i != " "]
print (operators)
print(operators_without_spaces)
print(number_list_of_lists)


# print(number_list_of_lists[0])

total = 0
if operators[0] == '+':
    result = 0
elif operators[0] == '*':        
    result = 1
for column_number in range(len(number_list_of_lists[0])):
    if(len(number_list_of_lists[0]) == column_number):
        break
    if operators[column_number] == '+':
        operator_to_use = "+"
        result = 0
        print("operator chosen +")
        
    elif operators[column_number] == '*':        
        operator_to_use = "*"
        print("operator chosen *")
        result = 1
        
    number = ""
    for number_list in number_list_of_lists:
        number = number + number_list[column_number]
    
    if number == "    ":
        total = total + result
        print("Partial RESULT: {}".format(result))
        continue
    else:
        print(number)
    if operator_to_use == '+':
        print(result)
        result = result + int(number)

    elif operator_to_use == '*':
        print(result)
        result = result * int(number)

     


# #     print (result)

print(total)