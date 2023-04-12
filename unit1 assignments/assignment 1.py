# bridge weights
weights = {
	'a' : 0,
	'b' : 0,
	'c' : 0,
	'd' : 0,
	'e' : 0
}

#max weight per route
route1MaxWeight = min(weights['a'], weights['b'], weights['c'])
route2MaxWeight = min(weights['d'], weights['e'])

# check which route can carry more weight
def highWeightRoute(route1, route2):
	return max(route1, route2)

print("the max weight you can carry between the two cites is %i" % highWeightRoute(route1MaxWeight, route2MaxWeight))
