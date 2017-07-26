#!/usr/bin/env python3


def recv_exactly(socket, n):
    data = bytearray()
    while len(data) < n:
        packet = socket.recv(n - len(data))
        data.extend(packet)
        if len(packet) == 0: break
    return bytes(data)


def recv_message(socket, cls):
    message_len = int.from_bytes(recv_exactly(socket, 3), byteorder='little')
    message_bytes = recv_exactly(socket, message_len)
    message = cls()
    message.ParseFromString(message_bytes)
    return message


def send_message(socket, message):
    message_bytes = message.SerializeToString()
    message_len = len(message_bytes).to_bytes(3, byteorder='little')
    socket.sendall(message_len)
    socket.sendall(message_bytes)
