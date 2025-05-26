[x] Train pm-wroc-fighter-v3-450m-3ms-90m on counterclockwise and test
[] Training log analysis - pm-wroc-fighter-v3-450m-3ms-90m
[] Train pm-wroc-fighter-v4-90m (changed rewrd function weights to increase impact of speed and steering, less action space parameters on edges and slower as well)
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