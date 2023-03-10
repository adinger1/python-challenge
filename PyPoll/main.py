import csv

election_data = "Resources/election_data.csv"

total_votes = 0
candidate_votes_dict = {}
curr_candidate_name = ""

with open(election_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads the header row
    csv_header = next(csvreader)
    for row in csvreader:
         #increment total_votes with each row. Each row represents 1 vote
        total_votes += 1
        
        curr_candidate_name = row[2]    
        
        #This condition executes if current row candidate is not currently in the dictionary
        if curr_candidate_name not in candidate_votes_dict:
            #Add entry into dictionary. Current row counts as 1 vote toward the candidate
            candidate_votes_dict[curr_candidate_name] = 1
        
        #This condition executes if candidate is already in the dictionary
        else:
            #update candidate's vote count in the dictionary
            candidate_votes_dict[curr_candidate_name] += 1
        
csvfile.close()

#Creating list of results info to use for text file
l1,l2 = "Election Results","-------------------------"
results_text = [l1,l2]

max = 0
winner = ""
percentage = 0

print(l1)
print(l2)
for candidate in candidate_votes_dict.keys():
    percentage = (candidate_votes_dict[candidate] / total_votes) * 100
    #format percentage
    percentage_string = f"{percentage:.3f}%"
    curr_candidate_results = f"{candidate} : {percentage_string} ({candidate_votes_dict[candidate]})"
    
    #prints candidate results to terminal
    print(curr_candidate_results)
    
    #saves string to results list to be used later in text file
    results_text.append(curr_candidate_results)
    
    #Looking for candidate with max number of votes
    if candidate_votes_dict[candidate] > max:
        winner = candidate
        max = candidate_votes_dict[candidate]

print(l2)
results_text.append(l2)
winner_line = "Winner: " + winner    
print(winner_line,'\n',l2)
results_text.append(winner_line)
results_text.append(l2)

#export a text file with the results.
new_text_file_path = 'Analysis/pypoll_results.txt'
with open(new_text_file_path,'w') as txtfile:
    #Writes each line of results_text to the text file
    for line in results_text:
        txtfile.write(line + '\n')
txtfile.close()