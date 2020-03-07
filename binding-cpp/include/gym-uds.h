#ifndef GYM_UDS_H
#define GYM_UDS_H

#include <memory>
#include <string>

#include "gym-uds.pb.h"
#include "gym-uds.grpc.pb.h"

class EnvironmentClient
{
private:
    std::unique_ptr<Environment::Stub> stub;

public:
    EnvironmentClient(const std::string &);

    void reset(State *state);
    void step(const Action &action, State *state);

    void sample(Action *action);
};

#endif // GYM_UDS_H
