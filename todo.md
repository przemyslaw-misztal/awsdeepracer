[x] Train pm-wroc-fighter-v3-450m-3ms-90m on counterclockwise and test
[] Training log analysis - pm-wroc-fighter-v3-450m-3ms-90m
[x] Train pm-wroc-fighter-v4-90m (changed rewrd function weights to increase impact of speed and steering, less action space parameters on edges and slower as well)
[x] try with this action space - https://github.com/FranklineMisango/ATLienHK_AWS_DeepRacer/blob/main/reward/reward_qualifier.py
[x] try with this action space https://github.com/FranklineMisango/ATLienHK_AWS_DeepRacer/blob/main/reward/reward_qualifier.py
[x] Train this for 90 minutes  - pm-cowboy-v1 = https://github.com/Shubham17-beep/AWS-DeepRacer-Reward-Function/blob/main/README.md
[] Train the most successful model for 300 minutes on the spot
    [] discourage >15
    [] try with this action space - https://github.com/FranklineMisango/ATLienHK_AWS_DeepRacer/blob/main/reward/reward_qualifier.py
    [] encourage speed

[] https://github.com/AlboBoy23/AWS-DeepRacer-Reward-Function/blob/main/reward.py
[] https://github.com/gabriosilva/deepracer/blob/main/reward.py

[] Train the pm-wroc-fighter-v4 for 500 minutes on the spot
[] Train the pm-wroc-fighter-v3 with adjusted hyperparameters for 500 minutes on the spot
[] Train the pm-wroc-fighter-v3 original for 500 minutes on the spot
[] theoretically super fast  -https://github.com/Shubham17-beep/AWS-DeepRacer-Reward-Function/blob/main/reward_function.py



[] https://github.com/Arian-Abdi/DeepRacer-Reward-function/blob/main/Final%20Function.py
[] https://github.com/AlboBoy23/AWS-DeepRacer-Reward-Function/blob/main/reward.py
[] https://github.com/gabriosilva/deepracer/blob/main/reward.py
[] https://github.com/GoSleepBelall/AWSDeepRacer/tree/main/Reward%20Functions

[] try visualizer https://github.com/1-ashraful-islam/deepracer-reward-function-visualizer
[] Explore the continous action space and reward function with three components

speed [2.2; 3.5] m/s
steering -30; 30

ppo
Tensorflow

64
0.01
0.985
Huber
0.0004
32
3

f(x) = car heading bonus
g(x) = distance from center or raceline bonus (need to be continouos)
h(x) = speed bonus

reward = reward_func(f(x), g(x), h(x))