#make note of data fields
#Voter ID,County,Candidate
#setup environment
import os
import csv

#set file path
votedata = os.path.join('..','..','PythonResources', 'election_data.csv')

#declare variables/lists
allcandidatevotes = []
uniquecandidates = []
cankey = []
canvotes = []
maxvotes = 0
cannum = 0
votenum = 0
voterids = []
totalvotes = 0

#pull data from file into lists for candidates and voter IDs
with open(votedata) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        allcandidatevotes.append(row[2])
        voterids.append(row[0])
#check votes for voter fraud - count of all votes should match count of unique voter IDs
setvoterids = set(voterids)
voteridcheck = list(setvoterids)
if len(voterids) == len(voteridcheck):
    fraud = "Passed"
else:
        fraud = "Failed"
#create list of unique candidate names    
setcandidates = set(allcandidatevotes)
uniquecandidates = list(setcandidates)
#assign value for total votes based on the length of the list of all candidate votes
totalvotes = len(allcandidatevotes)

#create key values in a list based on number of candidates
for c in uniquecandidates:
    cankey.append(str(cannum))
    cannum = cannum + 1

#zip cankey and uniquecandidates into a dictionary in order to iterate through the list
#and use variables to calculate the stats for the candidates in a for loop
candict = {key:value for key, value in zip(cankey, uniquecandidates)}

for c in candict:
    canvotes.append(str(candict[c]).rjust(11,' ') + ": " + 
    str(allcandidatevotes.count(candict[c])).rjust(10,' ') + "  " +
    str(round((float(allcandidatevotes.count(candict[c]))/float(totalvotes))*100,2)).rjust(6,' ') + "%")
    if maxvotes < allcandidatevotes.count(candict[c]):
        maxvotes = allcandidatevotes.count(candict[c])
        winner = candict[c]
    else: 
        winner = winner

print("")
print("") 
print("Fraud check: " + str(fraud))
print("")
print("Election Results:")
print("---------------------------------")
print("Total Votes: " + str(totalvotes))
print("---------------------------------")
print("   Candidate      Votes  Percent")
print("---------------------------------")
for can in canvotes:
    print(str(can).rjust(30,' '))
print("---------------------------------")
print("     Winner: " + str(winner))
print("---------------------------------")
print("")

#files output
f = open("election_results.txt","w")
f.write("\n")
f.write("Fraud check: " + str(fraud) + "\n") 
f.write("\n")    
f.write("Election Results:\n")
f.write("---------------------------------\n")
f.write("Total Votes: " + str(totalvotes) + "\n")
f.write("---------------------------------\n")
f.write("   Candidate      Votes  Percent\n")
f.write("---------------------------------\n")
for can in canvotes:
    f.write(str(can).rjust(30,' ') + "\n")
f.write("---------------------------------\n")
f.write("     Winner: " + str(winner) + "\n")
f.write("---------------------------------\n")
f.write("\n")
f.close()