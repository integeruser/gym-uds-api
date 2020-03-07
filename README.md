# gym-uds-api
This project presents a basic API for interacting with [OpenAI Gym](https://github.com/openai/gym) environments in languages other than Python through the [gRPC](https://grpc.io) framework and local Unix domain sockets.

The API comes with a C++ binding example which supports one-dimensional observation spaces of type `Box` and action spaces of type `Discrete` (suitable, for example, for the CartPole-v0 environment).

## Requisites
Example instructions are provided for macOS (tested on macOS Catalina 10.15.3).

0. Install [Homebrew](https://brew.sh).

1. Install pkg-config:

        ~$ brew install pkg-config

1. Install [protobuf](https://github.com/protocolbuffers/protobuf):

        ~$ brew install protobuf

1. Install gRPC:

        ~$ brew install grpc

1. Install the grpcio_tools, [NumPy](https://numpy.org) and [OpenAI Gym](https://github.com/openai/gym) pip packages (for Python 3):

        ~$ pip install grpcio_tools numpy gym

## Installation
1. Clone this repository:

        ~$ git clone https://github.com/integeruser/gym-uds-api

1. `cd` to the `gym-uds-api` directory and generate the gRPC headers and sources for the Python server and client:

        gym-uds-api$ python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./gym-uds.proto

1. To build the C++ example client, generate the gRPC headers and sources for C++ and move them to the `binding-cpp` directory:

        gym-uds-api$ protoc -I=. --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc=$(which grpc_cpp_plugin) ./gym-uds.proto
        gym-uds-api$ mv ./gym-uds.pb.h binding-cpp/include/
        gym-uds-api$ mv ./gym-uds.pb.cc binding-cpp/src/
        gym-uds-api$ mv ./gym-uds.grpc.pb.h binding-cpp/include/
        gym-uds-api$ mv ./gym-uds.grpc.pb.cc binding-cpp/src/

## Usage
1. Start the Python server:

        gym-uds-api$ python ./gym-uds-server.py CartPole-v0

1. On a second terminal, execute the dummy Python client:

        gym-uds-api$ python ./gym-uds-test-client.py
        Ep. 1: 15.00
        Ep. 2: 12.00
        Ep. 3: 20.00

1. Alternatively, on a second terminal, `cd` to the `binding-cpp` directory, then build and execute the dummy C++ client:

        gym-uds-api/binding-cpp$ make
        gym-uds-api/binding-cpp$ bin/gym-uds-client
        Ep. 1: 19
        Ep. 2: 13
        Ep. 3: 10
