import csv

def csv_to_list(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append((float(row[0]), float(row[1])))
    return data

eeg_data_list = csv_to_list('eeg_data_random.csv')

# First column: time [s], second: amplitude [V]
print(eeg_data_list[0])