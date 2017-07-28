#!/usr/bin/env bash
cd $(dirname $(realpath $0))

PROTOC=$(which protoc)
if [[ ! -z $PROTOC ]] ; then
    $PROTOC --python_out=. gym-uds.proto &&
    $PROTOC --cpp_out=. gym-uds.proto &&
    mv gym-uds.pb.h binding-cpp/include/ &&
    mv gym-uds.pb.cc binding-cpp/src/
else
    echo "protoc not found!"
    exit 1
fi
