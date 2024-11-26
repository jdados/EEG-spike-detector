import csv
import heap as hp

def csv_to_list(file_name):
    l = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            l.append((float(row[0]), float(row[1])))
    return l

def csv_to_heap(file_name):
    heap = hp.max_heap()
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            heap.insert_data_point(float(row[0]), float(row[1]))
    return heap

if __name__ == "__main__":
    # load the EEG data into a list and into a heap
    eeg_data_list = csv_to_list('eeg_data_random.csv')
    eeg_data_heap = csv_to_heap('eeg_data_random.csv')

    # ask the user how many peaks need to be found

    # print out the peaks and the times when they occured