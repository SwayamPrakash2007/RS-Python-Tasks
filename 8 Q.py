# Given joint angles
angles = [30, -15, 45, 200, 60, 90]

# Function to check valid angles
def valid(x):
    return 0 <= x <= 180

# Function to convert to servo command
def servo(x):
    return x * 10

# Using filter()
valid_angles = list(filter(valid, angles))

# Using map()
servo_commands = list(map(servo, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)