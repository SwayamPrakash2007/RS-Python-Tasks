# Detection data
detections = [
    {"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
    {"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
    {"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
    {"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
    {"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
]

# Filter valid human detections
valid = list(filter(
    lambda x: x["object"] == "human" and
              x["mode"] == "camera" and
              x["confidence"] > 85,
    detections))

# Extract distances
distances = list(map(lambda x: x["distance"], valid))

# Function for alert
def check_distance(d):
    if d < 1:
        print("ALERT: Human very close!")
    else:
        print("Human detected at safe distance")

# Output
print("Valid Human Detections:")
print(valid)

print("Distances:")
print(distances)

# Check each distance
for d in distances:
    check_distance(d)