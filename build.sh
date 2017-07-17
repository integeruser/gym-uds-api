#!/usr/bin/env bash
protoc --python_out={server,client-python} gym.proto
protoc --cpp_out=client-cc gym.proto
mv client-cc/gym.pb.h client-cc/include/gym.pb.h
mv client-cc/gym.pb.cc client-cc/src/gym.pb.cc
