CXXFLAGS=-std=c++11 -O2 -march=native -Wall
ifeq ($(shell uname | cut -f 1 -d_),Darwin)
LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++`\
			-pthread\
			-lgrpc++_reflection\
			-ldl
else
LDFLAGS += -L/usr/local/lib `pkg-config --libs protobuf grpc++`\
			-pthread\
			-Wl,--no-as-needed -lgrpc++_reflection -Wl,--as-needed\
			-ldl
endif

default:
	mkdir -p bin
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o bin/gym-uds-client \
		-I include \
		src/gym-uds.pb.cc src/gym-uds-client.cc src/gym-uds.grpc.pb.cc src/gym-uds.cc

clean:
	rm -rf bin/gym-uds-client
