default:
	mkdir -p bin
	$(CXX) -std=c++11 -O2 -o bin/gym-uds-client -I include `pkg-config --libs protobuf grpc++ grpc` -lgrpc++_reflection -ldl src/*.cc

clean:
	rm -rf bin/gym-uds-client
