from line_follower_robot.sensor import get_sensor_data
from line_follower_robot.movement import decide_move

sensors, active = get_sensor_data()

action = decide_move(sensors)

print("Sensor Values:", sensors)
print("Active Sensors:", active)
print("Robot Action:", action)