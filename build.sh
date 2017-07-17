#!/usr/bin/env bash
if [[ ! -z $1 ]] ; then
    PROTOC=$1
else
    PROTOC=$(which protoc)
fi

if [[ ! -z $PROTOC ]] ; then
    $PROTOC --python_out=. gym-uds.proto &&
    $PROTOC --cpp_out=. gym-uds.proto
    mv gym-uds.pb.h binding-cpp/include/ &&
    mv gym-uds.pb.cc binding-cpp/src
fi
