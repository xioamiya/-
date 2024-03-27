#%%
import numpy as np
np.random.seed(0)

#定义状态转移概率矩阵p
p = [
    [0.9,0.1,0.0,0.0,0.0,0.0],
    [0.5,0.0,0.5,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.6,0.0,0.4],
    [0.0,0.0,0.0,0.0,0.3,0.7],
    [0.0,0.2,0.3,0.5,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,1.0],
]

P = np.array(p)

rewards = [-1,-2,-2,10,1,0]

gamma = 0.5

def compute_return(start_index, chain, gamma):
    G = 0
    for i in reversed(range(start_index, len(chain))):
        G = gamma*G+rewards[chain[i]-1]
    return G

chain = [1,2,3,6]
start_index = 0
G = compute_return(start_index,chain,gamma)
print(f'应该得到的回到:{G}')
# %%
def compute(P,rewards, gamma,states_num):
    rewards = np.array(rewards).reshape((-1,1))
    value = np.dot(np.linalg.inv(np.eye(states_num)-gamma*P),rewards)
    return value

V = compute(P,rewards,gamma,6)
print(V)
# %%
S = ['s1','s2','s3','s4','s5'],
A = [
    '保持s1','前往s1',
    '前往s2','前往s3','前往s4','前往s5','概率向前'
]
#状态转移函数
P = {
    's1-保持s1-s1':1.0, 's1-前往s2-s2':1.0,
    's2-前往s1-s1':1.0, 's2-前往s3-s3':1.0,
    's3-前往s4-s4':1.0, 's3-前往s5-s5':1.0,
    's4-前往s5-s5':1.0, 's4-概率前往-s2':0.2,
    's2-概率前往-s3':0.4, 's4-概率前往-s4':0.4,
}

#奖励函数
R = {
    's1-保持s1':-1, 's1-前往s2':0,
    's2-前往s1':-1, 's2-前往s3':-2,
    's3-前往s4':-2, 's3-前往s5':0,
    's4-前往s5':10, 's1-前往s2':1,
}

gamma =0.5
MDP = (S,A,P,R,gamma)

#策略1，随机策略都是0.5
Pi_1 = {
    's1-保持s1':0.5, 's1-前往s2':0.5,
    's2-前往s1':0.5, 's2-前往s3':0.5,
    's3-前往s4':0.5, 's3-前往s5':0.5,
    's4-前往s5':0.5, 's4-概率前往':0.5,
}

Pi_2 = {
    's1-保持s1':0.6, 's1-前往s2':0.4,
    's2-前往s1':0.3, 's2-前往s3':0.7,
    's3-前往s4':0.5, 's3-前往s5':0.5,
    's4-前往s5':0.1, 's4-概率前往':0.9,
}

def join(str1,str2):
    return str1 + '-' + str2


P_from_mdp_to_mrp=[
    [0.5,0.5,0.0,0.0,0.0],
    [0.5,0.0,0.5,0.0,0.0],
    [0.0,0.0,0.0,0.5,0.5],
    [0.0,0.1,0.2,0.2,0.5],
    [0.0,0.0,0.0,0.0,1.0],
]

P_from_mdp_to_mrp = np.array(P_from_mdp_to_mrp)
R_from_mdp_to_mrp = [-0.5,-1.5,-1.0,5.5,0]

V = compute(P_from_mdp_to_mrp,R_from_mdp_to_mrp,gamma,5)
print(f'MDP中每个状态的价值分别为{V}')
# %%
