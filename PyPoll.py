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

# open the election result and read the file 
with open(file_to_load, newline='') as election_data:
   file_reader = csv.reader(election_data, delimiter=',')
   headers = next(file_reader)
   print(headers)


# to do: read and analyze the data here 
# print each row in the
#  CSV file 
 # read and print the header row

# create a filename variable to a direct or indirect path to the file
file_to_save= os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file 
with open(file_to_save, "w") as txt_file:
    
    # write some data to the file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson\n")





