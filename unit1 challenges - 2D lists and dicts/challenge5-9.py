# Ch1
# Ch2
# Ch3
# Ch4

# Challenge 5
# Create the following using a 2D
# dictionary showing the sales each
# person has made in the different
# geographical regions: 

salesftw = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
}

# Challenge 6
# Using the program from Question 5, ask the user for a name and a region. 
# Display the relevant data. Ask the user for the name and region of data they 
# want to change and allow them to make the alteration to the sales figure. 
# Display the sales for all regions for the name they choose. 

salesperson = input('enter name of salesperson: ')
region = input('enter the region of sale: ')

print('sales for the data entered is: {0}'.format(salesftw[salesperson][region]))

print('\nenter information for data you wish to change')
salesperson = input('enter name of salesperson: ')
region = input('enter the region of sale: ')
newValue = int(input('what value would you like to set the data to for the information provided?: '))
salesftw[salesperson][region] = newValue

salesperson = input('\nEnter the name of the salesperson you want to view data for: ')
print('Data: ', salesftw[salesperson])

# Challenge 7
# Ask the user to enter the name, age and shoe size for four people. Ask for 
# the name of one of the people in the list and display their age and shoe size.

pplsInfo = [{}, {}, {}, {}]

for i in range(4):
    print('info for person %i'%i)
    pplsInfo[i]['name'] = input('Enter name: ')
    pplsInfo[i]['age'] = input('Enter age: ')
    pplsInfo[i]['shoesize'] = input('Enter shoe size: ')

mfwanted = input('enter name of person info wanted: ')
for ppl in pplsInfo:
    if mfwanted == ppl['name']:
        wantedInfo = ppl
print('info for person {0} is {1}'.format(mfwanted, wantedInfo))

# Challenge 8
# Adapt program in the previous example to display the names and ages of 
# all the people in the list but do not show their shoe size.

for ppl in pplsInfo:
    tempppl = ppl
    tempppl.pop('shoesize')
    print(tempppl)

# Challenge 9
# After gathering the four names, ages and shoe sizes, ask the user to enter 
# the name of the person they want to remove from the list. Delete this row 
# from the data and display the other rows on separate lines.

mftoremove = input('enter name of person to remove data: ')

for ppl in pplsInfo:
    if mftoremove == ppl['name']:
        pplsInfo.pop(pplsInfo.index(ppl))

for i in pplsInfo:
    print(i)
