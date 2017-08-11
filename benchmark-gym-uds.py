#!/usr/bin/env python3
import timeit

MAX_NUM_STEPS = 1

env = __import__('gym-uds-test-client').Environment('/tmp/gym-uds-socket')

start = timeit.default_timer()

num_steps = 0
benchmark_is_over = False
while not benchmark_is_over:
    env.reset()

    done = False
    while not done:
        action = env.action_space.sample()
        start = timeit.default_timer()
        o, _, done = env.step(action)
        end = timeit.default_timer()
        print('gg', end-start)

        num_steps += 1
        if num_steps == MAX_NUM_STEPS:
            benchmark_is_over = True
            break

end = timeit.default_timer()
print('%d steps in %f seconds' % (num_steps, end - start))
