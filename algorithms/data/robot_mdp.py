'''
Define the Robot MDP Properties
'''
from algorithms.mdp import *


def generate_Robot_MDP(step_cost = -0.04):
    states = ('(1,1)', '(1,2)', '(1,3)', '(2,1)', '(2,3)', '(3,1)', '(3,2)', '(3,3)', '(4,1)', '(4,2)', '(4,3)')
    actions = ('UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY')
    probabilities = {
        ('(1,1)', 'UP', '(1,2)'): 0.8,
        ('(1,1)', 'UP', '(2,1)'): 0.1,
        ('(1,1)', 'UP', '(1,1)'): 0.1,
        ('(1,1)', 'DOWN', '(1,1)'): 0.9,
        ('(1,1)', 'DOWN', '(2,1)'): 0.1,
        ('(1,1)', 'LEFT', '(1,1)'): 0.9,
        ('(1,1)', 'LEFT', '(1,2)'): 0.1,
        ('(1,1)', 'RIGHT', '(2,1)'): 0.8,
        ('(1,1)', 'RIGHT', '(1,2)'): 0.1,
        ('(1,1)', 'RIGHT', '(1,1)'): 0.1,

        ('(1,2)', 'UP', '(1,3)'): 0.8,
        ('(1,2)', 'UP', '(1,2)'): 0.2,
        ('(1,2)', 'DOWN', '(1,1)'): 0.8,
        ('(1,2)', 'DOWN', '(1,2)'): 0.2,
        ('(1,2)', 'LEFT', '(1,2)'): 0.8,
        ('(1,2)', 'LEFT', '(1,3)'): 0.1,
        ('(1,2)', 'LEFT', '(1,1)'): 0.1,
        ('(1,2)', 'RIGHT', '(1,2)'): 0.8,
        ('(1,2)', 'RIGHT', '(1,3)'): 0.1,
        ('(1,2)', 'RIGHT', '(1,1)'): 0.1,

        ('(1,3)', 'UP', '(1,3)'): 0.9,
        ('(1,3)', 'UP', '(2,3)'): 0.1,
        ('(1,3)', 'DOWN', '(1,2)'): 0.8,
        ('(1,3)', 'DOWN', '(2,3)'): 0.1,
        ('(1,3)', 'DOWN', '(1,3)'): 0.1,
        ('(1,3)', 'LEFT', '(1,3)'): 0.9,
        ('(1,3)', 'LEFT', '(1,2)'): 0.1,
        ('(1,3)', 'RIGHT', '(2,3)'): 0.8,
        ('(1,3)', 'RIGHT', '(1,3)'): 0.1,
        ('(1,3)', 'RIGHT', '(1,2)'): 0.1,

        ('(2,1)', 'UP', '(2,1)'): 0.8,
        ('(2,1)', 'UP', '(1,1)'): 0.1,
        ('(2,1)', 'UP', '(3,1)'): 0.1,
        ('(2,1)', 'DOWN', '(2,1)'): 0.8,
        ('(2,1)', 'DOWN', '(1,1)'): 0.1,
        ('(2,1)', 'DOWN', '(3,1)'): 0.1,
        ('(2,1)', 'LEFT', '(1,1)'): 0.8,
        ('(2,1)', 'LEFT', '(2,1)'): 0.2,
        ('(2,1)', 'RIGHT', '(3,1)'): 0.8,
        ('(2,1)', 'RIGHT', '(2,1)'): 0.2,

        ('(2,3)', 'UP', '(2,3)'): 0.8,
        ('(2,3)', 'UP', '(1,3)'): 0.1,
        ('(2,3)', 'UP', '(3,3)'): 0.1,
        ('(2,3)', 'DOWN', '(2,3)'): 0.8,
        ('(2,3)', 'DOWN', '(1,3)'): 0.1,
        ('(2,3)', 'DOWN', '(3,3)'): 0.1,
        ('(2,3)', 'LEFT', '(1,3)'): 0.8,
        ('(2,3)', 'LEFT', '(2,3)'): 0.2,
        ('(2,3)', 'RIGHT', '(3,3)'): 0.8,
        ('(2,3)', 'RIGHT', '(2,3)'): 0.2,

        ('(3,1)', 'UP', '(3,2)'): 0.8,
        ('(3,1)', 'UP', '(2,1)'): 0.1,
        ('(3,1)', 'UP', '(4,1)'): 0.1,
        ('(3,1)', 'DOWN', '(3,1)'): 0.8,
        ('(3,1)', 'DOWN', '(2,1)'): 0.1,
        ('(3,1)', 'DOWN', '(3,1)'): 0.1,
        ('(3,1)', 'LEFT', '(2,1)'): 0.8,
        ('(3,1)', 'LEFT', '(3,2)'): 0.1,
        ('(3,1)', 'LEFT', '(3,1)'): 0.1,
        ('(3,1)', 'RIGHT', '(4,1)'): 0.8,
        ('(3,1)', 'RIGHT', '(3,2)'): 0.1,
        ('(3,1)', 'RIGHT', '(3,1)'): 0.1,

        ('(3,2)', 'UP', '(3,3)'): 0.8,
        ('(3,2)', 'UP', '(3,2)'): 0.1,
        ('(3,2)', 'UP', '(4,2)'): 0.1,
        ('(3,2)', 'DOWN', '(3,1)'): 0.8,
        ('(3,2)', 'DOWN', '(3,2)'): 0.1,
        ('(3,2)', 'DOWN', '(4,2)'): 0.1,
        ('(3,2)', 'LEFT', '(3,2)'): 0.8,
        ('(3,2)', 'LEFT', '(3,3)'): 0.1,
        ('(3,2)', 'LEFT', '(3,1)'): 0.1,
        ('(3,2)', 'RIGHT', '(4,2)'): 0.8,
        ('(3,2)', 'RIGHT', '(3,3)'): 0.1,
        ('(3,2)', 'RIGHT', '(3,1)'): 0.1,

        ('(3,3)', 'UP', '(3,3)'): 0.8,
        ('(3,3)', 'UP', '(2,3)'): 0.1,
        ('(3,3)', 'UP', '(4,3)'): 0.1,
        ('(3,3)', 'DOWN', '(3,2)'): 0.8,
        ('(3,3)', 'DOWN', '(2,3)'): 0.1,
        ('(3,3)', 'DOWN', '(4,3)'): 0.1,
        ('(3,3)', 'LEFT', '(2,3)'): 0.8,
        ('(3,3)', 'LEFT', '(3,3)'): 0.1,
        ('(3,3)', 'LEFT', '(3,2)'): 0.1,
        ('(3,3)', 'RIGHT', '(4,2)'): 0.8,
        ('(3,3)', 'RIGHT', '(3,3)'): 0.1,
        ('(3,3)', 'RIGHT', '(3,2)'): 0.1,

        ('(4,1)', 'UP', '(4,2)'): 0.8,
        ('(4,1)', 'UP', '(4,1)'): 0.1,
        ('(4,1)', 'UP', '(3,1)'): 0.1,
        ('(4,1)', 'DOWN', '(4,1)'): 0.9,
        ('(4,1)', 'DOWN', '(3,1)'): 0.1,
        ('(4,1)', 'LEFT', '(3,1)'): 0.8,
        ('(4,1)', 'LEFT', '(4,1)'): 0.1,
        ('(4,1)', 'LEFT', '(4,2)'): 0.1,
        ('(4,1)', 'RIGHT', '(4,1)'): 0.9,
        ('(4,1)', 'RIGHT', '(4,2)'): 0.1,

        ('(4,3)', 'STAY', '(4,3)'): 1,
        ('(4,2)', 'STAY', '(4,2)'): 1,
    }
    rewards = {
        ('(1,1)', 'UP', '(1,2)'): step_cost,
        ('(1,1)', 'UP', '(2,1)'): step_cost,
        ('(1,1)', 'UP', '(1,1)'): step_cost,
        ('(1,1)', 'DOWN', '(1,1)'): step_cost,
        ('(1,1)', 'DOWN', '(2,1)'): step_cost,
        ('(1,1)', 'LEFT', '(1,1)'): step_cost,
        ('(1,1)', 'LEFT', '(1,2)'): step_cost,
        ('(1,1)', 'RIGHT', '(2,1)'): step_cost,
        ('(1,1)', 'RIGHT', '(1,2)'): step_cost,
        ('(1,1)', 'RIGHT', '(1,1)'): step_cost,

        ('(1,2)', 'UP', '(1,3)'): step_cost,
        ('(1,2)', 'UP', '(1,2)'): step_cost,
        ('(1,2)', 'DOWN', '(1,1)'): step_cost,
        ('(1,2)', 'DOWN', '(1,2)'): step_cost,
        ('(1,2)', 'LEFT', '(1,2)'): step_cost,
        ('(1,2)', 'LEFT', '(1,3)'): step_cost,
        ('(1,2)', 'LEFT', '(1,1)'): step_cost,
        ('(1,2)', 'RIGHT', '(1,2)'): step_cost,
        ('(1,2)', 'RIGHT', '(1,3)'): step_cost,
        ('(1,2)', 'RIGHT', '(1,1)'): step_cost,

        ('(1,3)', 'UP', '(1,3)'): step_cost,
        ('(1,3)', 'UP', '(2,3)'): step_cost,
        ('(1,3)', 'DOWN', '(1,2)'): step_cost,
        ('(1,3)', 'DOWN', '(2,3)'): step_cost,
        ('(1,3)', 'DOWN', '(1,3)'): step_cost,
        ('(1,3)', 'LEFT', '(1,3)'): step_cost,
        ('(1,3)', 'LEFT', '(1,2)'): step_cost,
        ('(1,3)', 'RIGHT', '(2,3)'): step_cost,
        ('(1,3)', 'RIGHT', '(1,3)'): step_cost,
        ('(1,3)', 'RIGHT', '(1,2)'): step_cost,

        ('(2,1)', 'UP', '(2,1)'): step_cost,
        ('(2,1)', 'UP', '(1,1)'): step_cost,
        ('(2,1)', 'UP', '(3,1)'): step_cost,
        ('(2,1)', 'DOWN', '(2,1)'): step_cost,
        ('(2,1)', 'DOWN', '(1,1)'): step_cost,
        ('(2,1)', 'DOWN', '(3,1)'): step_cost,
        ('(2,1)', 'LEFT', '(1,1)'): step_cost,
        ('(2,1)', 'LEFT', '(2,1)'): step_cost,
        ('(2,1)', 'RIGHT', '(3,1)'): step_cost,
        ('(2,1)', 'RIGHT', '(2,1)'): step_cost,

        ('(2,3)', 'UP', '(2,3)'): step_cost,
        ('(2,3)', 'UP', '(1,3)'): step_cost,
        ('(2,3)', 'UP', '(3,3)'): step_cost,
        ('(2,3)', 'DOWN', '(2,3)'): step_cost,
        ('(2,3)', 'DOWN', '(1,3)'): step_cost,
        ('(2,3)', 'DOWN', '(3,3)'): step_cost,
        ('(2,3)', 'LEFT', '(1,3)'): step_cost,
        ('(2,3)', 'LEFT', '(2,3)'): step_cost,
        ('(2,3)', 'RIGHT', '(3,3)'): step_cost,
        ('(2,3)', 'RIGHT', '(2,3)'): step_cost,

        ('(3,1)', 'UP', '(3,2)'): step_cost,
        ('(3,1)', 'UP', '(2,1)'): step_cost,
        ('(3,1)', 'UP', '(4,1)'): step_cost,
        ('(3,1)', 'DOWN', '(3,1)'): step_cost,
        ('(3,1)', 'DOWN', '(2,1)'): step_cost,
        ('(3,1)', 'DOWN', '(3,1)'): step_cost,
        ('(3,1)', 'LEFT', '(2,1)'): step_cost,
        ('(3,1)', 'LEFT', '(3,2)'): step_cost,
        ('(3,1)', 'LEFT', '(3,1)'): step_cost,
        ('(3,1)', 'RIGHT', '(4,1)'): step_cost,
        ('(3,1)', 'RIGHT', '(3,2)'): step_cost,
        ('(3,1)', 'RIGHT', '(3,1)'): step_cost,

        ('(3,2)', 'UP', '(3,3)'): step_cost,
        ('(3,2)', 'UP', '(3,2)'): step_cost,
        ('(3,2)', 'UP', '(4,2)'): step_cost,
        ('(3,2)', 'DOWN', '(3,1)'): step_cost,
        ('(3,2)', 'DOWN', '(3,2)'): step_cost,
        ('(3,2)', 'DOWN', '(4,2)'): step_cost,
        ('(3,2)', 'LEFT', '(3,2)'): step_cost,
        ('(3,2)', 'LEFT', '(3,3)'): step_cost,
        ('(3,2)', 'LEFT', '(3,1)'): step_cost,
        ('(3,2)', 'RIGHT', '(4,2)'): step_cost,
        ('(3,2)', 'RIGHT', '(3,3)'): step_cost,
        ('(3,2)', 'RIGHT', '(3,1)'): step_cost,

        ('(3,3)', 'UP', '(3,3)'): step_cost,
        ('(3,3)', 'UP', '(2,3)'): step_cost,
        ('(3,3)', 'UP', '(4,3)'): step_cost,
        ('(3,3)', 'DOWN', '(3,2)'): step_cost,
        ('(3,3)', 'DOWN', '(2,3)'): step_cost,
        ('(3,3)', 'DOWN', '(4,3)'): step_cost,
        ('(3,3)', 'LEFT', '(2,3)'): step_cost,
        ('(3,3)', 'LEFT', '(3,3)'): step_cost,
        ('(3,3)', 'LEFT', '(3,2)'): step_cost,
        ('(3,3)', 'RIGHT', '(4,2)'): step_cost,
        ('(3,3)', 'RIGHT', '(3,3)'): step_cost,
        ('(3,3)', 'RIGHT', '(3,2)'): step_cost,

        ('(4,1)', 'UP', '(4,2)'): step_cost,
        ('(4,1)', 'UP', '(4,1)'): step_cost,
        ('(4,1)', 'UP', '(3,1)'): step_cost,
        ('(4,1)', 'DOWN', '(4,1)'): step_cost,
        ('(4,1)', 'DOWN', '(3,1)'): step_cost,
        ('(4,1)', 'LEFT', '(3,1)'): step_cost,
        ('(4,1)', 'LEFT', '(4,1)'): step_cost,
        ('(4,1)', 'LEFT', '(4,2)'): step_cost,
        ('(4,1)', 'RIGHT', '(4,1)'): step_cost,
        ('(4,1)', 'RIGHT', '(4,2)'): step_cost,

        ('(4,3)', 'STAY', '(4,3)'): 1,
        ('(4,2)', 'STAY', '(4,2)'): -1,
    }

    markov = MDP(states, actions, probabilities, rewards)
    return markov

def plot_z(policy, z, policy_value):
    if policy['(1,1)'] == 'UP':
        z[0][0] = '↑, V=' + str(round(policy_value['(1,1)'], 4))
    if policy['(1,1)'] == 'DOWN':
        z[0][0] = '↓, V=' + str(round(policy_value['(1,1)'], 4))
    if policy['(1,1)'] == 'LEFT':
        z[0][0] = '←, V=' + str(round(policy_value['(1,1)'], 4))
    if policy['(1,1)'] == 'RIGHT':
        z[0][0] = '→, V=' + str(round(policy_value['(1,1)'], 4))

    if policy['(1,2)'] == 'UP':
        z[1][0] = '↑, V=' + str(round(policy_value['(1,2)'], 4))
    if policy['(1,2)'] == 'DOWN':
        z[1][0] = '↓, V=' + str(round(policy_value['(1,2)'], 4))
    if policy['(1,2)'] == 'LEFT':
        z[1][0] = '←, V=' + str(round(policy_value['(1,2)'], 4))
    if policy['(1,2)'] == 'RIGHT':
        z[1][0] = '→, V=' + str(round(policy_value['(1,2)'], 4))

    if policy['(1,3)'] == 'UP':
        z[2][0] = '↑, V=' + str(round(policy_value['(1,3)'], 4))
    if policy['(1,3)'] == 'DOWN':
        z[2][0] = '↓, V=' + str(round(policy_value['(1,3)'], 4))
    if policy['(1,3)'] == 'LEFT':
        z[2][0] = '←, V=' + str(round(policy_value['(1,3)'], 4))
    if policy['(1,3)'] == 'RIGHT':
        z[2][0] = '→, V=' + str(round(policy_value['(1,3)'], 4))

    if policy['(2,1)'] == 'UP':
        z[0][1] = '↑, V=' + str(round(policy_value['(2,1)'], 4))
    if policy['(2,1)'] == 'DOWN':
        z[0][1] = '↓, V=' + str(round(policy_value['(2,1)'], 4))
    if policy['(2,1)'] == 'RIGHT':
        z[0][1] = '→, V=' + str(round(policy_value['(2,1)'], 4))
    if policy['(2,1)'] == 'LEFT':
        z[0][1] = '←, V=' + str(round(policy_value['(2,1)'], 4))

    if policy['(2,3)'] == 'UP':
        z[2][1] = '↑, V=' + str(round(policy_value['(2,3)'], 4))
    if policy['(2,3)'] == 'DOWN':
        z[2][1] = '↓, V=' + str(round(policy_value['(2,3)'], 4))
    if policy['(2,3)'] == 'RIGHT':
        z[2][1] = '→, V=' + str(round(policy_value['(2,3)'], 4))
    if policy['(2,3)'] == 'LEFT':
        z[2][1] = '←, V=' + str(round(policy_value['(2,3)'], 4))

    if policy['(3,1)'] == 'RIGHT':
        z[0][2] = '→, V=' + str(round(policy_value['(3,1)'], 4))
    if policy['(3,1)'] == 'UP':
        z[0][2] = '↑, V=' + str(round(policy_value['(3,1)'], 4))
    if policy['(3,1)'] == 'LEFT':
        z[0][2] = '←, V=' + str(round(policy_value['(3,1)'], 4))
    if policy['(3,1)'] == 'DOWN':
        z[0][2] = '↓, V=' + str(round(policy_value['(3,1)'], 4))

    if policy['(3,2)'] == 'LEFT':
        z[1][2] = '←, V=' + str(round(policy_value['(3,2)'], 4))
    if policy['(3,2)'] == 'RIGHT':
        z[1][2] = '→, V=' + str(round(policy_value['(3,2)'], 4))
    if policy['(3,2)'] == 'UP':
        z[1][2] = '↑, V=' + str(round(policy_value['(3,2)'], 4))
    if policy['(3,2)'] == 'DOWN':
        z[1][2] = '↓, V=' + str(round(policy_value['(3,2)'], 4))

    if policy['(3,3)'] == 'UP':
        z[2][2] = '↑, V=' + str(round(policy_value['(3,3)'], 4))
    if policy['(3,3)'] == 'RIGHT':
        z[2][2] = '→, V=' + str(round(policy_value['(3,3)'], 4))
    if policy['(3,3)'] == 'DOWN':
        z[2][2] = '↓, V=' + str(round(policy_value['(3,3)'], 4))
    if policy['(3,3)'] == 'LEFT':
        z[2][2] = '←, V=' + str(round(policy_value['(3,3)'], 4))

    if policy['(4,1)'] == 'UP':
        z[0][3] = '↑, V=' + str(round(policy_value['(4,1)'], 4))
    if policy['(4,1)'] == 'RIGHT':
        z[0][3] = '→, V=' + str(round(policy_value['(4,1)'], 4))
    if policy['(4,1)'] == 'DOWN':
        z[0][3] = '↓, V=' + str(round(policy_value['(4,1)'], 4))
    if policy['(4,1)'] == 'LEFT':
        z[0][3] = '←, V=' + str(round(policy_value['(4,1)'], 4))

    z[1][3] = '-1, V=' + str(round(policy_value['(4,2)'], 4))
    z[2][3] = '1, V=' + str(round(policy_value['(4,3)'], 4))

    return z


policy1 = {
        '(1,1)' : 'RIGHT',
        '(1,2)' : 'DOWN',
        '(1,3)' : 'RIGHT',
        '(2,1)' : 'RIGHT',
        '(2,3)' : 'RIGHT',
        '(3,1)' : 'UP',
        '(3,2)' : 'RIGHT',
        '(3,3)' : 'RIGHT',
        '(4,1)' : 'UP',
        '(4,2)' : 'STAY',
        '(4,3)' : 'STAY',
}

policy2 = {
        '(1,1)' : 'UP',
        '(1,2)' : 'DOWN',
        '(1,3)' : 'DOWN',
        '(2,1)' : 'LEFT',
        '(2,3)' : 'LEFT',
        '(3,1)' : 'UP',
        '(3,2)' : 'DOWN',
        '(3,3)' : 'LEFT',
        '(4,1)' : 'LEFT',
        '(4,2)' : 'STAY',
        '(4,3)' : 'STAY',
}

policy3 = {
        '(1,1)' : 'UP',
        '(1,2)' : 'UP',
        '(1,3)' : 'RIGHT',
        '(2,1)' : 'RIGHT',
        '(2,3)' : 'RIGHT',
        '(3,1)' : 'UP',
        '(3,2)' : 'UP',
        '(3,3)' : 'RIGHT',
        '(4,1)' : 'LEFT',
        '(4,2)' : 'STAY',
        '(4,3)' : 'STAY',
}