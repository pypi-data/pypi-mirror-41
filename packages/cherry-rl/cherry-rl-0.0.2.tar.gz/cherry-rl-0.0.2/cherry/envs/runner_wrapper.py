#!/usr/bin/env python3

from .base import Wrapper


class Runner(Wrapper):

    def __init__(self, env):
        super(Runner, self).__init__(env)
        self.env = env
        self._needs_reset = True
        self._current_state = None

    def run(self,
            get_action,
            replay=None,
            steps=None,
            episodes=None,
            render=False):

        if steps is None:
            steps = float('inf')
        if episodes is None:
            episodes = float('inf')

        collected_episodes = 0
        collected_steps = 0
        while True:
            if self._needs_reset:
                self._current_state = self.env.reset()
                self._needs_reset = False
            info = {}
            action = tuple(get_action(self._current_state))
            if len(action) == 2:
                info = action[1]
                action = action[0]
            else:
                action = action[0]
            old_state = self._current_state
            state, reward, done, _ = self.env.step(action)
            if done:
                collected_episodes += 1
                state = self.env.reset()
            if replay is not None:
                replay.add(old_state, action, reward, state, done, info=info)
            self._current_state = state
            if render:
                self.env.render()
            collected_steps += 1
            if collected_steps >= steps or collected_episodes >= episodes:
                return collected_steps, collected_episodes
