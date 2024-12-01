clear all; close all; clc
% Generate the baseline noise for the entire waveform
mynoise = noise(100000, 1, 100);
% Signal length: 100000 points

% Generate 100 random peak locations across the waveform
peaks = zeros(1, 100000);
a = 1;
b = 100000;
r = (b-a).*rand(100,1) + a;

% Generate the peaks for these locations 
for i = 1:length(r)
    peaks = peaks + peak(100000, 1, 100, 5, r(i));
end

% Combine the noise and peaks into one signal
mysignal = 3 * peaks + mynoise; 
% Add a time column such that the data is amplitude vs. time
mysignal_time = zeros(2,100000);
mysignal_time(1,:) = 0:1/100:1000-1/100;
mysignal_time(2,:) = mysignal;
plot(mysignal);
title("Random EEG signal")
% Write the data to a csv file to be used in the Python program
csvwrite("eeg_data_random.csv", mysignal_time');

