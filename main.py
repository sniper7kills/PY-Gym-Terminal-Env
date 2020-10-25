import gym
import numpy as np
import tensorflow as tf
from tf_agents.networks import actor_distribution_network
from tf_agents.agents.reinforce import reinforce_agent

train_env = gym.make('gym_terminal:terminal-v0')

# step = env.reset()
# print('Reset:')
# print(step)

# action = "ls -R /"

# next_step = env.step(action)
# print('First Command:')
# print(next_step)

fc_layer_params = (100,)
learning_rate = 1e-3 # @param {type:"number"}

actor_net = actor_distribution_network.ActorDistributionNetwork(
    train_env.observation_spec(),
    train_env.action_spec(),
    fc_layer_params=fc_layer_params)

optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate)

train_step_counter = tf.compat.v2.Variable(0)

tf_agent = reinforce_agent.ReinforceAgent(
    train_env.time_step_spec(),
    train_env.action_spec(),
    actor_network=actor_net,
    optimizer=optimizer,
    normalize_returns=True,
    train_step_counter=train_step_counter)
tf_agent.initialize()