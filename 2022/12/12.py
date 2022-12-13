from aocd import data, lines, submit

from typing import Tuple, List, Optional
from collections import defaultdict
import random
import math
from copy import deepcopy
from pprint import pprint as pp

from rich.progress import track, Progress

actions = ["^", "v", "<", ">"]


class Environment:
    def __init__(
        self,
        heightmap,
        reward_move=-0.1,
        reward_goal=10,
        reward_illegal=-1000,
        max_height_difference=1,
    ) -> None:
        self.heightmap = heightmap
        self.y_max = len(heightmap)
        self.x_max = len(heightmap[0])
        self.reward_move = reward_move
        self.reward_goal = reward_goal
        self.reward_illegal = reward_illegal
        self.max_height_difference = max_height_difference

        self.total_states = self.x_max * self.y_max * len(actions)

        self.done = False
        self._START = "S"
        self._GOAL = "E"
        self.start = self.get_start()
        self.goal = self.get_goal()

    def __getitem__(self, coord):
        if type(coord) == tuple:
            x, y = coord
            return self.heightmap[y][x]

    def get_start(self):
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self[x, y] == self._START:
                    return x, y

    def get_goal(self):
        for y in range(self.y_max):
            for x in range(self.x_max):
                if self[x, y] == self._GOAL:
                    return x, y

    def is_illegal(self, state, new_state):
        new_x, new_y = new_state
        # Check out-of-bounds
        if self.y_max <= new_y or new_y < 0 or self.x_max <= new_x or new_x < 0:
            return True
        # Check height difference
        # * For start
        elif state == self.start:
            return ord(self[new_state]) - ord("a") > self.max_height_difference
        # * For goal
        elif self[new_state] == self._GOAL:
            return ord("z") - ord(self[state]) > self.max_height_difference
        # * For other moves
        else:
            return ord(self[new_state]) - ord(self[state]) > self.max_height_difference

    def act(
        self, action: str, state: Tuple[int, int], terminal=False
    ) -> Tuple[Tuple[int, int], float]:
        x, y = state
        if terminal and self.done:
            return state, 0.0
        elif state == self.goal:
            return state, self.reward_goal
        match action:
            case "^":
                new_state = x, y - 1
            case "v":
                new_state = x, y + 1
            case "<":
                new_state = x - 1, y
            case ">":
                new_state = x + 1, y
            case _:
                print(f"Invalid action: {action}")
        if self.is_illegal(state, new_state):
            self.done = True
            return state, self.reward_illegal
        elif self[new_state] == self._GOAL:
            self.done = True
            return new_state, self.reward_goal
        else:
            return new_state, self.reward_move

    def random_restart(self):
        self.done = False
        x = random.randrange(0, self.x_max)
        y = random.randrange(0, self.y_max)
        if self[x, y] == self._GOAL:
            return self.random_restart()
        else:
            return x, y

    def restart(self):
        self.done = False
        return self.start


def sigmoid(x, k):
    return 1.0 / (1 + math.exp(-1 * k * x))


class QLearner:
    def __init__(self, alpha=0.8, gamma=0.8):
        self.alpha = alpha
        self.gamma = gamma
        self.q = defaultdict(lambda: 0.5)

    def decide_action(self, state: Optional[Tuple[int, int]] = None):
        if state is None:
            return random.choice(actions)
        rewards = []
        for action in actions:
            rewards.append(self.q[(state, action)])

        min_reward = min(rewards)
        max_reward = max(rewards)
        if min_reward == max_reward:
            return random.choice(actions)
        norm_rewards = [
            (reward - min_reward) / (max_reward - min_reward) for reward in rewards
        ]
        return random.choices(actions, weights=norm_rewards)[0]

    def updateQ(self, state, action, next_state, reward):
        td = (
            reward
            + self.gamma * max([self.q[next_state, a] for a in actions])
            - self.q[(state, action)]
        )
        self.q[(state, action)] = self.q[(state, action)] + self.alpha * td

    def learn(self, env: Environment, iterations: int, gamma_updates=20):
        state = env.random_restart()
        for itr in track(range(iterations), description="Training..."):
            if env.done or itr % env.total_states:
                state = env.random_restart()
            if itr % (iterations // gamma_updates) == 0:
                self.gamma = sigmoid(itr, 3.0 / iterations)
            action = self.decide_action(state)

            next_state, reward = env.act(action, state)
            # print(itr, state, action, next_state, reward, env.done)

            self.updateQ(state, action, next_state, reward)
            state = next_state

    def optimal_path(self, env: Environment):

        state = env.restart()
        steps = [state]
        while not env.done and len(steps) < env.total_states:
            max_reward = env.reward_illegal
            best_action = None
            for action in actions:
                if self.q[(state, action)] >= max_reward:
                    best_action = action
                    max_reward = self.q[(state, action)]
            state, _ = env.act(best_action, state)
            steps.append(state)
        return steps


class ValueIteration:
    def __init__(self, env: Environment, gamma):
        self.env = env
        self.gamma = gamma
        self.V = [[0.0 for _ in range(env.x_max)] for _ in range(env.y_max)]

    def learn(self, margin=0.1):
        while True:
            next_V = deepcopy(self.V)
            for y in range(self.env.y_max):
                for x in range(self.env.x_max):
                    max_reward = self.env.reward_illegal
                    best_action = None
                    for action in actions:
                        next_state, reward = self.env.act(action, (x, y))
                        next_x, next_y = next_state
                        if reward + self.gamma * self.V[next_y][next_x] >= max_reward:
                            max_reward = reward + self.gamma * self.V[next_y][next_x]
                    next_V[y][x] = max_reward
            if self.approx_equal(self.V, next_V, margin):
                self.V = next_V
                break
            else:
                self.V = next_V
        return self.V

    @staticmethod
    def approx_equal(V, next_V, margin):
        total_diff = abs(
            sum([sum(row) for row in V]) - sum([sum(row) for row in next_V])
        )
        print(total_diff)
        return total_diff < margin

    def new_state(self, action, state):
        x, y = state
        match action:
            case "^":
                new_state = x, y - 1
            case "v":
                new_state = x, y + 1
            case "<":
                new_state = x - 1, y
            case ">":
                new_state = x + 1, y
        return new_state

    def print_policy(self):
        pass

    def optimal_path(self, start: Optional[Tuple[int, int]] = None):
        if start is None:
            state = self.env.restart()
        else:
            state = start
        steps = [state]
        while state != self.env.goal and len(steps) < self.env.total_states:
            max_reward = self.env.reward_illegal
            best_action = None

            new_state = None
            next_state = None
            for action in actions:
                new_state = self.new_state(action, state)
                if self.env.is_illegal(state, new_state):
                    continue
                else:
                    new_x, new_y = new_state
                    if self.V[new_y][new_x] >= max_reward:
                        best_action = action
                        next_state = new_state
                        max_reward = self.V[new_y][new_x]
            state = next_state
            steps.append(state)
        return steps


# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".split(
#     "\n"
# )

# Implementation works for sample state-action space, but full space
#  requires more optimization techniques than I feel like implementing
# def pt1():
#     learner = QLearner(alpha=1.0)
#     env = Environment(
#         heightmap=lines, reward_move=-0.1, reward_illegal=-5, reward_goal=100
#     )
#     learner.learn(env, iterations=100000000)
#     print(f"Visited: {len(learner.q)}, unvisited: {env.total_states - len(learner.q)}")
#     # print(sorted(learner.q.items(), key=lambda x: x[1]))

#     steps = learner.optimal_path(env)
#     print(len(steps) - 1)
#     # print(steps)
#     return learner, env, steps


def pt1():

    env = Environment(
        heightmap=lines, reward_move=-0.0, reward_illegal=-5, reward_goal=100
    )
    learner = ValueIteration(env, gamma=0.999)
    learner.learn(margin=0.1)
    # print(f"Visited: {len(learner.q)}, unvisited: {env.total_states - len(learner.q)}")
    # print(sorted(learner.q.items(), key=lambda x: x[1]))

    steps = learner.optimal_path()
    print(len(steps) - 1)
    # print(steps)
    return learner, env, steps


def pt2(learner, env):
    max_a_V = 0
    for y in range(env.y_max):
        for x in range(env.x_max):
            if env[x, y] == "a" and learner.V[y][x] > max_a_V:
                best_a = x, y
                max_a_V = learner.V[y][x]
    steps = learner.optimal_path(best_a)
    print(len(steps) - 1)


if __name__ == "__main__":
    learner, env, steps = pt1()
    pt2(learner, env)
