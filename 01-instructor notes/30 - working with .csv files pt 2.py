################ WORKING WITH CSV FILES PT2 ##################

# A .csv file cannot be altered, only added to.
# If you need to alter the file you need to  write it to a temporary list.
# This block of code will read the original .csv file and
# write it  to a list called “tmp”.
# This can then be used and altered as a list

import csv

file = list (csv.reader(open("Stars.csv")))  #reads original csv
tmp = []            #newlist tmp

for row in file:
    tmp.append(row)  #write csv to new list called tmp, now can be altered
    #print (tmp)


file = open ("NewStars.csv","w")        #creates new .csv
x = 0
for row in tmp:
    newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
    file.write(newRec)      #uses list tmp writes to new file newRec
    x = x+1
file.close ()






