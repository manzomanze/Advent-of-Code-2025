import re


def find_invalid_ids(start, finish):
    print("Finding invalid IDs in range {}-{}.".format(start, finish))
    invalid_ids = []
    for id in range(start, finish + 1):
        print("Checking ID: {}".format(id))
        if (len(str(id)) % 2 == 0):
            first_half = str(id)[:len(str(id))//2]
            second_half = str(id)[len(str(id))//2:]
            print(first_half)
            print(second_half)
            if int(first_half) == int(second_half):
                print("Invalid ID found: {}".format(id))
                invalid_ids.append(id)
    print(invalid_ids)
    return invalid_ids

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
for range_name in ranges:
    start_finish_range= range_name.split('-')
    invalid_ids = find_invalid_ids(int(start_finish_range[0]), int(start_finish_range[1]))
    sum_of_invalid_ids += sum_invalid_ids(invalid_ids)
print("The sum of all invalid IDs is {}.".format(sum_of_invalid_ids))



