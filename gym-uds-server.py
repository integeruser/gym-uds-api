#!/usr/bin/env python
import argparse
import os
import time
from concurrent import futures

import gym
import numpy as np

import grpc
import gym_uds_pb2
import gym_uds_pb2_grpc


class EnvironmentServicer(gym_uds_pb2_grpc.EnvironmentServicer):
    def __init__(self, env_id):
        self.env = gym.make(env_id)

    def Reset(self, empty_request, context):
        observation = self.env.reset()
        observation_pb = gym_uds_pb2.Observation(data=observation.ravel(), shape=observation.shape)
        return gym_uds_pb2.State(observation=observation_pb, reward=0.0, done=False)

    def Step(self, action_request, context):
        observation, reward, done, _ = self.env.step(action_request.value)
        observation_pb = gym_uds_pb2.Observation(data=observation.ravel(), shape=observation.shape)
        return gym_uds_pb2.State(observation=observation_pb, reward=reward, done=done)

    def Sample(self, empty_request, context):
        action = self.env.action_space.sample()
        return gym_uds_pb2.Action(value=action)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="the id of the gym environment to simulate")
    parser.add_argument(
        "sockfilepath",
        nargs="?",
        default="unix:///tmp/gym-uds-socket",
        help="a unique filepath where the Unix domain server will bind",
    )
    args = parser.parse_args()

    try:
        os.remove(args.sockfilepath)
    except FileNotFoundError:
        pass

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    gym_uds_pb2_grpc.add_EnvironmentServicer_to_server(EnvironmentServicer(args.id), server)
    server.add_insecure_port(args.sockfilepath)
    server.start()
    server.wait_for_termination()
