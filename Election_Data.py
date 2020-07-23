import csv
with open("C:/Hany/Data Analyst Course/paython/Python-Challenge/election_data.csv", newline="") as csvfile:
    budgetdata_reader = csv.reader(csvfile, delimiter=',')
    next(budgetdata_reader)

    voted =[]
    Khan = []
    Correy = []
    Li = []
    O_Tooley = []

    for row in budgetdata_reader:
        voted.append(row[2])
        count=(len((voted)))

        if (row[2]) ==("Khan"):
            Khan.append([2])
            Khan_Votes=(len(Khan))
            Khanvotes = round((((Khan_Votes) / (count))*100), 3)

        elif (row[2]) ==("Correy"):
            Correy.append([2])
            Corry_Votes=(len((Correy)))
            Corryvotes = round((((Corry_Votes) / (count))*100), 3)

        elif (row[2]) ==("Li"):
            Li.append([2])
            Li_Votes=(len((Li)))
            Livotes = round((((Li_Votes) / (count))*100), 3)

        else:
            O_Tooley.append([2])
            O_Tooley_Votes=(len((O_Tooley)))
            O_Torryvotes = round((((O_Tooley_Votes) / (count))*100), 3)
Win_List = {"Khan":Khanvotes, "Correy":Corryvotes, "Li":Livotes, "O'Tooley":O_Torryvotes}
key1 = max(Win_List)
key2 = max(Win_List, key = lambda k: Win_List[k])
Winner = (key2)

with open('C:/Hany/Data Analyst Course/paython/Python-Challenge/Analysis/Elction_Data.txt', 'w') as h:
        h.write("Elction Data Analysis\n")
        h.write("Election Results\n")
        h.write("-------------------------\n")
        h.write("Total Votes: " + str(count)+ "\n")
        h.write("-------------------------\n\n")
        h.write("Khan: " + str(Khanvotes) + "% " + "(" + str(Khan_Votes) + ")" + "\n")
        h.write("Correy: " + str(Corryvotes) + "% " + "(" + str(Corry_Votes) + ")" + "\n")
        h.write("Li: " + str(Livotes) + "% " + "(" + str(Li_Votes) + ")" + "\n")
        h.write("O'Torry: " + str(O_Torryvotes) + "% " + "(" + str(O_Tooley_Votes) + ")" + "\n\n")
        h.write("-------------------------\n")
        h.write("Winner:  " + (str(Winner)) + "\n")
        h.write("-------------------------\n")
