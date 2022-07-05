# import os module for file pathing
import os

# import the csv module for us to handle .csv files
import csv
from tkinter import W

# create path to csv file
filePath = os.path.join("./", "Resources", "election_data.csv")

#create a output file to export results to:
outputFile = os.path.join("./", "Analysis", "PyPollResults.txt")

"""print("filePath generated: " + filePath)
# = "Resources\election_data.csv"""

"""print(filePath)"""


candidates = [] # Candidate list variable
candidateVotes = {} # Vote talley per candidate as a dictionary
winnerVoteCount = 0 #variable to store winner by popular vote count
winnerCandidate = "" #Variable to store winning candidate


# Open the csv file from path
with open(filePath, 'r', encoding="utf-8") as csvfile:

    # read file
    csvReader = csv.reader(csvfile, delimiter=",")

    # Skip Header
    csvheader = next(csvReader)

    #variable to store total vote count
    totalVoteCount = 0

    # Checking for unique candidates in the list and appending list and dictionary
    for row in (csvReader):
        totalVoteCount += 1
        if row[2] not in candidates:
            candidates.append(str(row[2]))
            
            candidateVotes[row[2]] = 1

        else:
            candidateVotes[row[2]] += 1

cVoteOutput =""

#determine percentage of votes for each candidate
for candidates in candidateVotes:
   cVotes = candidateVotes.get(candidates) 
   cVotePct = (float(cVotes) /float(totalVoteCount)) * 100.00

   cVoteOutput += f"\t{candidates}: {cVotePct: .2f}%: {cVotes}\n"
   if cVotes > winnerVoteCount:
    winnerVoteCount = cVotes
    winnerCandidate = candidates
    
winnerCandidateOutput = f"Winner: {winnerCandidate}\n--------------------------------------------------"
   #print(cVoteOutput)

#Create a variable to hold output file

output = (

    f"\n\nElection Results\n"
    f"--------------------------------------------------\n"
    f"\tTotal Votes : {totalVoteCount:,} \n"
    f"--------------------------------------------------\n"
    f"{cVoteOutput}\n"
    f"--------------------------------------------------\n"
    f"{winnerCandidateOutput}\n"
)        

print(output)


with open(outputFile, 'w') as textFile:
    #Write output data to the text file
    textFile.write(output)
    



