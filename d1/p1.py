import random
import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")

env.reset()
env.render()

for _ in range(100) :
    observation, reward, termination, truncation, info  = env.step(random.choice((0,1)))
    env.render()
    print(observation, reward, termination, truncation, info)

    if termination:
        break
env.close()
# pip3 install "gymnasium[all]"