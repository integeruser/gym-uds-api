#include <cassert>
#include <string>

#include "gym-uds.h"

#include <grpcpp/grpcpp.h>

EnvironmentClient::EnvironmentClient(const std::string &sockfilepath)
    : stub(Environment::NewStub(grpc::CreateChannel(sockfilepath, grpc::InsecureChannelCredentials())))
{
}

void EnvironmentClient::reset(State *state)
{
    grpc::ClientContext context;
    Empty empty;
    grpc::Status status = stub->Reset(&context, empty, state);
    assert(status.ok());
}
void EnvironmentClient::step(const Action &action, State *state)
{
    grpc::ClientContext context;
    grpc::Status status = stub->Step(&context, action, state);
    assert(status.ok());
}

void EnvironmentClient::sample(Action *action)
{
    grpc::ClientContext context;
    Empty empty;
    grpc::Status status = stub->Sample(&context, empty, action);
    assert(status.ok());
}
