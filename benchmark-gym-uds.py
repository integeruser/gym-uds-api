#!/usr/bin/env python3
import timeit


def benchmark(env, MAX_NUM_STEPS=1):
    start = timeit.default_timer()

    num_steps = 0
    benchmark_is_over = False
    while not benchmark_is_over:
        env.reset()

        done = False
        while not done:
            action = env.sample()
            env.step(action)

            num_steps += 1
            if num_steps == MAX_NUM_STEPS:
                benchmark_is_over = True
                break

    end = timeit.default_timer()
    print('%d steps in %f seconds' % (num_steps, end - start))


class UdsEnvironment:
    def __init__(self, sock_filepath):
        self.env = __import__('gym-uds-test-client').Environment(sock_filepath)

    def reset(self):
        return self.env.reset()

    def sample(self):
        return self.env.action_space.sample()

    def step(self, action):
        return self.env.step(action)


if __name__ == '__main__':
    env = UdsEnvironment('/Users/fcagnin/volatile/gym-uds-socket')
    benchmark(env)
