#!/usr/bin/env python3
import socket

import gym

import gym_pb2


def run(sock, conn):
    env = gym.make('CartPole-v0')

    observation = env.reset()
    send_state(observation, 0.0, False)

    done = False
    while not done:
        action = recv_action()
        observation, reward, done, _ = env.step(action)
        send_state(observation, float(reward), bool(done))


def recv_action():
    action_pb_len = int.from_bytes(conn.recv(1), byteorder='little')
    action_pb = conn.recv(action_pb_len)

    action = gym_pb2.Action()
    action.ParseFromString(action_pb)
    return action.value


def send_state(observation, reward, done):
    state_pb = gym_pb2.State(value=observation, reward=reward, done=done).SerializeToString()
    conn.sendall(len(state_pb).to_bytes(1, byteorder='little'))
    conn.sendall(state_pb)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind('/tmp/gym-server-socket')
    sock.listen(0)

    conn, _ = sock.accept()
    run(sock, conn)
