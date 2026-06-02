# sensor.py

def get_sensor_data():
    data = input("Enter 6 sensor values (example 001100): ")

    sensors = list(map(int, data))

    active = len(list(filter(lambda x: x == 1, sensors)))

    return sensors, active