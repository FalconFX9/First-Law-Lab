import matplotlib.pyplot as plt
import numpy as np


# Element Numbers
TIME = 0
T1 = 1
T_WALL = 2
T_TOP_PLATE = 3
T_BOT_PLATE = 4
P1 = 5
P2 = 6
MASS_FLOW = 7
HEAT_ENERGY = 8


def get_data(file):
    file_open = open(file)
    lines = file_open.readlines()
    file_open.close()
    sample_num = []
    counts = []
    lines = lines[2:]
    series_names = lines[0].split('\t')
    lines = lines[2:]
    data = []
    for line in lines:
        separated_data = line.split('\t')
        line = [float(i) for i in separated_data]
        data.append(line)
    return series_names, data


def split_experiment_b_2_files():
    new_file = open("First Law Data\Lab 2-Part 1b", 'w')
    old_file = open("First Law Data\Lab 2-Part 2b")
    new_file.writelines(old_file.readlines()[:784])
    old_file.close()
    new_file.close()
    new_file = open("First Law Data\Lab 2-Part 2b-generated", 'w')
    old_file = open("First Law Data\Lab 2-Part 2b")
    lines = old_file.readlines()
    new_lines = lines[0:4]
    for line in lines[784:]:
        elements = line.split('\t')
        new_time = round(float(elements[0]) - 78, 1)
        new_lines.append(f"{new_time}\t{elements[1]}\t{elements[2]}\t{elements[3]}\t{elements[4]}\t{elements[5]}\t{elements[6]}\t{elements[7]}\t{elements[8]}")
    new_file.writelines(new_lines)
    new_file.close()


def integrate(element_num, data):
    DT = 0.1
    total = 0
    for datapoint in data[element_num]:
        total += datapoint * DT
    return total


def derive(element_num, data):
    DT = 0.1
    derivative = []
    for i in range(len(data[element_num])-1):
        derivative.append((data[element_num][i+1]-data[element_num][i])/DT)
    return derivative


def convert_to_single_list(data):
    new_data = []
    for x in range(len(data[0])):
        row = []
        for y in range(len(data)):
            row.append(data[y][x])
        new_data.append(row)
    return new_data


def plot(elements_to_plot, series_names, data):
    legends = []
    for element in elements_to_plot:
        plt.plot(data[0], data[element])
        legends.append(series_names[element])

    plt.legend(legends)


def results_filling(file, experiment):
    series, col_data = get_data(file)
    row_data = convert_to_single_list(col_data)
    # plot([T1, T_WALL, T_TOP_PLATE, T_BOT_PLATE], series, row_data)
    plot([P1, MASS_FLOW], series, row_data)
    plt.show()
    print(f"Total Mass Added (Experiment {experiment}): {integrate(MASS_FLOW, row_data)}g")


def results_heating(file, experiment):
    series, col_data = get_data(file)
    row_data = convert_to_single_list(col_data)
    # plot([T1, T_WALL, T_TOP_PLATE, T_BOT_PLATE], series, row_data)
    heater_power = derive(HEAT_ENERGY, row_data)
    #plot([HEAT_ENERGY], series, row_data)
    #plt.plot(row_data[0][:-1], heater_power)
    #plt.legend(["Heat Energy(kJ)", "Heater Power (kW)"])
    #plt.show()
    plot([P1, T1, T_WALL, T_TOP_PLATE, T_BOT_PLATE, HEAT_ENERGY], series, row_data)
    plt.show()
    # print(f"Total Mass Added (Experiment {experiment}): {integrate(MASS_FLOW, row_data)}g")


def show_results_filling():
    results_filling("First Law Data\Lab 2-Part 1a", 'a')
    results_filling("First Law Data\Lab 2-Part 1b", 'b')
    results_filling("First Law Data\Lab 2-Part 1c", 'c')
    results_filling("First Law Data\Lab 2-Part 1d", 'd')


def show_results_heating():
    results_heating("First Law Data\Lab 2-Part 2a", 'a')
    results_heating("First Law Data\Lab 2-Part 2b-generated", 'b')
    results_heating("First Law Data\Lab 2-Part 2c", 'c')
    results_heating("First Law Data\Lab 2-Part 2d", 'd')


show_results_filling()
show_results_heating()
#split_experiment_b_2_files()