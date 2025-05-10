MIN_SPEED = 1.0
MAX_SPEED = 2.0

# Margin threshold for being near the inner edge
def edge_margin(params):
    # Allow greater margin for turns
    margin = (abs(params['steering_angle']) / 20) * params['track_width']

    return margin

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_reversed = params['is_reversed']
    is_left_of_center = params['is_left_of_center']
    progress = params['progress']
    steps = params['steps']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']

    # Give a very low reward by default
    reward = 1e-3

    # Reward progress on percentage of track completed
    reward += progress / 100.0  # Normalize to 0–1

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += 1.0

    # Increase reward closer to the inner edge, within the margin
    margin = edge_margin(params)
    edge_proximity = (track_width / 2) - distance_from_center

    # If agent is within the inner edge
    within_inner_edge = (is_reversed and not is_left_of_center) or (not is_reversed and is_left_of_center)

    if within_inner_edge and edge_proximity > 0:
        reward += 1.0 + ((margin - edge_proximity) / margin)

    # Reward high speed on straights, low speeds on curves
    if abs_steering <= 5:
        # Reward higher speeds on straight sections
        reward += 2.5 * min(1.0, speed / MAX_SPEED)
    elif abs_steering <= 15:
        reward += 2.0 * min(1.0, speed / MAX_SPEED)
    else:
        # Penalize for high speeds on turns
        reward += max(0.2, 1.0 - ((speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)))
        
    # Incentivise less steps
    reward += (progress / steps) * 10.0 
    
    if params['is_offtrack']:
        reward *= 0.1  # Strong penalty for going off track
    
    # Always return a float value
    return float(reward)
    