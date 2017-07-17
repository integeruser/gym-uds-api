#!/usr/bin/env bash
protoc --python_out=. gym.proto
protoc --cpp_out=binding-cpp gym.proto
mv binding-cpp/gym.pb.h binding-cpp/include/gym.pb.h
mv binding-cpp/gym.pb.cc binding-cpp/src/gym.pb.cc
