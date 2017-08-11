#!/usr/bin/env python3
import timeit

import gym_http_client  # https://github.com/openai/gym-http-api

MAX_NUM_STEPS = 1

client = gym_http_client.Client('http://127.0.0.1:5000')
instance_id = client.env_create('Pong-v0')

start = timeit.default_timer()

num_steps = 0
benchmark_is_over = False
while not benchmark_is_over:
    client.env_reset(instance_id)

    done = False
    while not done:
        action = client.env_action_space_sample(instance_id)
        o, _, done, _ = client.env_step(instance_id, action)
        print(o)

        num_steps += 1
        if num_steps == MAX_NUM_STEPS:
            benchmark_is_over = True
            break

end = timeit.default_timer()
print('%d steps in %f seconds' % (num_steps, end - start))
