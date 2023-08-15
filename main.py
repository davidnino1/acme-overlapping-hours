import os
from itertools import combinations

employee_times = []
employee_names = []

def read_file(filename, names, times):
    data_file_path = os.path.join(os.path.dirname(__file__), filename)
    my_file = open(data_file_path, "r")
    data = my_file.read()
    data_into_list = data.split("\n")
    print(data_into_list)
    for i in range(len(data_into_list)):
        names.append(data_into_list[i].split("=")[0])
        times.append(data_into_list[i].split("=")[1])
    print(names)
    print(times)
    my_file.close()

def add_to_week(employee_hours) -> list:
    list = employee_hours.split(",")
    hours = [(0,0)] * 7
    for i in list:
        if i[0:2] == "MO":
            hours[0] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "TU":
            hours[1] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "WE":
            hours[2] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "TH":
            hours[3] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "FR":
            hours[4] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "SA":
            hours[5] = (int(i[2:4]),int(i[8:10]))
        elif i[0:2] == "SU":
            hours[6] = (int(i[2:4]),int(i[8:10]))
    return hours

def overlapping_hours(first_employee, second_employee):
    overlap = 0
    for i in range(len(first_employee)):
        if (first_employee[i][0] <= second_employee[i][1]) and (second_employee[i][0] <= first_employee[i][1]):
            if(first_employee[i] != (0,0) and second_employee[i != (0,0)]):
                # print(str(first_employee[i]) + " " + str(second_employee[i]) + " There was an overlap")
                overlap += 1
    return overlap

def get_pairs(employee):
    pair = list(combinations(employee, 2))
    return pair

def compare_hours(names,times):
    pair_names = get_pairs(employee_names)
    pair_times = get_pairs(employee_times)
    for i in range(len(get_pairs(names))):
        overlap_names = pair_names[i][0] + '-' + pair_names[i][1]
        overlap_times = overlapping_hours(add_to_week(pair_times[i][0]), add_to_week(pair_times[i][1]))
        print(overlap_names + ': ' + str(overlap_times))

read_file("time_input.txt", employee_names, employee_times)
compare_hours(employee_names, employee_times)
