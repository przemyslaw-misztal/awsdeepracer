def reward_function(params):
    """
    Reward function for AWS DeepRacer.
    Rewards the car for staying close to the centerline and penalizes it for deviating.
    """
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Define markers at varying distances from the centerline
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize reward
    reward = 1e-3  # Small reward by default

    # Reward based on distance from centerline
    if distance_from_center <= marker_1:
        reward = 1.0  # Closest to the centerline
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # Likely off track

    # Penalize if the car is off track
    if not all_wheels_on_track:
        reward = 1e-3

    # Reward higher speeds, but only if the car is on track
    if all_wheels_on_track and reward > 1e-3:
        reward += speed * 0.1

    return float(reward)