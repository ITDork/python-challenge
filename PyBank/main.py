#make note of the headers in the data file
# Date,Profit/Losses
#setup environment
import os
import csv

#set file path
budgetdata = os.path.join('..','..','PythonResources', 'budget_data.csv')

#declare variables/lists
month = []
gainloss = []
monthchange = []
listi = 0
nextlisti = 1

#pull data from file into lists for month and for gain/loss
with open(budgetdata) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        month.append(row[0])
        gainloss.append(float(row[1]))

#perform calculations on list items and generate alother list
for iRow in range(len(gainloss)-1):
    changecalc = gainloss[nextlisti] - gainloss[listi]
    monthchange.append(float(changecalc))
    nextlisti = nextlisti + 1
    listi = listi + 1

#gather other data as required and create variables with formated output      
monthcount = len(month)
gainlosssum = float(sum(gainloss))
formattedglsum = '${:,.2f}'.format(gainlosssum)
changeaverage = float(sum(monthchange) / len(monthchange))
formattedaverage = '${:,.2f}'.format(changeaverage)
maxgain = max(monthchange)
formattedmaxgain = '${:,.2f}'.format(maxgain)
#pull index location of max change amount, add one and use the 
#index location to find the associated date for both maxgain and maxloss
maxgainindex = monthchange.index(max(monthchange))+1
datemaxgain = month[maxgainindex]
maxloss = min(monthchange)
formattedmaxloss = '${:,.2f}'.format(maxloss)
maxlossindex = monthchange.index(min(monthchange))+1
datemaxloss = month[maxlossindex]

#terminal output
print("")
print("Financial Analysis")
print("_________________________________________")
print("")
print("Total Months: " + str(monthcount))
print("Total Gain/Loss: " + str(formattedglsum))
print("Average Change: " + str(formattedaverage))
print("Greatest Gain occured " + datemaxgain + " totalling " + str(formattedmaxgain))
print("Greatest Loss occured " + datemaxloss + " totalling " + str(formattedmaxloss))
print("")

#files output
f = open("analysis_results.txt","w")
f.write("\n")
f.write("Financial Analysis\n")
f.write("_________________________________________\n")
f.write("\n")
f.write("Total Months: " + str(monthcount) + "\n")
f.write("Total Gain/Loss: " + str(formattedglsum) + "\n")
f.write("Average Change: " + str(formattedaverage) + "\n")
f.write("Greatest Gain occured " + datemaxgain + " totalling " + str(formattedmaxgain) + "\n")
f.write("Greatest Loss occured " + datemaxloss + " totalling " + str(formattedmaxloss) + "\n")
f.write("\n")

f.close()






        
