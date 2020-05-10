clc 
clear all

disp ('---------------------Q1------------------')
% Import data from Excel spreadsheet

filename = 'Data_Input_Q1.xlsx'; %Excel file name
sheet = 'Sample_Data';%Excel sheet name
xlRange = 'B4:E7' ; %Rectangular range of data to import

data = xlsread(filename,sheet,xlRange);

sample = data(:,1); % sample number
c_value = data(:,2); % certified value
mean_value = data(:,3); % mean value
std_value = data(:,4); % std value

data_size = size(data); %size of matrix data
N = 8; %number of repeat measurements for alloy
n_sample = length(sample);
df = N -1
t_cr = tinv(0.975,df); % 2sided confidence at 95%, risk factor is 195/200

for k=1:n_sample
    t = (mean_value(k) - c_value(k)) * sqrt(N) / std_value(k);
    abs_t = abs(t);
    
    text = sprintf('Sample %d:',sample(k));
    
    disp(text)
    text = sprintf('Critical t(95%%) = %4.3f',t_cr);
    
    disp(text)
    text = sprintf('Statistic t = %4.3f',abs_t);
    disp(text)
    if abs_t > t_cr
 
        text = sprintf('The mean value %4.3f differs significantly  from the certified value %4.3f.', mean_value(k),c_value(k));
        disp(text);
        disp(' ');
        
    else
        text = sprintf('The mean value %4.3f does not differ significantly  from the certified value %4.3f.', mean_value(k),c_value(k));
        disp(text);
        disp(' ');
    end
end