import re

# Write an import of the text file  1_in_test
with open('1_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

password = 50
real_password = 0

for line in lines:
    number_match = re.search(r'(\d+)', line)
    direction_match =  re.search(r'([L,R])', line)
    movement = int(number_match.group(1))
    direction = direction_match.group(1)
    old_password = password
    if direction == 'L':
        delta = (movement - password)
        print(delta)
        if delta == 0:
            number_of_times_passed_through_zero = 1
        elif delta > 0:
            if password == 0:
                number_of_times_passed_through_zero = abs((delta // 100))
            else:
                number_of_times_passed_through_zero = abs((delta // 100)) + 1
        else:
            number_of_times_passed_through_zero = 0
            
        #print(password)
    elif direction == 'R':
        delta = movement + password
        number_of_times_passed_through_zero = abs(delta // 100)

    if direction == 'L':
        password = (password - movement)%100
        #print(password)
    elif direction == 'R':
        password = (password + movement)%100

    
    real_password += number_of_times_passed_through_zero
    print("The dial is rotated {} from {} to point at {} and passes through {} times".format(line, old_password, password, number_of_times_passed_through_zero))
print("The real password is {}.".format(real_password))
        

