#!/usr/bin/env python3
import socket

import gym_pb2


class Environment:
    def __init__(self, socket_filepath):
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.connect(socket_filepath)

    def _recv_message(self, cls):
        message_pb_len = int.from_bytes(self.socket.recv(1), byteorder='little')
        message_pb = self.socket.recv(message_pb_len)
        message = cls()
        message.ParseFromString(message_pb)
        return message

    def _send_message(self, message):
        message_pb = message.SerializeToString()
        self.socket.sendall(len(message_pb).to_bytes(1, byteorder='little'))
        self.socket.sendall(message_pb)

    def reset(self):
        self._send_message(gym_pb2.Request(type=gym_pb2.Request.RESET))
        state = self._recv_message(gym_pb2.State)
        return state.observation, state.reward, state.done

    def step(self, action):
        self._send_message(gym_pb2.Request(type=gym_pb2.Request.STEP))
        self._send_message(gym_pb2.Action(value=action))
        state = self._recv_message(gym_pb2.State)
        return state.observation, state.reward, state.done


if __name__ == '__main__':
    env = Environment('/tmp/gym-server-socket')

    num_episodes = 3
    for episode in range(num_episodes):
        observation, _, _ = env.reset()

        done = False
        while not done:
            action = 1
            observation, reward, done = env.step(action)
            print(observation, reward, done)
