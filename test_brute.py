import retro
import os
from retro.examples.brute import *

def main():
    env = retro.make('Airstriker-Genesis', retro.State.DEFAULT, use_restricted_actions=retro.Actions.DISCRETE)
    brute = Brute(env, 4500)
    best_rew = 0
    obs = env.reset()
    while True:
        acts, rew = brute.run()

        env.reset()
        if rew > best_rew:
            print(best_rew, "->", rew)
#            os.remove("best.bk2")
            env.unwrapped.record_movie("best.bk2")
            for act in acts:
                env.step(act)
                env.render()
            env.unwrapped.stop_record()
        if rew > 150:
            break

    env.close()


if __name__ == "__main__":
    main()






