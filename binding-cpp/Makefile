default:
	mkdir -p bin
	clang++ -std=c++11 -O2 -o bin/gym-client -I include -l protobuf \
	src/gym.cc src/gym.pb.cc src/gym-client.cc

clean:
	rm -rf bin/gym-client
