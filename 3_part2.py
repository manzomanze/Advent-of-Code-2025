import re

class Battery:
    def __init__(self, distinct_number):
        self.distinct_number = distinct_number
        self.voltage = None
        self.position = None

    def get_voltage(self):
        return self.voltage

    def get_position(self):
        return self.position
    
    def set_voltage(self, voltage):
        self.voltage = voltage

    def set_position(self, position):
        self.position = position

def find_joltage(line,num_of_batteries):

    batteries = []
    for battery_num in range(0, num_of_batteries):    
        batteries.append(Battery(battery_num) )
    
    batteries[0].set_position(0)
    batteries[0].set_voltage(int(line[0]))
    for battery_num in range(0, num_of_batteries): 
        if battery_num > 0:
            batteries[battery_num].set_position(batteries[battery_num-1].get_position()+1)
            batteries[battery_num].set_voltage(int(line[batteries[battery_num].get_position()]))
        for i in range(batteries[battery_num].get_position(), len(line)-num_of_batteries + battery_num +1):
            print("Battery {}, Checking position {} with voltage {}".format(battery_num, i, line[i]))
            if int(line[i]) > batteries[battery_num].get_voltage():
                print("Found new voltage {} for battery {}".format(int(line[i]), battery_num))
                batteries[battery_num].set_voltage(int(line[i]))
                batteries[battery_num].set_position(i)
        

    for battery in batteries:
        print("Battery {}: Position {}, Voltage {}".format(battery.distinct_number, battery.get_position(), battery.get_voltage()))
        # Do something with joltage
    joltage_list = [str(battery.get_voltage()) for battery in batteries]
    joltage = ''.join(joltage_list)
    return int(joltage)



# Write an import of the text file  1_in_test
with open('3_in_test', 'r') as file:
    lines = [line.rstrip() for line in file]
sum_of_joltage = 0
for line in lines:
    joltage = find_joltage(line,12)
    print(joltage)

    sum_of_joltage += joltage
# #     sum_of_invalid_ids += sum_invalid_ids(invalid_ids)
print("The sum of all joltage is {}.".format(sum_of_joltage))
# print("The sum of all invalid IDs is {}.".format(sum_of_invalid_ids))



