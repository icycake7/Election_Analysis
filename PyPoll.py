# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receive voted
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


# Import the datetime class from the datetime module.
# Add dependencies
#import datetime as dt
import csv
import os

# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()

# Print the present time.
#print("The time right now is", now)


# Assign a variable for the file to load and the path.

#file_to_load = 'Resources/election_results.csv' -- Direct Path Method

file_to_load = os.path.join("Resources", "election_results.csv") # -- Indirect Method
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.

##election_data = open(file_to_load, 'r')
#use with statement instead of open and close functions
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #print(election_data)


    file_reader = csv.reader(election_data)

    #for row in file_reader:
    #    print(row[0])
    headers = next(file_reader)
    #print(headers) 

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2] 
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0  
           # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)





    # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.

        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)



        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        

        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



#print(candidate_votes)
# 3. Print the total votes.
#print(total_votes)   
























##outfile = open(file_to_save, "w")

# Write some data to the file.
##outfile.write("Hello World")

# Close the file.
##election_data.close()
##outfile.close()


##with open(file_to_save, "w") as txt_file:

    #txt_file.write("Arapahoe, ")

    #txt_file.write("Denver, ")

    #txt_file.write("Jefferson ")

    #txt_file.write("Arapahoe, Denver, Jefferson")

    
    #use new line method
    #txt_file.write("Arapahoe\nDenver\nJefferson")




    #skill drill
    ##txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

