## Generating a random EEG waveform
We use a model developed by Oxford University’s MRC Brain Networks Dynamics Unit (https://data.mrc.ox.ac.uk/data-set/simulated-eeg-data-generator), with most of the MATLAB code coming from their template.
Our script to generate a 100000-points long signal with 100 random peaks and write it to a CSV is in matlab/eeg_generate.m
It can be easily edited to change the input signal parameters.


## Running the peak extraction program (main.py)

The first thing you need for running this program is a dataset with EEG data. This program requires the data to be stored in a CSV file with signal amplitude (in milivolts) in the first column and corresponding times (in seconds) in the second column. For reference, check out the eeg_data_random.csv file in this repo.
If you do not have your own dataset, a randomly generated dataset containing 100,000 rows is provided in the previously mentioned CSV file.

Next, this program is simply ran in your computer's terminal (python is required to be installed on the machine):

![image](https://github.com/user-attachments/assets/9b7737b8-f93b-4f50-83a3-2e3d5fa5176f)

To interact with the program, simply answer the question's asked by the print-outs in the terminal. Here's a sample run:

![image](https://github.com/user-attachments/assets/72af1c29-26d3-4b9b-b119-7adbd06d12f9)
