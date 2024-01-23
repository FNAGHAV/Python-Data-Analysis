# Input file path and output file path 
file_path = "../Python-Challenge/PyBank/Resources/budget_data.csv"
text_path = "../Python-Challenge/PyBank/Analysis/Analysis.txt"

# importing library
from math import fsum 
import csv 


# Specifying empty dictionaries and lists for the following loop(s)
dict_date = {} 
lsit_number = [] 
list_pair = {} 
list_date = [] 


# Csv file reading and writing 
with open(file_path, 'r') as file: 
    reader_file = csv.reader(file) 
    Header = next(reader_file) 
 
    with open (text_path, 'w') as Analysis: 
        writer_file = csv.writer(Analysis)     
        
        # for loop through the lines of the csv file
        for line in reader_file: 
         
            date = line[0] 
            pro_lo = int(line[1]) 
            lsit_number.append (pro_lo) 
            list_date.append (date) 
 
            each_date = date.split('-') 
            Month = each_date[0] 
            if Month in dict_date: 
                dict_date [Month] += 1 
 
            else: 
                dict_date [Month] = 1 
 
        # getting the percentage of change in profit/losses         
        list_result = [second - first for first, second in zip(lsit_number, lsit_number[1:])]
        
        
        # finding the max and min of change in profit/losses
        max_increase = max(list_result) 
        min_decrease = min(list_result) 
    
        max_date = [date for date, diff in zip(list_date [1:], list_result) if diff == max_increase][0] 
        min_date = [date for date, diff in zip(list_date[1:], list_result) if diff == min_decrease][0] 
 
        #calculating total Number of Month, Total and Average
        total_Number_of_Month = fsum (dict_date.values ()) 
        total = sum (lsit_number) 
        Total_list= sum (list_result) 
        Average = round(Total_list/len(list_result),2) 
        
        # Writing on the csv file for financial analysis, total months, total,average changes and greatest increase and decrease in profits
        writer_file.writerows([ 
            ['Financial Analysis'], 
            [], 
            ["------------------"], 
            [], 
            [f"Total Months: {total_Number_of_Month:.0f}"], 
            [], 
            [f"Total: ${total}"], 
            [], 
            [f"Average Change: ${Average}"], 
            [], 
            [f"Greatest Increaase In Profits: {max_date} (${max_increase})"], 
            [], 
            [f"Greatest decrease In Profits: {min_date} (${min_decrease})"] 
 
        ]) 

# printing the output in terminal
print(f"Financial Analysis" 
      f"\n\n---------------------" 
      f"\n\nTotal Months: {total_Number_of_Month:.0f}" 
      f"\n\nTotal: ${total}" 
      f"\n\nAverage Difference: ${Average}" 
      f"\n\nGreatest Increase in Profits: {max_date} (${max_increase})" 
      f"\n\nGreatest Decrease in Profits: {min_date} (${min_decrease})")