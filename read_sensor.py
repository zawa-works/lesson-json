import json

with open('data/sensor.json', 'r', encoding="utf-8_sig") as f:
    df = json.load(f)

    sensor_data = df['sensordata']

    print('---accel---')
    accel_data = sensor_data['accel']
    print(accel_data['x'], accel_data['y'], accel_data['z'])
    print()

    print('---light---')
    light = sensor_data['light']['light']
    print(light)
    print()

    print('---touch---')
    touch_data = sensor_data['touch']
    for touch in touch_data:
        print(touch['x'], touch['y'])
    print()

    print('---timestamp---')
    timestamp = df['timestamp']
    print(timestamp)
