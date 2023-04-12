############USING STATISTICS MODULE ########

import statistics

nums = []

print ("you will be entering 5 five numbers")

for i in range (0,5):
    x = int(input("Enter a number:  "))
    nums.append(x)
print (nums)

#mean - average
print(statistics.mean(nums))

# median - middle number
print(statistics.median(nums))

# mode - most common number
print(statistics.mode(nums))


