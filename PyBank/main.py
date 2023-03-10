import csv

#set up csvreader
file_path = "Resources/budget_data.csv"
counter = 0
net_total = 0
average_change = 0
sum_of_changes = 0
list_of_changes = []
previous = ""
difference = 0
date_of_increase = ""
date_of_decrease = ""
greatest_increase = 0
greatest_decrease = 0
string_to_write = ""
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    #calculate total number of months. I.e. total number of rows
    #Reads each row of data after the header
    for row in csvreader:
        #counter keeps track of row in the data 
        #E.g. Counter = 1 corresponds to 1st row of data in the csv file
        #Counter also equals the number of months counted so far
        counter += 1
        
        #Initialize date values
        if counter == 1:
            date_of_decrease = row[0]
            date_of_increase = row[1]
            
        else:
            difference = int(row[1]) - int(previous[1])
            
             #calculates the sum of all changes. This is needed to calculate the average change later on
            sum_of_changes += difference
            
            list_of_changes.append(difference)
            
            if difference < greatest_decrease:
                date_of_decrease = row[0]
                greatest_decrease = difference
            
            if difference > greatest_increase:
                date_of_increase = row[0]
                greatest_increase = difference
            
        net_total += int(row[1])
        #keeps track of previous row so we can calculate the change between subsequent rows
        previous = row
csvfile.close()
average_change = sum_of_changes / len(list_of_changes)

#print results to terminal
l1 = "Financial Analysis"
l2 = "----------------------------"
l3 = "Total months: " + str(counter)
l4 = "Total: $" + str(net_total)
l5 = f"Average Change: ${average_change:.2f}"
l6 = f"Greatest Increase in Profits: {date_of_increase} (${greatest_increase})"
l7 = f"Greatest Decrease in Profits: {date_of_decrease} (${greatest_decrease})"

results = [l1,l2,l3,l4,l5,l6,l7]

#Prints results to terminal
for line in results:
    print(line)
    
#export a text file with the results.
new_text_file_path = 'Analysis/pybank_results.txt'
with open(new_text_file_path,'w') as txtfile:
    for line in results:
        string_to_write += line + '\n'
    txtfile.write(string_to_write)
txtfile.close()


