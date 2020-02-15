import os
os.environ["OMP_NUM_THREADS"] = "1"
import torch.multiprocessing as mp

from eval import test
from params import params


def log_params(params):
    msg = ''

    params_dict = params.__dict__
    for key in params_dict.keys():
        msg += '{}\t{}\n'.format(key, str(params_dict[key]))

    msg += '\n' + '\t'.join(['time', 'mazeId', 'avgReward', 'avgLength', 'successRate']) + '\n'
    csv_path = './log/' + params.log_file + '.csv'
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    if os.path.isfile(csv_path):
        raise ValueError('Log CSV file already exists')
    with open(csv_path, 'a') as file:
        file.write(msg)


def main():
    log_params(params)

    mp.set_start_method('spawn')

    process_num = 0
    num_envs = params.num_envs

    while process_num < num_envs:
        processes = []
        for _ in range(params.n_process):
            p = mp.Process(target=test, args=(process_num, ))
            p.start()
            processes.append(p)
            process_num += 1
            if process_num >= num_envs:
                break
        for p in processes:
            p.join()


if __name__ == "__main__":
    main()
