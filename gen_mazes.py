from random import sample
import os

from mazeenv.mazeexplorer import MazeExplorer

from params import params


if __name__ == '__main__':

    if not os.path.isdir(params.mazes_path_root):
        os.mkdir(params.mazes_path_root)

    for idx in range(params.num_envs):
        maze_path = params.mazes_path_root + str(idx)
        # floor_texture = sample(params.texture_list, 1)
        # ceiling_texture = sample(params.texture_list, 1)
        # wall_texture = sample(params.texture_list, 1)
        seed = params.seed + idx
        MazeExplorer(unique_maps=False,
                     number_maps=1,
                     size=params.map_size,
                     random_spawn=params.random_spawn,
                     random_textures=params.random_textures,
                     random_key_positions=params.random_key_positions,
                     seed=seed,
                     clip=params.reward_clip,
                     floor_texture=params.floor_texture,
                     ceilling_texture=params.ceilling_texture,
                     wall_texture=params.wall_texture,
                     action_frame_repeat=params.action_frame_repeat,
                     scaled_resolution=params.scaled_resolution,
                     episode_timeout=params.episode_timeout,
                     complexity=params.complexity,
                     density=params.density,
                     data_augmentation=params.data_augmentation,
                     mazes_path=maze_path,
                     key_categories=params.key_categories,
                     random_key_textures=params.random_key_textures)
