import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

model = PPO.load("cartpole_agent")
env = gym.make("CartPole-v1")
env = DummyVecEnv([lambda: env])

obs = env.reset()
total_reward = 0

for _ in range(500):
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    total_reward += reward[0]
    if done[0]:
        break

print(f"Total Reward: {total_reward}")
env.close()