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
# county options
county_options = []
# 1. declare the empty dictionary
county_votes = {}
# largest county turnout tracker
winning_county =""
winning_count = 0
winning_percentage = 0
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

# print the county name from each row
        county_name = row[1]

# if the county does not match any existing county..
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

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

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    county_votes_result = "\nCounty Votes:\n"
    print(county_votes_result)
    txt_file.write(county_votes_result)

    # Determine the % of votes for each county by looping thru
    # 1. iterate thru the county list
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100

    # 1. determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_county = county

        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)


    winning_count =0
    winning_percentage=0
    # Determine the % of votes for each candidate by looping thru
    # 1. iterate thru the canddiate list
    for candidate in candidate_votes:
        #2. retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        #3. calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # 1. determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. if true, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        #3. set the winning_candidate equal to the candidate's name
            winning_candidate = candidate

    winning_county_summary = (
        f"\n--------------------------\n"
        f"Largest County Turnout: {winning_county}\n")

    print(winning_county_summary)
    txt_file.write(winning_county_summary)

    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
