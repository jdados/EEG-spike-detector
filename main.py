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
    # Terminal UI variables
    welcome_message = "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n*                                           *\n*    ---      EEG Analyzer      ---         *\n*                                           *\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    menu_message = "    1. Load a dataset\n    2. Search for a repeating signal\n    3. Detect peaks\n    4. Save results\n    5. Exit\n"
    eeg_data_loaded = False
    eeg_data_filename = ''
    eeg_data_list = ''
    eeg_data_heap = ''
    

    print(welcome_message)

    # Terminal UI loop 
    while True:
        print(menu_message)
        menu_selection = input()

        if menu_selection == '1':
            # Collect file name
            eeg_data_filename = input('Enter .csv file name: ')
            eeg_data_loaded = False 
            if not '.' in eeg_data_filename:
                eeg_data_filename += '.csv'
            # Error handling  
            try:
                eeg_data_list = csv_to_list(eeg_data_filename)
                eeg_data_heap = csv_to_heap(eeg_data_filename)
            except:
                print("File not found or not in .csv format.\n")
                continue
            # File will now be used for next commands
            eeg_data_loaded = True
            print("Success.\n")

        elif menu_selection == '2':
            pass
            # TODO, maybe this won't even be in our project

        elif menu_selection == '3':
            # Use the randomly generated data if user doesn't load their own
            if not eeg_data_loaded:
                eeg_data_filename = 'eeg_data_random.csv'
                eeg_data_list = csv_to_list('eeg_data_random.csv')
                eeg_data_heap = csv_to_heap('eeg_data_random.csv')
                eeg_data_loaded = True
            
             # Get and print peak 
            peak = eeg_data_heap.extract_max()
            print(f'The following peak is detected in {eeg_data_filename}:\n{peak}\n')


        elif menu_selection == '4':
            pass
            # TODO, will just save whatever to a txt file probaly

        elif menu_selection == '5' or menu_selection.lower() == 'exit':
            break

        else:
            print('Error, please try again.\n')