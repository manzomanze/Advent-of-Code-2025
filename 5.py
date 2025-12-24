import re

# def broaden_ranges(fresh_ranges):

#     range_to_merge_found = False
#     fresh_ranges_broadened = fresh_ranges.copy()
#     print (fresh_ranges_broadened)
#     for range_cursor in range(len(fresh_ranges)):
#         for range_2_cursor in range(len(fresh_ranges)):
#             start_range = int(fresh_ranges[range_cursor][0])
#             finish_range = int(fresh_ranges[range_cursor][1])
#             start_range_2 = int(fresh_ranges[range_2_cursor][0])
#             finish_range_2 = int(fresh_ranges[range_2_cursor][1])

#             if range_cursor != range_2_cursor and start_range <= start_range_2 and start_range_2 <= finish_range:
#                 print("case 1")
#                 smaller_start = start_range if start_range <= start_range_2 else start_range_2
#                 bigger_finish = finish_range if finish_range >= finish_range_2 else finish_range_2
#                 fresh_ranges_broadened.remove(fresh_ranges_broadened[max([range_cursor,range_2_cursor])])
#                 fresh_ranges_broadened.remove(fresh_ranges_broadened[min([range_cursor,range_2_cursor])])
#                 fresh_ranges_broadened.append([smaller_start,bigger_finish])
#                 return (True,fresh_ranges_broadened)

#             if range_cursor != range_2_cursor and start_range_2 <= start_range and start_range <= finish_range_2:
#                 smaller_start = start_range if start_range <= start_range_2 else start_range_2
#                 bigger_finish = finish_range if finish_range >= finish_range_2 else finish_range_2
#                 print("case 2")
#                 fresh_ranges_broadened.remove(fresh_ranges_broadened[max([range_cursor,range_2_cursor])])
#                 fresh_ranges_broadened.remove(fresh_ranges_broadened[min([range_cursor,range_2_cursor])])
#                 fresh_ranges_broadened.append([smaller_start,bigger_finish])
#                 return (True,fresh_ranges_broadened)
#     return (False,fresh_ranges_broadened)


   
                    

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

# something_to_broaden = True
# while something_to_broaden:
#     something_to_broaden,fresh_ranges_tuples = broaden_ranges(fresh_ranges_tuples)
#     print(fresh_ranges_tuples)
print("####")

print(fresh_ranges_tuples)
print(ingredients)

# fresh_ingredients_found = 0
# for ingredient in ingredients:
#     for range in fresh_ranges_tuples:
#         if int(ingredient) >= int(range[0]) and int(ingredient) <= int(range[1]):
#             fresh_ingredients_found += 1 

fresh_ingredients_found = 0
for ingredient in ingredients:
    for range in fresh_ranges_tuples:
        if int(ingredient) <= int(range[1]) and int(ingredient) >= int(range[0]):
            fresh_ingredients_found += 1
            break             


print (fresh_ingredients_found)