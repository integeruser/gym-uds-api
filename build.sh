#!/usr/bin/env bash
if [[ ! -z $1 ]] ; then
    PROTOC=$1
else
    PROTOC=$(which protoc)
fi

if [[ ! -z $PROTOC ]] ; then
    $PROTOC --python_out=. gym.proto &&
    $PROTOC --cpp_out=binding-cpp gym.proto &&
    mv binding-cpp/gym.pb.h binding-cpp/include/gym.pb.h &&
    mv binding-cpp/gym.pb.cc binding-cpp/src/gym.pb.cc
fi
