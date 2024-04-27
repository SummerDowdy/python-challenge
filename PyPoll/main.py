# import modules
import csv
import os

# load the file to read data
inputFile = os.path.join(".","Resources", "election_data.csv")

# out the file location for election results
outputFile = os.path.join(".", "Analysis", "Election Results.txt")

# variables
totalVotes = 0 # variable that hold the total number of votes
candidates = [] # list the hold the candidates who received votes
candidateVotes = {} # dictionary that contains the total number of votes each candidate won
winningCount = 0 # variable that holds the winning count
winningCandidate = "" # variable for the winning candidate

# read the csv file
with open(inputFile) as electionData:
    # create the csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot ID
        # index 1 is the county
        # index 2 is the candidate
            
    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1

        # check to see if candidate is in list of candidates
        if row[2] not in candidates:
            # if the candidate is not in the list, add them to the list
            candidates.append(row[2])

            # add the value to the dictionary as well
            # { "key": value }
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1

        else:
            # the candidate is in the list of candidates
            # add a vote to the candidate's count
            candidateVotes[row[2]] += 1

# print(candidateVotes)
voteOutput = ""

for candidate in candidateVotes:
    # get the vote count and percentage of the votes
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) /float(totalVotes)) * 100.00
    voteOutput += f"{candidate}: {votePct:.3f}% ({votes}) \n"
    
    # compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winnin count
        winningCount = votes
        # update the winning candidate
        winningCandidate = candidate

winningCandidateOutput = f"Winner: {winningCandidate} \n"

# create an output varialbe to hold the output
output = (
    f"\n\nElection Results\n"
    f"\n--------------------------\n"
    f"\nTotal Votes = {totalVotes:,}\n"
    f"\n--------------------------\n"
    f"\n{voteOutput}"
    f"\n--------------------------\n"
    f"\n{winningCandidateOutput} \n"
)

# displays the output in terminal
print(output)

# print the results and export the data to a text file
with open(outputFile, "w") as textFile:
    # write the output to the text file
    textFile.write(output)