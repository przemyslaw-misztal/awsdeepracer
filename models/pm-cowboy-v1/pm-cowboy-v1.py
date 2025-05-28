import math

def reward_function(params):
    '''
    Reward function for AWS DeepRacer
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    steps = params['steps']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steering_angle = params['steering_angle']

    # Initialize reward
    reward = 1e-3  # Use a very small reward by default

    # Reward if the car is on the track
    if all_wheels_on_track:
        reward = 1.0
    else:
        return reward

    # Reward for staying close to the center line
    track_width_half = track_width / 2.0
    distance_from_center_ratio = distance_from_center / track_width_half

    if distance_from_center_ratio <= 0.1:
        reward += 1.0
    elif distance_from_center_ratio <= 0.25:
        reward += 0.5
    elif distance_from_center_ratio <= 0.5:
        reward += 0.1

    # Penalize if the car is off the track
    if is_offtrack:
        reward = 1e-3
        return reward

    # Reward for progress
    reward += progress / 100.0

    # Reward for speed
    SPEED_THRESHOLD = 1.75  # Define a speed threshold
    if speed > SPEED_THRESHOLD and all_wheels_on_track:
        reward += 2.0
    elif speed > SPEED_THRESHOLD:
        reward+=1.0
    else:
        reward += 0.5

    # Calculate the direction of the center line based on the closest waypoints
    next_waypoint = waypoints[closest_waypoints[1]]
    prev_waypoint = waypoints[closest_waypoints[0]]

    track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize if the direction difference is too large
    DIRECTION_THRESHOLD = 5.0
    if direction_diff < DIRECTION_THRESHOLD:
        reward += 1.0
    else:
        reward -= 0.5

    # Smoothness of turns (penalizing for sudden changes in steering angle)
    if abs(steering_angle) > 24:
        reward -= 0.2

    # Progress bonus to encourage completing the track faster
    TOTAL_NUM_STEPS = 300  # Define the total number of steps expected for the track
    progress_bonus = (params['progress'] / 100.0) * (steps / TOTAL_NUM_STEPS)
    reward += progress_bonus

    return float(reward)