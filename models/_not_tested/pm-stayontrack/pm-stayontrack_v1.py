def reward_function(params):
    reward = 1e-3
    PENALTY = 5.0

    if not params['all_wheels_on_track']:
        reward -= PENALTY * params['distance_from_center']
    else:
        reward += 1

    return float(reward)