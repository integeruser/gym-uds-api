#!/usr/bin/env python
import argparse

import numpy as np

import grpc
import gym_uds_pb2
import gym_uds_pb2_grpc


class EnvironmentClient:
    def __init__(self, sockfilepath):
        channel = grpc.insecure_channel(sockfilepath)
        self.stub = gym_uds_pb2_grpc.EnvironmentStub(channel)
        self.action_space = lambda: None
        self.action_space.sample = self.sample

    def reset(self):
        state_pb = self.stub.Reset(gym_uds_pb2.Empty())
        observation = np.asarray(state_pb.observation.data).reshape(state_pb.observation.shape)
        return observation

    def step(self, action):
        state_pb = self.stub.Step(gym_uds_pb2.Action(value=action))
        observation = np.asarray(state_pb.observation.data).reshape(state_pb.observation.shape)
        return observation, state_pb.reward, state_pb.done

    def sample(self):
        action_pb = self.stub.Sample(gym_uds_pb2.Empty())
        return action_pb.value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sockfilepath",
        nargs="?",
        default="unix:///tmp/gym-uds-socket",
        help="a unique filepath where the Unix domain client will connect",
    )
    args = parser.parse_args()

    env = EnvironmentClient(args.sockfilepath)

    num_episodes = 3
    for episode in range(1, num_episodes + 1):
        observation = env.reset()

        episode_reward = 0
        done = False
        while not done:
            action = env.action_space.sample()
            observation, reward, done = env.step(action)
            episode_reward += reward
        print("Ep. {}: {:.2f}".format(episode, episode_reward))
