from gym.envs.registration import register

register(
    id="terminal-v0",
    entry_point="gym_terminal.envs:TerminalEnv"
)