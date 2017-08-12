#!/usr/bin/env python3
import argparse
import timeit

import gym_http_client  # https://github.com/openai/gym-http-api


class HttpEnvironment:
    def __init__(self, env_id):
        self.client = gym_http_client.Client('http://127.0.0.1:5000')
        self.instance_id = self.client.env_create(env_id)

    def reset(self):
        return self.client.env_reset(self.instance_id)

    def sample(self):
        return self.client.env_action_space_sample(self.instance_id)

    def step(self, action):
        return self.client.env_step(self.instance_id, action)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('env_id')
    args = parser.parse_args()

    env = HttpEnvironment(args.env_id)
    benchmark_gym_uds = __import__('benchmark-gym-uds')
    benchmark_gym_uds.benchmark(env)
