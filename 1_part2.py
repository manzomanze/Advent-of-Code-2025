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
        #print(password)
    elif direction == 'R':
        password = (password + number)%100


    if old_password - number <= 0 and direction == 'L':
        number_of_times_passed_through_zero = abs(int((old_password - number) / 100))
        # print(int(abs(old_password - number)))
        if old_password - number <= 0 and old_password - number > old_password - 100 and old_password != 0:
        if old_password - number <= 0 and old_password - number > old_password - 100 and old_password != 0:
            number_of_times_passed_through_zero += 1
        print(number_of_times_passed_through_zero)
        real_password += number_of_times_passed_through_zero
        print("The dial is rotated {} from {} to point at {} and passes through {} times".format(line, old_password, password, number_of_times_passed_through_zero))
    elif old_password + number >= 100 and direction == 'R':
        number_of_times_passed_through_zero = int((old_password + number) / 100)
        print(number_of_times_passed_through_zero)
        # print(int(abs(old_password + number)))
        # if old_password == 0:
        #     number_of_times_passed_through_zero -= 1
        real_password += number_of_times_passed_through_zero
        print("The dial is rotated {} from {} to point at {} and passes through {} times".format(line, old_password, password, number_of_times_passed_through_zero))
    else:
        print("The dial is rotated {} from {} to point at {} and passes through 0 times".format(line, old_password, password))
    
print("The real password is {}.".format(real_password))
