#!/usr/bin/env bash
cd $(dirname $(realpath $0))

if [[ ! -z $1 ]] ; then
    PROTOC=$1
else
    PROTOC=$(which protoc)
fi

GRPC_CPP_PLUGIN_PATH=$(which grpc_cpp_plugin)

if [[ ! -z $PROTOC ]] ; then
    $PROTOC --python_out=. gym-uds.proto &&
    $PROTOC --cpp_out=. gym-uds.proto &&
    $PROTOC --grpc_out=. --plugin=protoc-gen-grpc=$GRPC_CPP_PLUGIN_PATH gym-uds.proto &&
    mv gym-uds.pb.h binding-cpp/include/ &&
    mv gym-uds.grpc.pb.h binding-cpp/include/ &&
    mv gym-uds.pb.cc binding-cpp/src/ &&
    mv gym-uds.grpc.pb.cc binding-cpp/src/
else
    echo "protoc not found!"
    exit 1
fi
