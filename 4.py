import re

class Roll:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position
    

num_of_columns = 137
num_of_rows = 137
def create_index_column_row(lines,size):
    index = [[] for i in range(0,size)]
    for row in range(0, len(lines)):
        for column in range(0, len(lines[row])):
            roll = Roll(column, row)
            index[column].append(roll)
    return index

def create_index_row_column(lines,size):
    index = [[] for i in range(0,size)]
    for row in range(0, len(lines)):
        for column in range(0, len(lines[row])):
            roll = Roll(column, row)
            index[row].append(roll)
    return index


# Write an import of the text file  1_in_test
with open('4_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]
print(len(lines))
print(len(lines[0]))
index_column_row = [[] for i in range(0,137)]
index_row_column = [[] for i in range(0,137)]
rolls = []
for row in range(0, len(lines)):
    for column in range(0, len(lines[row])):
        if lines[row][column] == '@':
            roll = Roll(column, row)
            index_column_row[column].append(roll)
            index_row_column[row].append(roll)
            rolls.append(roll)
# print("The sum of all invalid IDs is {}.".format(sum_of_invalid_ids))

reachable_rolls = 0
for roll in rolls:
    adjacent_rolls = 0
    for roll2 in rolls:
        if roll != roll2:
            if roll.get_x_position() + 1 >= roll2.get_x_position() and roll.get_x_position() - 1 <= roll2.get_x_position() and roll.get_y_position() + 1 >= roll2.get_y_position() and roll.get_y_position() - 1 <= roll2.get_y_position():
                print("Roll at ({},{}) is adjacent to roll at ({},{}).".format(roll.get_x_position(), roll.get_y_position(), roll2.get_x_position(), roll2.get_y_position()))
                adjacent_rolls += 1
    if adjacent_rolls < 4:
        reachable_rolls += 1
        print("Roll at ({},{}) has {} adjacent rolls.".format(roll.get_x_position(), roll.get_y_position(), adjacent_rolls))

print("There are {} reachable rolls.".format(reachable_rolls))
