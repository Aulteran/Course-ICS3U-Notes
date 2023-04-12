# Feb 17 2023
# Assignment
# Create a program that allows for checking trig functions answers.
# The Program must:
#  have a menu
#  ask if looking to solve angle or side
#  solve the answer(right angle only)
#  the whole program should loop

import math as trig

# gets int/float inputs without error
def numQuery(prompt):
    try:
        return float(input(prompt))
    except(ValueError):
        print("invalid input")

def getData(mode):
    # checks for side lengths available
    print("\nWhat are the side lengths you have available?")
    print("If you don't have one of the lengths asked for - respond with \"0\"")
    if mode:
        second_angle = numQuery("Do you have the other angle in the triangle?(NOT 90degrees): ")
    elif not mode:
        second_angle = numQuery("Do you have an angle in the triangle?(NOT 90degrees): ")
    opposite = numQuery("What is the measure of the side opposite?: ")
    adjacent = numQuery("What is the measure of the side adjacent?: ")
    hypotenuse = numQuery("What is the measure of the hypotenuse?: ")

    # returns dict with all inputs
    return {
    "opposite": opposite,
    "adjacent": adjacent,
    "hypotenuse": hypotenuse,
    "second_angle": second_angle
    }

    # raise NotImplementedError #DISREGARD

def solveAngle():
    # gets user data
    data = getData(True)
    hyp = data['hypotenuse']
    adj = data['adjacent']
    opp = data['opposite']

    # checks if can use basic addition
    # if data["second_angle"] > 0 and data['second_angle'] < 90:
    #     angle = 180 - (data['second_angle'] + 90)
    # checks if enough data/sides available
    if (adj == 0 and hyp == 0) or (hyp == 0 and opp == 0) or (opp == 0 and adj == 0):
        print("You don't have enough side lengths.") 
        return 
    # finds angle depending on data available
    elif hyp == 0:
        angle = trig.atan(opp/adj)
    elif adj == 0:
        angle = trig.asin(opp/hyp)
    elif opp == 0:
        angle = trig.acos(adj/hyp)
    # if all sides available, use inverse tangent by default
    else:
        angle = trig.atan(opp/adj)
    
    # converts to degrees and returns
    return trig.degrees(angle)
    
    # raise NotImplementedError #DISREGARD

def solveSide():
    # gets user data
    solveFor = input("What side should I solve for?[hyp, opp, adj]: ")
    sidesAvail = numQuery("""
    What data do you have available?
    1) hypotenuse and angle
    2) opposite and angle
    3) adjacent and angle
    4) Two sides
    """)

    data = getData(False)
    hyp = data['hypotenuse']
    adj = data['adjacent']
    opp = data['opposite']
    angle = trig.radians(data["second_angle"])
    

    # angle = trig.radians(data["second_angle"])

    # # if (hyp > 0 and adj > 0) or (adj > 0 and opp > 0) or (opp > 0 and hyp > 0):
    # #     pass

    # if solveFor == 'hyp' and adj == 0:
    #     side = hyp * trig.sin(angle)
    # elif solveFor == 'adj' and opp == 0:
    #     pass

    if sidesAvail == 1: # if you have hyp and angle
        opp = hyp * trig.sin(angle)
        adj = hyp * trig.cos(angle)
    elif sidesAvail == 2: # if you have opposite and angle
        adj = opp / trig.tan(angle)
        hyp = opp / trig.sin(angle)
    elif sidesAvail == 3: # if you have adjacent and angle
        hyp = adj / trig.cos(angle)
        opp = adj * trig.tan(angle)
    print("the hypotenuse is: %f\nthe opposite is: %f\nthe adjacent is: %f\nthe angle is %f" %(float(hyp), float(opp), float(adj), float(trig.degrees(angle))))

    if sidesAvail == 4:

        if ((hyp == 0) and (opp == 0)) or ((opp == 0) and (adj == 0)) or ((adj == 0) and (hyp == 0)):
            print("You don't have enough side lengths.")
            return
        if (hyp < opp or hyp < adj) and hyp != 0:
            print("The hypontenuse cannot be smaller than another side!")
            return
        if solveFor == 'hyp':
            side = trig.sqrt(adj**2 + opp**2)
        elif solveFor == 'adj':
            side = trig.sqrt(hyp**2 - opp**2)
        elif solveFor == 'opp':
            side = trig.sqrt(hyp**2 - adj**2)
        else:
            print("You didn't enter a valid side.")
        
        return side

    # raise NotImplementedError #DISREGARD

# Global Loop
while True:
    menu = '''

----[Welcome to TrigWizard]----

Please select an option[1 or 2]:

1) Solve for angle
2) Solve for side length
Select Option: '''

    option = 0
    while option < 1 or option > 2:
        option = numQuery(menu)
        
        # if str(option).isnumeric() != True:
        #     break

        if option == 1:
            angle = solveAngle()
            print("The angle is ", angle)
        elif option == 2:
            solveSide()
        else:
            print("invalid option")

    