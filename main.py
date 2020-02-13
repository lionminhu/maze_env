import os
os.environ["OMP_NUM_THREADS"] = "1"
import torch.multiprocessing as mp

from eval import test
from gen_mazes import GenMazesParams

class Params():
    def __init__(self):
        self.n_process = 30
        self.max_episode = 1000
        self.gpu_ids_test = [0]
        self.seed = 1
        self.semantic_mode = False  # if false, RGB mode on
        self.log_file = 'log1'


def log_params(params, gen_mazes_params):
    msg = ''

    params_dict = params.__dict__
    for key in params_dict.keys():
        msg += '{}\t{}\n'.format(key, str(params_dict[key]))

    msg += '\n'

    gen_mazes_params_dict = gen_mazes_params.__dict__
    for key in gen_mazes_params_dict.keys():
        msg += '{}\t{}\n'.format(key, str(gen_mazes_params_dict[key]))

    msg += '\n' + '\t'.join(['time', 'mazeId', 'avgReward', 'avgLength', 'successRate']) + '\n'
    csv_path = './log/' + params.log_file + '.csv'
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    if os.path.isfile(csv_path):
        raise ValueError('Log CSV file already exists')
    with open(csv_path, 'a') as file:
        file.write(msg)


def main():
    params = Params()
    gen_mazes_params = GenMazesParams()

    log_params(params, gen_mazes_params)

    mp.set_start_method('spawn')

    process_num = 0
    num_envs = gen_mazes_params.num_envs

    while process_num < num_envs:
        processes = []
        for _ in range(params.n_process):
            p = mp.Process(target=test, args=(process_num, params,))
            p.start()
            processes.append(p)
            process_num += 1
            if process_num >= num_envs:
                break
        for p in processes:
            p.join()


if __name__ == "__main__":
    main()
