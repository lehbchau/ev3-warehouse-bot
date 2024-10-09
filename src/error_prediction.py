import math

# Prompt user for box location
location = input("Enter inventory location (Shelving Unit_Box Number): ")

# Split location string to analyze the final position
characters = []
for char in location:
    characters.append(char)

unitLetter = characters[0]
unitNumber = int(characters[1])  # Convert to integer
boxIndex = int(characters[3])     # Convert to integer
boxColumnDistance = [1, 3, 5, 7, 9, 11]
numberOf90degTurns = 2

# Turning 90 degrees first time to arrive at the target x and y, another time 90 degrees to make the
# front of the robot faces the box to scan barcode. This applies because we plan for our robot to always
# travel to always travel straight to the target y distance before navigating itself again and go to
# the target x position.
X_errorOf1turn90 = 0.125  # How much x is off after 1 90 degree turning
Y_errorOf1turn90 = 0.25  # How much y is off after 1 90 degree turning
SHELF_WIDTH = 12

# Function to calculate the x and y distance of the box location from the bottom left corner position of the shelf
def boxPosition(boxNumber):
    if (boxNumber >= 1 and boxNumber <= 6):
        finalX = initialX + 3 * boxColumnDistance[boxNumber - 1]
        finalY = initialY
    elif (boxNumber > 6 and boxNumber <= 12):
        finalX = initialX + 3 * boxColumnDistance[boxNumber - 7]  # Adjusted indexing for second row
        finalY = initialY + SHELF_WIDTH
    else:
        print("Invalid box number!")
        return None, None  # Return None for invalid box number
    return finalX, finalY

# For the below functions, error values that are considered are the average values taken from our test plan. For distance values that 
# are not in the test cases (for example, 24 inches), we take the average of test cases from 12 to 36 inches and make the result the error.

def predictError1(yBox):  # Error caused by driving straight to the target y only
    xOff, yOff = 0, 0
    if (yBox == 12):  # Shelf A1, B1
        xOff += 0.2125
        yOff += 0.025
    elif (yBox == 24):
        xOff += 0.26875
        yOff += 0.29375
    elif (yBox == 36):
        xOff += 0.325
        yOff += 0.5625  
    elif (yBox == 48):
        xOff += 0.575
        yOff += 0.3625
    elif (yBox == 60):
        xOff += 0.825
        yOff += 0.1625
    elif (yBox == 72):
        xOff += 0.70625
        yOff += 0.275
    elif (yBox == 84):
        xOff += 0.5875
        yOff += 0.3875
    elif (yBox == 96):
        xOff += 0.734375
        yOff += 0.484375
    return xOff, yOff

def predictError2(xBox,xOff,yOff):  # Error caused by driving straight to the target x after turning 90 degrees from the target y
    if (xBox == 12):  # Shelf A1, A2
        xOff += 0.3
        yOff += 0.8625
    elif (xBox == 24):
        xOff += 0.75625
        yOff += 1.075
    elif (xBox == 36):
        xOff += 1.2125
        yOff += 1.2875  
    elif (xBox == 48):
        xOff += 2.0125
        yOff += 2.1875
    elif (xBox == 60):
        xOff += 2.8125
        yOff += 3.0875
    elif (xBox == 72):
        xOff += 3.45
        yOff += 3.975
    elif (xBox == 84):
        xOff += 4.0875
        yOff += 4.8625
    elif (xBox == 96):
        xOff += 6.13125
        yOff += 7.29375
    return xOff, yOff

def predictError3(current_x_off, current_y_off, xBox, yBox):
    # Error caused by the final turning 90 degrees to face the box
    # Calculate actual final position of the robot
    current_x_off += X_errorOf1turn90
    current_y_off += Y_errorOf1turn90
    actual_x = xBox + current_x_off
    actual_y = yBox + current_y_off
    return actual_x, actual_y

# Initialize initialX and initialY
initialX = None
initialY = None

if (unitLetter == 'A' and unitNumber == 1):
    initialX = 12
    initialY = 12
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'A' and unitNumber == 2):
    initialX = 12
    initialY = 36
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'C' and unitNumber == 1):
    initialX = 12
    initialY = 60
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'C' and unitNumber == 2):
    initialX = 12
    initialY = 84
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'B' and unitNumber == 1):
    initialX = 60
    initialY = 12
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'B' and unitNumber == 2):
    initialX = 60
    initialY = 36
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'D' and unitNumber == 1):
    initialX = 60
    initialY = 60
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

elif (unitLetter == 'D' and unitNumber == 1):
    initialX = 60
    initialY = 84
    targetX, targetY = boxPosition(boxIndex)
    X_Error, Y_Error = predictError1(targetY)
    X_Error2, Y_Error2 = predictError2(targetX,X_Error,Y_Error)
    final_X, final_Y = predictError3(X_Error2, Y_Error2, targetX, targetY)

distanceError = math.sqrt((targetX - final_X)**2 + (targetY - final_Y)**2)

# Check if targetX and targetY are defined
if targetX is not None and targetY is not None:
    print("Target X of inventory: ", targetX)
    print("Target Y of inventory: ", targetY)
    print("Actual X the robot stops at: ", final_X)
    print("Actual Y the robot stops at: ", final_Y)
    print("Distance from the target inventory location: {0:.2f} inches".format(distanceError))
else:
    print("Check your inputs!")
