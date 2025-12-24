import re

# Write an import of the text file  1_in_test
with open('1_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

password = 50
real_password = 0

for line in lines:
    number_match = re.search(r'(\d+)', line)
    direction_match =  re.search(r'([L,R])', line)
    number = int(number_match.group(1))
    direction = direction_match.group(1)
    old_password = password
    if direction == 'L':
        password = (password - number)%100
    elif direction == 'R':
        password = (password + number)%100
    if password == 0:
        real_password += 1
    print("The dial is rotated {} from {} to point at {}.".format(line, old_password, password))
print("The real password is {}.".format(real_password))
