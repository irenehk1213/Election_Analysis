 # The data we need to retrieve: 
#1. The total number of votes cast 
#2. A complete list of candidates who received votes
#3. The % of votes each candidate won 
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

import os 
import csv 

# assign a variable for the file to load and the path 
file_to_load= os.path.join("Resources/election_results.csv")
# create a filename variable to a direct or indirect path to the file
file_to_save= os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file 
with open(file_to_save, "w") as txt_file:
    
    # write some data to the file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson\n")

#1. initialize a total vote counter 
total_votes = 0

# candidate options
candidate_options = []
# 1. declare the empty dictionary
candidate_votes = {} 
# winning Candidate and Winning count tracker 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# open the election result and read the file 
with open(file_to_load, newline='') as election_data:
   file_reader = csv.reader(election_data, delimiter=',')

   # read and print the header row
   headers = next(file_reader)

   # print each row in the CSV file
   for row in file_reader:

#2. add to the total vote count
        total_votes += 1 

# print the candidate name from each row 
        candidate_name = row[2]

# if the candidate does not match any existing candidate..
        if candidate_name not in candidate_options: 
    # add it to the candidate list
            candidate_options.append(candidate_name)
    # begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
    # add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

# Determine the % of votes for each candidate by looping thru
# 1. iterate thru the canddiate list
for candidate in candidate_votes: 
    #2. retrieve vote count of a candidate 
    votes = candidate_votes[candidate]
    #3. calculate the % of votes 
    vote_percentage = float(votes) / float(total_votes) * 100 
    #4. print the candidate name and % of votes 


# Determine winning vote count and candidate
# 1. determine if the votes are greaer than the winning count 
    if (votes > winning_count) and (vote_percentage > winning_percentage): 
    #2. if true, then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
    #3. set the winning_candidate equal to the candidate's name
        winning_candidate = candidate 

    print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")

print(winning_candidate_summary) 







