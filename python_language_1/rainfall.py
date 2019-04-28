import numpy as np
import csv
import json
import matplotlib.pyplot as plt
import time


def rainfall(csv_name):
    with open(csv_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        data = []
        for row in reader:
            data.append(row)

    year_list = np.unique([row[0] for row in data])
    rainfall_dict = {}

    for year in year_list:
        rainfall_mmday_data = []
        for i in range(len(data)):
            if year == data[i][0]:
                rainfall_mmday_data.append(float(data[i][2]))
        rainfall_dict[year] = rainfall_mmday_data

    with open('rainfall.json', 'w') as f:
        json.dump(rainfall_dict, f, indent=4)


def rainfall_plot(json_name, year, colour='b'):
    # optional colour argument with default set to blue
    with open(json_name, 'r') as f:
        data = json.load(f)
    plt.plot(range(1, len(data[year])+1), data[year], colour)
    plt.title('Rainfall time series for {}'.format(year))
    plt.xlabel('Day')
    plt.ylabel('Rainfall (mm)')
    plt.savefig('Rainfall_{}.png'.format(year))


def mean_annual_rainfall_plot(json_name, start_year, end_year):
    with open(json_name, 'r') as f:
        data = json.load(f)
    mean_rainfall = []
    for i in range(int(start_year), int(end_year)+1):
        mean_rainfall.append(np.mean(data[str(i)]))
    plt.plot(range(int(start_year), int(end_year)+1), mean_rainfall)
    plt.title('Mean annual rainfall between {} and {}'.format(start_year,
              end_year))
    plt.xlabel('Year')
    plt.ylabel('Mean rainfall (mm)')
    plt.savefig('Mean_annual_rainfall_{}_to_{}.png'.format(start_year,
                end_year))


def correct_value(rainfall_value):
    corrected_value = rainfall_value*(1.2**np.sqrt(2))
    round_corrected_value = round(corrected_value, 3)
    return round_corrected_value


def apply_correction_loop(json_name, year):
    """ Evaluations:

        Pros:
        
        Cons: 

    """
    with open(json_name, 'r') as f:
        data = json.load(f)
    new_values = []
    for i in range(len(data[year])):
        new_value = correct_value(data[year][i])
        new_values.append(new_value)
    return new_values


def apply_correction_comprehension(json_name, year):
    with open(json_name, 'r') as f:
        data = json.load(f)
    new_values = [correct_value(value) for value in data[year]]
    return new_values


def time_functions(year):
    start = time.time()
    apply_correction_loop('rainfall.json', year)
    end = time.time()
    print('Loop:', end - start)
    start = time.time()
    apply_correction_loop('rainfall.json', year)
    end = time.time()
    print('Comprehension:', end - start)
