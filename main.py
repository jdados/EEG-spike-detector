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
    menu_message = "    1. Load a dataset\n    2. Detect peaks using python list\n    3. Detect peaks using heap\n    4. Save results\n    5. Exit\n"
    eeg_data_loaded = False
    eeg_data_filename = ''
    eeg_data_list = ''
    eeg_data_heap = ''
    output = []
    

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
            # Use the randomly generated data if user doesn't load their own
            if not eeg_data_loaded:
                eeg_data_filename = 'eeg_data_random.csv'
                eeg_data_list = csv_to_list('eeg_data_random.csv')
                eeg_data_heap = csv_to_heap('eeg_data_random.csv')
                eeg_data_loaded = True
            
            # Extract n peaks 
            n = input("Enter how many peaks the program should extract: ")
            print(f"The following peaks are detected in {eeg_data_filename}:")
            temp = eeg_data_list[:]
            output.clear()
            for i in range(int(n)):
                peak = max(temp, key=lambda x: x[1])
                temp.remove(peak)
                print(f'{peak}')
                output.append(peak)
            print()

        elif menu_selection == '3':
            # Use the randomly generated data if user doesn't load their own
            if not eeg_data_loaded:
                eeg_data_filename = 'eeg_data_random.csv'
                eeg_data_list = csv_to_list('eeg_data_random.csv')
                eeg_data_heap = csv_to_heap('eeg_data_random.csv')
                eeg_data_loaded = True
            
            # Extract n peaks 
            n = input("Enter how many peaks the program should extract: ")
            print(f"The following peaks are detected in {eeg_data_filename}:")
            output.clear()
            for i in range(int(n)):
                peak = eeg_data_heap.extract_max()
                print(f'{peak}')
                output.append(peak)
            print()


        elif menu_selection == '4':
            # Saves anything in the output list to a simple txt file 
            if not output:
                print("Error: nothing to save.\n")
            else:
                try:
                    with open("results.txt", 'w') as output_file:
                        output_file.write("Detected peaks:\n")
                        for i in output:
                            output_file.write(f"Time: {i[0]:.4f}, Amplitude: {i[1]:.3f}\n")
                    print("Results saved to results.txt\n")
                except:
                    print("Error: something went wrong.")

        elif menu_selection == '5' or menu_selection.lower() == 'exit':
            break

        else:
            print('Error, please try again.\n')