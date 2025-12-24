import re

class Roll:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.removed = False

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position
    
    def remove(self):
        self.removed = True
    def is_removed(self):
        return self.removed
        

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

def remove_reachable_rolls(rolls):
    reachable_rolls = 0
    rolls_to_remove = []
    for roll in rolls:
        adjacent_rolls = 0
        if roll.is_removed():
            continue
        for roll2 in rolls:
            if roll != roll2:
                if not roll2.is_removed() and roll.get_x_position() + 1 >= roll2.get_x_position() and roll.get_x_position() - 1 <= roll2.get_x_position() and roll.get_y_position() + 1 >= roll2.get_y_position() and roll.get_y_position() - 1 <= roll2.get_y_position():
                    #print("Roll at ({},{}) is adjacent to roll at ({},{}).".format(roll.get_x_position(), roll.get_y_position(), roll2.get_x_position(), roll2.get_y_position()))
                    adjacent_rolls += 1
        print("Number of adjacent rolls {} of roll ({},{})".format(adjacent_rolls, roll.get_x_position(), roll.get_y_position()))
        if adjacent_rolls < 4 and not roll.is_removed():
            reachable_rolls += 1
            rolls_to_remove.append(roll)
            print("Removing roll at ({},{}).".format(roll.get_x_position(), roll.get_y_position()))
    for roll in rolls_to_remove:
        roll.remove()
    print("##### END PASS #####")
    if not rolls_to_remove:
        return (False, len(rolls_to_remove))
    return (True, len(rolls_to_remove))




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
            print("@", end='')
        else:
            print(".", end='')
        if column == len(lines[row])-1:
            print("")
    
to_remove = True
removed = 0
while to_remove:
    to_remove, removed_this_pass = remove_reachable_rolls(rolls)
    removed += removed_this_pass
    


print("Removed {} rolls.".format(removed))
