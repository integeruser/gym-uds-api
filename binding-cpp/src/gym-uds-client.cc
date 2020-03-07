#include <cstdlib>
#include <iostream>

#include "gym-uds.h"
#include "gym-uds.pb.h"
#include "gym-uds.grpc.pb.h"

int main(int argc, char const *argv[])
{
    GOOGLE_PROTOBUF_VERIFY_VERSION;

    auto env = EnvironmentClient("unix:///tmp/gym-uds-socket");

    const int num_episodes = 3;
    for (int episode = 1; episode <= num_episodes; ++episode)
    {
        State state;
        env.reset(&state);

        float episode_reward = 0.0f;
        while (!state.done())
        {
            Action action;
            env.sample(&action);

            env.step(action, &state);
            episode_reward += state.reward();
        }
        std::cout << "Ep. " << episode << ": " << episode_reward << std::endl;
    }

    return EXIT_SUCCESS;
}
