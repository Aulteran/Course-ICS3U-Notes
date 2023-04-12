# Use a FOR loop to create a 5 x 5 square of ones (hint: use a for loop in a for loop)

length = 5
arr = []

for i in range(length):
    for j in range(length):
        arr.append(1)
    print(arr)
    arr = []
