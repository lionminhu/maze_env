import os
from setproctitle import setproctitle as ptitle
import time
import logging
import random

from mazeenv.mazeexplorer import MazeExplorer
from vizdoom import GameVariable
from gen_mazes import GenMazesParams


gen_mazes_params = GenMazesParams()

actions = list(range(3))  # MOVE_FORWARD TURN_LEFT TURN_RIGHT
targets = list(gen_mazes_params.key_categories.keys())


def test(rank, params, train_set=True):
    if not os.path.exists('./log'):
        os.mkdir('./log')
    logging.basicConfig(filename='./log/'+params.log_file+'.log', level=logging.INFO)
    ptitle('Test Agent: {}'.format(rank))
    # gpu_id = params.gpu_ids_test[rank % len(params.gpu_ids_test)]

    maze_id = rank
    maze_path = gen_mazes_params.mazes_path_root + str(maze_id)

    env = MazeExplorer.load_vizdoom_env(maze_path, 1,
                                        gen_mazes_params.action_frame_repeat,
                                        gen_mazes_params.scaled_resolution)

    start_time = time.time()

    max_episode = params.max_episode

    eval = []
    for episode in range(max_episode):
        next_observation = env.reset()
        target = int(env.env.get_game_variable(GameVariable.USER5))

        step, total_rew, good = 0, 0.0, 0
        done = False

        while not done:
            observation = next_observation
            act = random.randrange(len(actions))

            next_observation, rew, done, info = env.step(actions[act])
            total_rew += rew

            if rew == 1.0:   # success
                good = 1

            step += 1

            if done:
                eval.append((step, total_rew, good))
                break

    succ = [e for e in eval if e[2] > 0]
    succ_rate = (len(succ) / len(eval)) * 100
    avg_reward = sum([e[1] for e in eval]) / len(eval)
    avg_length = sum([e[0] for e in eval]) / len(eval)
    msg = " ".join([
        "++++++++++ Task Stats +++++++++++\n",
        "Time {}\n".format(time.strftime("%dd %Hh %Mm %Ss", time.gmtime(time.time() - start_time))),
        "Episode Played: {:d}\n".format(len(eval)),
        "Maze id: {:d}\n".format(maze_id),
        "Avg Reward = {:5.3f}\n".format(avg_reward),
        "Avg Length = {:.3f}\n".format(avg_length),
        "Success rate {:3.2f}%".format(succ_rate)
    ])
    print(msg)
    logging.info(msg)

    msg = '\t'.join([
        str(time.time() - start_time),
        str(maze_id),
        str(avg_reward),
        str(avg_length),
        str(succ_rate)
    ]) + '\n'
    csv_path = './log/' + params.log_file + '.csv'
    with open(csv_path, 'a') as file:
        file.write(msg)
