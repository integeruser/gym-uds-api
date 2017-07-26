# gym-uds-api
This project provides a local [Unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket) API to the [OpenAI Gym](https://github.com/openai/gym) toolkit, allowing development in languages other than Python with a much faster interprocess communication than the [gym-http-api](https://github.com/openai/gym-http-api).

Currently, the API only provides the methods `reset()` and `step()` for modifying the Gym environment and `sample()` for sampling from the action space, but it is simple to extend it with any other method needed.

## Requisites
This projects requires any recent version of Google's [Protocol Buffers](https://developers.google.com/protocol-buffers/).

## Installation
1. Clone or download this repository, e.g. `git clone https://github.com/integeruser/gym-uds-api.git`
2. Run `./build.sh` to generate the necessary protobuf headers and sources

## Usage
1. Start the server:
```
/o/gym-uds-api $ python3 ./gym-uds-server.py CartPole-v0
```
2. Run the Python or C++ client:
```
/o/gym-uds-api $ python3 ./gym-uds-client.py
Ep. 1: 53.00
Ep. 2: 12.00
Ep. 3: 39.00
/o/gym-uds-api $ python3 ./gym-uds-client.py
Ep. 1: 31.00
Ep. 2: 16.00
Ep. 3: 10.00
```
```
/o/g/binding-cpp $ make
clang++ -std=c++11 -O2 -o gym-uds-client -I include -l protobuf \
	src/gym.cc src/gym-uds.pb.cc src/gym-uds-client.cc
/o/g/binding-cpp $ ./gym-uds-client
Ep. 1: 17
Ep. 2: 16
Ep. 3: 15
/o/g/binding-cpp $ ./gym-uds-client
Ep. 1: 16
Ep. 2: 12
Ep. 3: 13
```
