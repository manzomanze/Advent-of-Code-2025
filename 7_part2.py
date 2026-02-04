import re
              
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

# Write an import of the text file  1_in_test
with open('7_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

prev_line=lines[0]
saved_path = []
for line in lines:
    line = line.replace('S','|')
    char_list = list(line)
    for char_cursor in range(len(line)):
        if prev_line[char_cursor] == '|' and line[char_cursor] == '^':
            char_list[char_cursor-1] = '|'
            char_list[char_cursor+1] = '|'

        if prev_line[char_cursor] == '|' and line[char_cursor] == '.':
            char_list[char_cursor] = '|'
    line = "".join(char_list)
    x = re.search("\.*", line)
    if x.span()[0] == 0 and x.span()[1] == 142:
        line = prev_line.replace('^','.')
    prev_line = line
    saved_path.append(line)

numbers = []
for line in saved_path:
    temp_numbers = []
    char_list = list(line)
    for char_cursor in range(len(char_list)):
        if line[char_cursor] == '.' or line[char_cursor] == '^' or line[char_cursor] == '|': 
            temp_numbers.append(0)
    numbers.append(temp_numbers)

for number_list in numbers:
    print(number_list)

saved_path_lists = []
prev_line_list = list(saved_path[0])
for line in saved_path[1:]:
    prev_line_list = list(saved_path[0])
    line_list = list(line)
    saved_path_lists.append(line_list)

print(saved_path_lists)




    
# prev_line = saved_path[0]
# for line in saved_path[1:]:
#     char_list = list(line)
#     prev_char_list = 
#     print(char_list)
#     for char_cursor in range(len(char_list)):
#         if bool(re.search("\d", prev_line[char_cursor])):
#             print(bool(re.search("\d", prev_line[char_cursor])))
#             char_list[char_cursor] = char_list[char_cursor]
#             print(char_list)

#         if char_cursor != len(char_list)-1 and char_cursor != 0:
#             if line[char_cursor+1] == '^' and line[char_cursor-1] != '^':
#                 char_list[char_cursor] = int(prev_line[char_cursor+1])
#             elif line[char_cursor+1] != '^' and line[char_cursor-1] == '^':
#                 char_list[char_cursor] = int(prev_line[char_cursor-1])
#             elif line[char_cursor+1] == '^' and line[char_cursor-1] == '^':
#                 char_list[char_cursor] = int(prev_line[char_cursor+1]) + int(prev_line[char_cursor-1])
#         elif char_cursor == len(char_list) -1 and line[char_cursor-1] == '^':
#             char_list[char_cursor] = int(prev_line[char_cursor-1])
#         elif char_cursor == 0 and line[char_cursor+1] == '^':
#             char_list[char_cursor] = int(prev_line[char_cursor+1])
#     print(char_list)
#     prev_line = line
