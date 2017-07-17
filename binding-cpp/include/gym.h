#ifndef GYM_H
#define GYM_H

#include <string>
#include <tuple>
#include <vector>

namespace gym
{
using action_t = int;

using observation_t = std::vector<float>;
using reward_t = float;
using done_t = bool;
using state_t = std::tuple<observation_t, reward_t, done_t>;


class Environment
{
    private:
        int sock, conn;

        template<typename T>
        T recv_message();

        template<typename T>
        void send_message(const T&);

    public:
        Environment(const std::string&);

        observation_t reset();
        state_t step(const action_t&);

        action_t sample();
};
}

#endif
