# Election_Analysis

## Overview of Election Audit:
Tom, a Colorado Board of Elections employee, has asked us to assist him with an election audit of a recent local congressional election in Colorado. After, having successfully counted the total votes that each candidate received, we are now tasked to find out the following:
<br>

1. How many votes were cast in this congressional election?
2. The number of votes and the percentage of total votes for each county in the precinct.
3. Which county had the largest number of votes?
4. The number of votes and the percentage of the total votes each candidate received.
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
<br>
## Resources
Data Source: election_results.csv<br>
Software: Python 3.7, Visual Studio Code 1.70.2
## Election-Audit Results:


### 1. How many votes were cast in this congressional election?</u>
```
Election Results
-------------------------
Total Votes: 369,711
-------------------------
```
* As can be seen above, there were **<u>369,711</u>** total votes cast. <br>This was done by reading the election_results.csv file in Python via the CSV module.
<br>
```
total_votes = 0
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
```
* The above code demonstrates how it is done. Before the csv file is read, a "total_votes" variable is initiated and set to 0. Then, we use a for loop to iterate through all lines within the .csv file. We skip the header row, and start counting.


### 2. Breakdown of the number of votes and the percentage of total votes for each county in the precinct:
```
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
```
* The code above shows us the name of the county, the percentage, and number of votes cast in each county. <br> Let us take a look at the code that helped us calculate these results.<br>
First, we want to create a list that has all the counties from the .csv file. We do not want duplicates, therefore we write the following into our for loop:

```
county = []
county_votes = {}
    [...]
    for row in reader:
    [...]
        county_name = row[1]
        if county_name not in county:
            county.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
```
* The **county** list is created before we read the .csv file. Then we need to append all county names into our list. With the condition however, that the county name does not already exist in the list. This helps us avoid duplicating the same county name.<br>
* Now, all that needs to be done is to add a dictionary that we name **county_votes**, assign the **county** list as key and set the values to 0. After that, we increment the value in the list by one in order to find the individual vote count for each county.
* Finally, since we know the individual vote count, we the vote count by the total vote count and multiply it by 100 to get percentage of total votes for each county. The following code shows how it is done:

```
    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
```
The reason we use floats here over integers is because the percentage will not be displayed otherwise in our output file.


### 3. Which county had the largest number of votes?

```
-------------------------
Largest County Turnout: Denver
-------------------------
```
* The county with the highest turnout was **Denver**. <br>This is done with an if-statement in another for loop that counts the votes for each county. The code below gets the values for each county name in the **county_votes** dictionary, which we then assign to the variable **vote**.
```
    for county_name in county_votes:
        votes = county_votes[county_name]
```
* Then, we write the following if-statement in our for loop to make sure that only the winning county is displayed when we output our code.

```
largest_county = ''
largest_count = 0
[...]
        if (votes > largest_count):
            largest_count = votes
            largest_county = county_name
```
* It is important to note that we initiated the **largest_count** variable and set it to 0 before reading the .csv file. This is done so that the vote count starts at 0 every time the file gets accessed.
* The if-statement basically checks if a county has more votes than another county found in the county_votes dictionary that we created earlier. If yes, the value is stored in the **largest_count** variable. Lastly, we set the **largest_county** variable to the name of the county that has the largest number of votes. In this case <u>Denver</u> is the winner!

### 4. The number of votes and the percentage of the total votes each candidate received.
```
Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)
```
* The above output shows us the candidates name, the percentage of total votes they received, and the number of total votes each candidate got. 

### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
```
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```

* <u>**Diana DeGette**</u> won the election with <u>**73.8%**</u> of the total vote count. She received a total of <u>**272,892**</u> out of the 369,711 votes.


## Election-Audit Summary:

As can be seen above, this script can easily go through huge amounts of data and deliver quick and clean results.

In this case, we were able to determine the winner of the local congressional election in Colorado. While this is a great way to quickly determine the winner, the script could be modified to provide us with greater detail and insight. For example, one could modify the script to return the percentages of votes for each candidate within each precinct.

Another great advantage of using this script is that it can be applied to several different types of elections. Whether the election is local or state wide, this script will quickly create an output file with the results. All we need is a csv file that we can easily import and read. This will save time and money when it comes to auditing elections. There is simply no need to write a script for each individual election. A simple modification here and there and you are all set and done.


Lastly, the scripts output file could be modified to include visualization, i.e., graphs or pie charts.
