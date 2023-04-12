#############BREAK AND CONTINUE STATEMENTS ##############



counter = 0

while True:
    lineIn = input("place text here:  ")
    if lineIn == 'END':   
        break
    counter = counter+1
    print('line', counter, '=', lineIn)



############################

#######  CONTINUE   STATEMENT ##############


for n in range(10, 16):  
  if (n == 13):  # bad luck
    continue     # so we skip it
  print(n)


for i in range(1, 16):
    if (i == 4):
        continue
    if (i == 9):
        break
    print(i)
print ("\n")
print('Done')
    
