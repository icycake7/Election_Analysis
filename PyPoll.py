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


with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #print(election_data)


    file_reader = csv.reader(election_data)

    #for row in file_reader:
    #    print(row[0])
    headers = next(file_reader)
    print(headers) 



























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

