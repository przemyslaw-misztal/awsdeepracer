def reward_function(params):

    # Read input parameters.
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    steering_angle = params['steering_angle']

    # Initialise the reward with a small positive value.
    reward = 1e-3

    # Reward based on progress.
    reward += progress

    # Reward for staying on the track.
    if all_wheels_on_track:
        reward += 10.0
    else:
        reward -= 10.0

    # Calculate 3 markers that are at varying distances away from the center line.
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa.
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 1e-3  # likely crashed/close to off track.

    # Reward for maintaining speed.
    reward += speed * 0.2

    # Encourage smooth steering.
    if abs(steering_angle) < 10.0:
        reward += 1.0
    elif abs(steering_angle) < 20.0:
        reward += 0.5
    else:
        reward -= 0.5

    return float(reward)
