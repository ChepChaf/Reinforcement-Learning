import gym
env = gym.make("CartPole-v1")
observation = env.reset()

total_reward = 0

for _ in range(1000):
  env.render()
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)

  total_reward += reward

  if done:
    print("Reward: {}".format(total_reward))
    total_reward = 0

    observation = env.reset()
env.close()