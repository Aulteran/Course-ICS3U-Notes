#You are in a bike race which goes up and down a hill. There are 4 predefined distances for you;

uphill_distance = 13 #km
downhill_distance = 20 #km
uphill_time = 14 #mins
downhill_time = 16.3 #mins

#Write a program that will print out your average speed (in km/min) for the entire race.

#finds the speed per minute uphill and downhill
totalDistance = uphill_distance+downhill_distance
totalTime = uphill_time+downhill_time

#finds total avg speed
avgSpeed_TOTAL = ((totalDistance/totalTime))

print("------------[Assignment 2]------------")
print("Average Speed: %fkm/min" % avgSpeed_TOTAL)
print("--------------------------------------")
