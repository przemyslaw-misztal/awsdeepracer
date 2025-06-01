def reward_function(params):

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params.get('steering_angle', 0)
    heading = params.get('heading', 0)
    track_heading = params.get('track_heading', 0)
    time_elapsed = params.get('time', 0)
    is_left_of_center = params.get('is_left_of_center', True)  # Boolean indicating position

    # Initialize reward
    reward = 1e-3  # Minimum reward to prevent zero rewards

    # Centerline reward
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # Penalize heavily if far from center or off track

    # Speed bonuses
    if abs(track_heading - heading) < 5:  # On straights
        if speed >= 3.5:  # Reward high speeds close to max
            reward *= 2.0
        elif speed >= 3.0:
            reward *= 1.5
    else:  # On curves
        if 2.0 <= speed <= 3.0:  # Optimal speed range for curves
            reward *= 1.3
        elif speed > 3.5:  # Penalize excessive speed on curves
            reward *= 0.8

    # Progress reward
    # Encourage making consistent progress with fewer steps
    progress_per_step = progress / (steps + 1e-3)  # Avoid division by zero
    reward += min(progress_per_step * 10, 1.0)

    # Steering smoothness
    if abs(steering_angle) < 10:  # Smooth steering
        reward *= 1.2
    else:  # Penalize sharp turns
        reward *= 0.8

    # Turn-handling reward
    if abs(steering_angle) < 10:  # Smooth handling
        if is_left_of_center and track_heading > heading:  # Left turn
            reward *= 1.2  # Higher bonus for dominant right turns
        elif not is_left_of_center and track_heading < heading:  # Right turn
            reward *= 1.4  # Smaller bonus for minor left adjustments
    else:
        reward *= 0.8  # Penalize sharp or erratic steering

    # Additional penalty for zigzagging
    if abs(steering_angle) > 20 and speed > 3.0:  # High-speed zigzagging
        reward *= 0.5

    # Straight section bonus
    if abs(track_heading - heading) < 5 and speed >= 3.5:  # High speed on straights
        reward += 2.0  # Bonus for maximizing speed

    # Completion bonuses
    TARGET_TIME = 10.0  # Target time for lap completion in seconds
    if progress == 100:  # Lap completed
        reward += 30  # Flat completion bonus
        if time_elapsed <= TARGET_TIME * 0.8:  # Exceptional lap time (under 11.25 seconds)
            reward += 70  # Large bonus for very fast laps
        elif time_elapsed <= TARGET_TIME:  # Completed within target time
            reward += 50
        elif time_elapsed > 2 * TARGET_TIME:  # Very slow completion
            reward -= 10  # Small penalty for poor performance

    # Penalize if off track
    if not all_wheels_on_track:
        reward = max(1e-3, 1e-3 * distance_from_center)

    # Ensure reward is non-negative
    reward = max(reward, 1e-3)

    return float(reward)