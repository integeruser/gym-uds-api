#!/usr/bin/env python3
import os
import socket

import gym

import gym_pb2


def recv_action():
    action_pb = conn.recv(int.from_bytes(conn.recv(1), byteorder='little'))
    action = gym_pb2.Action()
    action.ParseFromString(action_pb)
    return action.value


def send_state(observation, reward, done):
    state_pb = gym_pb2.State(value=observation, reward=reward, done=done).SerializeToString()
    conn.sendall(len(state_pb).to_bytes(1, byteorder='little') + state_pb)


if __name__ == '__main__':
    socket_filepath = '/tmp/gym-server-socket'
    try:
        os.remove(socket_filepath)
    except FileNotFoundError:
        pass

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(socket_filepath)
    sock.listen()

    env = gym.make('CartPole-v0')
    while True:
        conn, _ = sock.accept()
        observation = env.reset()
        send_state(observation, 0.0, False)

        done = False
        while not done:
            action = recv_action()
            observation, reward, done, _ = env.step(action)
            send_state(observation, float(reward), bool(done))
