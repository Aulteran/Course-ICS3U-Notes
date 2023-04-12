############## 2D LISTS ####################

grades = [[45,37,54],[62,58,59],[49,47,60],[78,83,62]]

print (grades[0][1])

# WE DON'T HAVE TO USE THE GENERIC COLUMN CODES

grades2 = [{"Ma":45,"En":37,"Fr":54},{"Ma":62,"En":58,"Fr":59},
          {"Ma":49,"En":47,"Fr":60},{"Ma":78,"En":83,"Fr":62}]

print (grades2[1]["En"])

# LETS GO EVEN FURTHER WITH OUR EXAMPLE AND NAME THE ROWS

grades3 = {"Susan":{"Ma":45,"En":37,"Fr":54},
            "Peter":{"Ma":62,"En":58,"Fr":59},
            "Mark":{"Ma":49,"En":47,"Fr":60},
            "Andy":{"Ma":78,"En":83,"Fr":62}}

print (grades3["Mark"]["En"])

