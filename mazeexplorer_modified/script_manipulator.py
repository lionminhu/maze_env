# Modified from https://github.com/microsoft/MazeExplorer/blob/e66a2d405e08bc75e51bd38a2b96959c554fe773/mazeexplorer/script_manipulator.py

from string import Template
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))


def write_config(wad, actions, episode_timeout):
    """
    args:
    wad: (str) name of corresponding wad file
    actions: (str) list of available actions (default: "MOVE_FORWARD TURN_LEFT TURN_RIGHT")
    """
    # open the file
    filein = open(os.path.join(dir_path, 'config_template.txt'))
    # read it
    src = Template(filein.read())

    mission_wad = os.path.splitext(os.path.basename(wad))[0]
    d = {'actions': actions, 'mission_wad': mission_wad, 'episode_timeout': episode_timeout}

    # do the substitution
    result = src.substitute(d)

    f = open(wad + ".cfg", "w+")
    f.write(result)
    f.close()

    return wad + ".cfg"


def sample_key_textures(categories):
    key_texture_list = []
    for category in categories.values():
        key_texture_list += random.sample(category, 1)
    return key_texture_list


def write_acs(random_spawn, random_textures, random_key_positions, map_size, number_maps,
              floor_texture, ceilling_texture, wall_texture, key_categories, seed=None):
    """
    args:
    random_spawn: (bool) whether or not agent should be randomly placed in maze at spawn time
    random_textures: (bool) whether or not textures (walls, floors etc.) should be randomised.
    """
    BLOCK_SIZE = 96

    xmin = BLOCK_SIZE / 2
    ymin = BLOCK_SIZE / 2
    xmax = BLOCK_SIZE / 2 + 2 * round(map_size[0] / 2) * BLOCK_SIZE
    ymax = BLOCK_SIZE / 2 + 2 * round(map_size[1] / 2) * BLOCK_SIZE

    if seed:
        random.seed(seed)

    maze_acs = os.path.join(dir_path, "maze.acs")
    if os.path.exists(maze_acs):
        os.remove(maze_acs)

    # open the file
    filein = open(os.path.join(dir_path, 'acs_template.txt'))
    # read it
    src = Template(filein.read())

    with open(os.path.join(dir_path, 'doom_textures.txt')) as textures:
        doom_textures = textures.read().replace(';\n', '')
        num_textures = len(doom_textures.split(','))

    key_texture_list = sample_key_textures(key_categories)
    print('keys used: {}'.format(key_texture_list))
    key_obj_textures = '{"' + '","'.join(key_texture_list) + '"};'
    num_keys = len(key_texture_list)

    # number_key_positions = keys * number_maps

    offset = 48

    keys_spawn = ", ".join(['%.4f' % (random.random()) for _ in range(num_keys)])

    keys_spawn_offset_x = ", ".join(['%.3f' % (random.randint(-offset, offset)) for _ in range(num_keys)])
    keys_spawn_offset_y = ", ".join(['%.3f' % (random.randint(-offset, offset)) for _ in range(num_keys)])

    spawns = ", ".join(['%.4f' % (random.random()) for _ in range(number_maps)])
    spawns_offset_x = ", ".join(['%.3f' % (random.randint(-offset, offset)) for _ in range(number_maps)])
    spawns_offset_y = ", ".join(['%.3f' % (random.randint(-offset, offset)) for _ in range(number_maps)])
    spawns_angle = ", ".join(['%.2f' % (random.random()) for _ in range(number_maps)])

    d = {
        'number_keys': num_keys, 'random_spawn': random_spawn, 'random_textures': random_textures,
        'textures': doom_textures, 'num_textures': num_textures, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax,
        'floor_texture': floor_texture, 'ceilling_texture': ceilling_texture, 'wall_texture': wall_texture,
        'random_key_positions': random_key_positions,
        'number_key_positions': num_keys, 'spawns': spawns, 'number_maps': number_maps,
        'spawns_offset_x': spawns_offset_x, 'spawns_offset_y': spawns_offset_y, 'spawns_angle': spawns_angle,
        'keys_spawn': keys_spawn, 'keys_spawn_offset_x': keys_spawn_offset_x,
        'keys_spawn_offset_y': keys_spawn_offset_y, 'number_keys_maps': num_keys,
        'key_obj_textures': key_obj_textures,
    }

    # do the substitution
    result = src.substitute(d)

    f = open(os.path.join(dir_path, "maze.acs"), "w+")
    f.write(result)
    f.close()
