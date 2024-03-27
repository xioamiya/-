import numpy as np
import gymnasium as gym
import random 
import imageio
import os
import tqdm

import pickle
from tqdm.notebook import tqdm

env = gym.make('FrozenLake-v1', map_name='4x4', is_slippery=False,render_mode='human')
desc = ['SFFD', 'FHFH', 'FFFH', 'HFFG']
gym.make('FrozenLake-v1',desc=desc, is_slippery=False)

#print(env.observation_space)
#print(env.action_space)

state_space = env.observation_space.n
action_space = env.action_space.n

def initialize_q_table(state_space,action_space):
    Qtable = np.zeros((state_space,action_space))
    return Qtable
        
def greedy_policy(Qtable,state):
    action = np.argmax(Qtable[state][:])
    return action

def epsilon_greedy_policy(Qtable,state,epsilon):
    random_num = random.uniform(0,1)
    if random_num > epsilon:
        action = greedy_policy(Qtable=Qtable,state=state)
    else:
        action = env.action_space.sample()
    return action

n_training_episodes = 100
learning_rate = 0.7
n_eval_eoisodes = 100
max_steps = 99
env_id = 'FrozenLake-v1'

eval_seed = []
max_eosilon = 1.0
min_eosilon = 0.05
decay_rate = 0.0005

def train(n_training_episodes,min_epsilon,max_epsilon,decay_rate,env,max_steps,Qtable,epsilon):
    for episode in tqdm(range(n_training_episodes)):
        state, info = env.reset()
        step = 0
        terminated = False
        truncated = False

        for step in range(max_steps):
            action = epsilon_greedy_policy(Qtable,state,epsilon)
            new_state,reward,terminated,truncated,info = env.step(action)

            Qtable[state][action] = Qtable[state][action] + learning_rate*(
                reward + np.max(Qtable[new_state]) - Qtable[state][action]
            )

            if terminated or truncated:
                break
            state = new_state

        return Qtable
    
def evaluate_agent(env,max_steps,n_eval_episodes,Q,seed):
    episode_rewards = []
    for episode in tqdm(range(n_eval_episodes)):
        if seed:
            state, info = env.reset(seed=seed[episode])
        else:
            state, info = env.reset()
        step = 0
        terminated = False
        truncated = False
        total_rewards_ep = 0
        for step in range(max_steps):
            action = greedy_policy(Q,state)
            new_state,reward,terminated,truncated,info = env.step(action)
            total_rewards_ep += reward

            if terminated or truncated:
                break
            state = new_state
        episode_rewards.append(total_rewards_ep)
    mean_reward = np.mean(episode_rewards)
    std_reward = np.std(episode_rewards)

    return mean_reward, std_reward


Qtable_frozenlake = initialize_q_table(state_space,action_space)

Qtable_frozenlake = train(n_training_episodes,min_eosilon,max_eosilon,decay_rate,env,max_steps,Qtable_frozenlake,epsilon=0.1)
mean_reward, std_reward = evaluate_agent(env,max_steps,n_eval_eoisodes,Qtable_frozenlake,eval_seed)
print(mean_reward,std_reward)