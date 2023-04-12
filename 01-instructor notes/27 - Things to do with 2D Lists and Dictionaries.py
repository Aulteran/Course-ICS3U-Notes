##### THINGS TO DO WITH 2D LISTS #######

### CREATE THE FOLLOWING ARRAY ###

#           0   1   2   
#       0   2   5   8
#       1   3   7   4
#       2   1   6   9

# CREATE THE ARRAY

simple_array = [[2,5,8],[3,7,4],[1,6,9]]

print (simple_array)

print (simple_array[1])     #PRINTS ROW 1

print (simple_array[2][1])  #PRINTS ROW 2, COL 1

simple_array[1][1] = 6      #CHANGES VALUE OF ROW1, COL1 TO 6
print (simple_array)


### CREATE THE FOLLOWING ARRAY ###

#               X   Y   Z
#       A       54  82  91
#       B       75  29  80


# CREATE the DICTIONARY

data_set = {"A":{"X":54,"Y":82,"Z":91},"B":{"X":75,"Y":29,"Z":80}}

print (data_set["A"])

print (data_set["B"]['Y'])

for i in data_set:
    print(data_set[i]["Y"])

data_set["B"]['Y'] = 50

print (data_set)





