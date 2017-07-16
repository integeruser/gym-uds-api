#!/usr/bin/env python3
import socket

import gym_pb2


def recv_state():
    state_pb_len = int.from_bytes(sock.recv(1), byteorder='little')
    state_pb = sock.recv(state_pb_len)

    state = gym_pb2.State()
    state.ParseFromString(state_pb)
    return state.value, state.reward, state.done


def send_action(action):
    action_pb = gym_pb2.Action(value=action).SerializeToString()
    sock.sendall(len(action_pb).to_bytes(1, byteorder='little'))
    sock.sendall(action_pb)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('/tmp/gym-server-socket')

    observation, _, _ = recv_state()

    done = False
    while not done:
        send_action(0)
        observation, reward, done = recv_state()
        print(observation, reward, done)
