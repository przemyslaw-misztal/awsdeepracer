#Optimise for efficient progress and speed
# https://mickqg.github.io/DeepracerBlog/

def reward_function(params):

    # Read input variables
    reward = 0.001

    if params["all_wheels_on_track"]:

        if params['steps']<10:
            reward = (1 - (params['distance_from_center'] / (params['track_width']/2))**(4))*params['speed']**2
        if params['steps']>=10:
            reward = ((params['progress']*params['speed']**2)/params['steps'])*2
    else:
        reward = 0.01

    if abs(params['steering_angle']) < 10 and params['speed']==3:
        reward += params['speed']**2/4
    else:
        reward += 0.01

    return float(reward)