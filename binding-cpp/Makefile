default:
	mkdir -p bin
	clang++ -std=c++11 -O2 -o bin/gym-uds-client -I include -l protobuf \
	src/gym.cc src/gym-uds.pb.cc src/gym-uds-client.cc

clean:
	rm -rf bin/gym-uds-client
