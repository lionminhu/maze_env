from random import sample
from collections import OrderedDict
import os

from mazeenv.mazeexplorer import MazeExplorer


class GenMazesParams:
    def __init__(self):
        self.num_envs = 80
        self.map_size = (10, 10)
        self.random_spawn = True
        self.random_textures = False
        self.mazes_path_root = './mazes_dir/'
        self.random_key_positions = False
        self.key_categories = OrderedDict({
            'Card': ['RedCard', 'BlueCard', 'YellowCard'],
            'Armor': ['GreenArmor', 'BlueArmor'],
            'Skull': ['RedSkull', 'BlueSkull', 'YellowSkull'],
            'Gun': ['Shotgun', 'Chaingun'],
            'Bonus': ['HealthBonus', 'ArmorBonus'],
        })
        self.maze_generation_seed = None
        self.reward_clip = (-1, 1)
        self.action_frame_repeat = 4
        self.scaled_resolution = (42, 42)
        self.episode_timeout = 400
        self.complexity = 0.7
        self.density = 0.7
        self.data_augmentation = False
        self.texture_list = ['ASHWALL2', 'ASHWALL3', 'ASHWALL4', 'ASHWALL6', 'ASHWALL7', 'BFALL1', 'BFALL2', 'BFALL3', 'BFALL4', 'BIGBRIK1', 'BIGBRIK2', 'BIGBRIK3', 'BIGDOOR2', 'BIGDOOR3', 'BIGDOOR4', 'BIGDOOR5', 'BLAKWAL1', 'BLAKWAL2', 'BRICK1', 'BRICK10', 'BRICK11', 'BRICK12', 'BRICK2', 'BRICK3', 'BRICK4', 'BRICK5', 'BRICK6', 'BRICK7', 'BRICK8', 'BRICK9', 'BRICKLIT', 'BRONZE1', 'BRONZE2', 'BRONZE3', 'BRONZE4', 'BROVINE2', 'BROWN1', 'BROWN144', 'BROWN96', 'BROWNGRN', 'BROWNHUG', 'BROWNPIP', 'BRWINDOW', 'BSTONE1', 'BSTONE2', 'BSTONE3', 'CEMENT1', 'CEMENT2', 'CEMENT3', 'CEMENT4', 'CEMENT5', 'CEMENT6', 'CEMENT7', 'CEMENT9', 'COMPBLUE', 'COMPSPAN', 'COMPSTA1', 'COMPSTA2', 'COMPTALL', 'COMPWERD', 'CRACKLE2', 'CRACKLE4', 'CRATE1', 'CRATE2', 'CRATE3', 'CRATELIT', 'CRATWIDE', 'DOORBLU', 'DOORRED', 'DOORSTOP', 'DOORTRAK', 'DOORYEL', 'FIREWALA', 'FIREWALB', 'FIREWALL', 'GRAY1', 'GRAY4', 'GRAY5', 'GRAYBIG', 'GRAYVINE', 'GSTONE1', 'GSTONE2', 'GSTVINE1', 'GSTVINE2', 'ICKWALL1', 'ICKWALL2', 'ICKWALL3', 'LITE3', 'LITE5', 'LITEBLU1', 'LITEBLU4', 'MARBGRAY', 'MARBLE1', 'MARBLE2', 'MARBLE3', 'MARBLOD1', 'METAL', 'METAL1', 'METAL2', 'METAL3', 'METAL4', 'METAL5', 'METAL6', 'METAL7', 'MODWALL1', 'MODWALL2', 'MODWALL4', 'NUKEDGE1', 'PANBOOK', 'PANBORD1', 'PANBORD2', 'PANCASE1', 'PANCASE2', 'PANEL1', 'PANEL2', 'PANEL4', 'PANEL5', 'PANEL6', 'PANEL7', 'PANEL8', 'PANEL9', 'PIPE1', 'PIPE2', 'PIPE4', 'PIPE6', 'PIPEWAL1', 'PIPEWAL2', 'PLAT1', 'REDWALL', 'ROCK1', 'ROCK2', 'ROCK3', 'ROCK4', 'ROCK5', 'ROCKRED1', 'ROCKRED2', 'SFALL1', 'SFALL2', 'SFALL3', 'SFALL4', 'SHAWN2', 'SILVER1', 'SILVER2', 'SILVER3', 'SKIN2', 'SK_LEFT', 'SK_RIGHT', 'SLADWALL', 'SPACEW2', 'SPACEW3', 'SPACEW4', 'SPCDOOR1', 'SPCDOOR2', 'SPCDOOR3', 'SPCDOOR4', 'SP_HOT1', 'STARBR2', 'STARG1', 'STARG2', 'STARG3', 'STARGR1', 'STARGR2', 'STARTAN2', 'STARTAN3', 'STONE', 'STONE2', 'STONE3', 'STONE4', 'STONE5', 'STONE6', 'STONE7', 'STUCCO', 'STUCCO1', 'SUPPORT2', 'SUPPORT3', 'TANROCK2', 'TANROCK3', 'TANROCK4', 'TANROCK5', 'TANROCK7', 'TANROCK8', 'TEKBRON1', 'TEKBRON2', 'TEKGREN1', 'TEKGREN2', 'TEKGREN3', 'TEKGREN4', 'TEKGREN5', 'TEKLITE', 'TEKLITE2', 'TEKWALL1', 'TEKWALL4', 'TEKWALL6', 'WOOD1', 'WOOD12', 'WOOD3', 'WOOD5', 'WOOD6', 'WOOD7', 'WOOD8', 'WOOD9', 'WOODMET1', 'WOODVERT', 'ZDOORB1', 'ZDOORF1', 'ZELDOOR', 'ZIMMER2', 'ZIMMER5', 'ZIMMER7', 'ZIMMER8', 'ZZWOLF1', 'ZZWOLF10', 'ZZWOLF11', 'ZZWOLF5', 'ZZWOLF9', 'ZZZFACE6', 'ZZZFACE7', 'ZZZFACE8', 'ZZZFACE9']
        self.floor_texture = 'CEIL5_2'
        self.ceilling_texture = 'CEIL5_1'
        self.wall_texture = 'STONE2'


if __name__ == '__main__':
    params = GenMazesParams()

    if not os.path.isdir(params.mazes_path_root):
        os.mkdir(params.mazes_path_root)

    for idx in range(params.num_envs):
        maze_path = params.mazes_path_root + str(idx)
        # floor_texture = sample(params.texture_list, 1)
        # ceiling_texture = sample(params.texture_list, 1)
        # wall_texture = sample(params.texture_list, 1)
        MazeExplorer(unique_maps=False,
                     number_maps=1,
                     size=params.map_size,
                     random_spawn=params.random_spawn,
                     random_textures=params.random_textures,
                     random_key_positions=params.random_key_positions,
                     seed=params.maze_generation_seed,
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
                     key_categories=params.key_categories)

