import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

# Training phase
env = gym.make("CartPole-v1")
env = DummyVecEnv([lambda: env])  # Vectorize the environment

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("cartpole_agent")

# Testing phase
env = gym.make("CartPole-v1")
env = DummyVecEnv([lambda: env])  # Keep it vectorized for consistency

obs = env.reset()  # Returns a vectorized observation
total_reward = 0
for _ in range(500):
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    total_reward += reward[0]  # Reward is an array in vectorized env, take first element
    env.render()  # Uncomment to visualize (may need 'human' render mode)
    if done[0]:  # Done is an array too
        break

print(f"Total Reward: {total_reward}")
env.close()