########### WORKING WITH .TXT FILES ##########3

file = open ("Countries.txt", "w")
file.write ("Italy\n")
file.write ("Germany\n")
file.write ("Spain\n")
file.close()

file = open ("Countries.txt", "r")
print (file.read())

file = open ("Countries.txt", "a")
file.write ("France\n")
file.close()

