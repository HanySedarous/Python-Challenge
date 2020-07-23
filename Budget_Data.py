import csv
with open('C:/Hany/Data Analyst Course/paython/Python-Challenge/budget_data.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)

    total = 0
    month = []
    loses = []
    earns = []
    biggest_month =""
    lowest_month =""
    highest_earm=0
    lowest_lost=0

    for row in spamreader:
        total = total + int(row[1])
        month.append(row[0])

        if 0 > int(row[1]):
            loses.append(int(row[1]))
        else:
            earns.append(int(row[1]))

        if float(row[1]) > highest_earm:
            highest_earm = float(row[1])
            biggest_month = row[0]

        if float(row[1]) < lowest_lost:
            lowest_lost = float(row[1])
            lowest_month = row[0]
        #print(float(row[1]) )
    total_month = (len((month)))
    avg = total/total_month
    with open('C:/Hany/Data Analyst Course/paython/Python-Challenge/Analysis/Financial_Analysis.txt','w') as f:
        f.write("Budget Data\n")
        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write("Total Months: "+ str(total_month)+"\n")
        f.write("Total: $"+ str(total)+"\n")
        f.write("Average Change: $"+ str(avg)+"\n")
        f.write("Greatest Increase in Profits: "+biggest_month+" ($"+
str(highest_earm)+")\n")
        f.write("Greatest Decrease in Profits: "+lowest_month+" ($"+
str(lowest_lost)+")\n")
        f.write("```\n")