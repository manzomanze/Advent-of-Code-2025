import re

                       

# Write an import of the text file  1_in_test
with open('5_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]

fresh_ranges_tuples = []
fresh_ranges_int = []
ingredients = []
start_ingredients = False

for line in lines:
    print(line)
    if not start_ingredients and line != "":
        fresh_ranges_tuples.append(line.split('-'))
    elif line != "":
        ingredients.append(line)
    
    if line == "":
        start_ingredients = True

for ranges in fresh_ranges_tuples:
    fresh_ranges_int.append([int(ranges[0]),int(ranges[1])])

print(fresh_ranges_tuples)
print(ingredients)
def myfunc(n):
  return int(n[0])

fresh_ranges_tuples_sorted = sorted(fresh_ranges_int,key=myfunc)
print(fresh_ranges_tuples_sorted)

last_range = fresh_ranges_tuples_sorted[0]
fresh_ids = last_range[1] - last_range[0] + 1
last_id = last_range[1]
for range_cursor in range(1,len(fresh_ranges_tuples_sorted)):
    print(fresh_ranges_tuples_sorted[range_cursor])
for range_cursor in range(1,len(fresh_ranges_tuples_sorted)):
    range = fresh_ranges_tuples_sorted[range_cursor]
    if range[1] <= last_id:
        print("Do nothing")
        last_range = range
        continue

    elif range[0] < last_id and range[1] > last_id:
        print("Case 0: Last  ID: {}, Last range was {},{}, Current range is {},{}".format(last_id, last_range[0], last_range[1], range[0], range[1]))
        print("fresh ids were {} to add {}".format(fresh_ids, range[1] - last_id))
        fresh_ids = fresh_ids + range[1] - last_id
        last_id = range[1]

    elif range[0] == last_id:
        print("Case 1: Last  ID: {}, Last range was {},{}, Current range is {},{}".format(last_id, last_range[0], last_range[1], range[0], range[1]))
        print("fresh ids were {} to add {}".format(fresh_ids, range[1] - last_id))
        fresh_ids = fresh_ids + range[1] - last_id
        last_id = range[1]

    elif range[0] > last_id:
        print("Case 2: Last  ID: {}, Last range was {},{}, Current range is {},{}".format(last_id, last_range[0], last_range[1], range[0], range[1]))
        print("fresh ids were {} to add {}".format(fresh_ids, range[1] - range[0] + 1))
        fresh_ids = fresh_ids + range[1] - range[0] + 1
        last_id = range[1]
    print(range)

    last_range = range

print(fresh_ids)

