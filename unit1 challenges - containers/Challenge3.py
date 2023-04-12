# Create a dictionary that contains different attributes about you: 
# height, favorite color, favorite author, etc.

attributesOfMe = {
    'height': 175,
    'favorite color': 'green',
    'favorite author': 'jk rowling'
}

for attribute in attributesOfMe:
    print ("The value of your %s is %s." % (attribute, str(attributesOfMe[attribute])))