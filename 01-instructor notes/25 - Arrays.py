from array import *

nums = array ('i',[45,324,654,45,264])
print (nums)

for x in nums:          #PRINTS EACH NUMBER IN A SEPARATE LINE
    print (x)

new_value = int(input("Input a new number:  "))

#APPENDS A NEW VALUE TO THE ARRAY
nums.append(new_value)
print(nums)

#SORTS THE NUMBERS ASCENDING
nums4 = sorted(nums)
print (nums4)

#REMOVES THE LAST NUMBER IN ARRAY
nums4 = nums4.pop()
print (nums4)

#REVERSES THE ORDER TO THE ARRAY
nums.reverse()
print (nums)


####AN ACTIVITY####

### CREATE A NEW ARRAY, ASKING THE USER HOW MANY NUMBERS THEY WANT
### TO INPUT. THEN APPENDS ALL THE ITEMS TO THE ARRAY
### AFTER ALL THE ITEMS HAVE BEEN ADDED IT WILL JOIN
### THE NEW ARRAY AND THE NUMS ARRAY

new_array = array('i',[])

more = int(input('how many items to input:  '))

for y in range (0,more):
    new_val = int(input('Enter a number:  '))
    new_array.append(new_val)
nums.extend(new_array)

print (nums)

#DELETES THE FIRST OCCURENCE OF THE ITEM IN THE ARRAY

get_rid = int(input('enter item index:  '))

nums.remove(get_rid)

print(nums)

print(nums.count(45)) #TIMES THE NUMBER OCCURS IN THE ARRAY

