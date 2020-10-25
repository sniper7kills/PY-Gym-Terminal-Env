import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from tf_agents.specs import array_spec
import subprocess

class TerminalEnv(gym.Env):
  metadata = {'render.modes':['human']}

  def __init__(self):
    self._episode_ended = False
    self._terminal = "Enter a Command"
    self.terminal_address = None
    self.terminal_port = None
    self.connectToTerminal()

  def step(self, keypress):
    print("log: Entering Command: " + keypress)
    proc = subprocess.Popen([keypress], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err is not None and (out is None or out.decode('UTF-8') == ''):
      print("log: Error: ", err)
      return err.decode('UTF-8')
    print("log:", out)
    return out.decode('UTF-8')

  def reset(self):
    self._episode_ended = False
    return self._terminal

  def render(self, mode='human'):
    print("Render")

  def close(self):
    print("Close")

  def connectToTerminal(self):
    print("Connecting To Terminal")