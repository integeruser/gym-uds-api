#ifndef GYM_H
#define GYM_H

#include <string>
#include <tuple>
#include <vector>

#include <grpcpp/grpcpp.h>

#include "gym-uds.pb.h"
#include "gym-uds.grpc.pb.h"

namespace gym_uds
{
using action_t = int;
using observation_t = std::vector<float>;
using state_t = std::tuple<observation_t, float, bool>;


class EnvironmentClient
{
    private:
        std::unique_ptr<Environment::Stub> stub;

    public:
        EnvironmentClient(const std::string&);

        observation_t reset();
        state_t step(const action_t&);

        action_t sample();
};
}

#endif
