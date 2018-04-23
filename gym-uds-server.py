#!/usr/bin/env python3
import argparse
import os
import time
from concurrent import futures

import grpc
import gym
import gym_uds_pb2
import gym_uds_pb2_grpc
import numpy as np

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Environment(gym_uds_pb2_grpc.EnvironmentServicer):
    def __init__(self, env_id):
        self.env = gym.make(env_id)

    def Reset(self, empty_request, context):
        observation = self.env.reset()
        observation_pb = gym_uds_pb2.Observation(data=observation.ravel(), shape=observation.shape)
        return gym_uds_pb2.State(observation=observation_pb, reward=0.0, done=False)

    def Step(self, action_request, context):
        observation, reward, done, _ = self.env.step(action_request.value)
        assert type(observation) is np.ndarray

        observation_pb = gym_uds_pb2.Observation(data=observation.ravel(), shape=observation.shape)
        return gym_uds_pb2.State(observation=observation_pb, reward=reward, done=done)

    def Sample(self, empty_request, context):
        action = self.env.action_space.sample()
        return gym_uds_pb2.Action(value=action)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='the id of the gym environment to simulate')
    parser.add_argument(
        'filepath',
        nargs='?',
        default='unix:///tmp/gym-uds-socket',
        help='a unique filepath where the server will bind')
    args = parser.parse_args()

    try:
        os.remove(args.filepath)
    except FileNotFoundError:
        pass

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    gym_uds_pb2_grpc.add_EnvironmentServicer_to_server(Environment(args.id), server)
    server.add_insecure_port(args.filepath)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
