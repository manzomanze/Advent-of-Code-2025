import re
import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            large_divisors.append(i)
    return large_divisors

def find_invalid_ids(start, finish):
    print("Finding invalid IDs in range {}-{}.".format(start, finish))
    invalid_ids = []
    
    for id in range(start, finish + 1):
        print("Checking ID: {}".format(id))
        divisors = divisorGenerator(len(str(id)))
        for divisor in divisors:
            print ("Divisor: {}".format(divisor))
            divided_id = []
            if divisor == 1:
                section_length = 1
                number_of_sections = len(str(id))
            else:
                section_length = len(str(id)) // divisor
                number_of_sections = divisor


            for section_number in range(0, number_of_sections):
                print(len(str(id)))
                
                print("Section length: {}".format(section_length))
                start_index = section_number * section_length
                end_index = start_index + section_length
                print("Start index: {}, End index: {}".format(start_index, end_index))
                divided_id.append(str(id)[start_index:end_index])
            print(divided_id)
            divided_id_set = set(divided_id)
            if len(divided_id_set) == 1:
                print("Invalid ID found: {}".format(id))
                invalid_ids.append(id)
    print(invalid_ids)
    return set(invalid_ids)

def sum_invalid_ids(invalid_ids):
    total = 0
    for invalid_id in invalid_ids:
        total += invalid_id
    return total



# Write an import of the text file  1_in_test
with open('2_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

line = lines[0]

ranges = line.split(',')
print(ranges)
sum_of_invalid_ids = 0
all_invalid_ids = []
for range_name in ranges:
    start_finish_range= range_name.split('-')
    invalid_ids = find_invalid_ids(int(start_finish_range[0]), int(start_finish_range[1]))
    sum_of_invalid_ids += sum_invalid_ids(invalid_ids)
    all_invalid_ids.extend(invalid_ids)
print("The sum of all invalid IDs is {}.".format(sum_of_invalid_ids))
print("All invalid IDs found: {}".format(set(all_invalid_ids)))



