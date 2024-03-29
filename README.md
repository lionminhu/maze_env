# MazeEnv

This repository contains the maze scenario where an agent must learn to navigate within randomly generated maze environments to obtain target objects and avoid non-target objects scattered within the map.

## Installation and Running Random Agent

1. To run the random agent, MazeExplorer must be installed. Please follow [this link](https://github.com/microsoft/MazeExplorer#installation) for installation.
2. Other requirements can be installed as below:
```
pip3 install numpy torch
pip3 install setproctitle
```

3. `gen_mazes.py` generates maze config files and WAD files in `mazes_dir/` directory.
```
python gen_mazes.py
```

4. `main.py` runs the random agent with multiprocessing. Prior to running `main.py`, the `log_file` of `class Params` in `params.py` must be changed to a nonexisting file name. The raw data will be saved to the CSV file of the specified `log_file` path.
```
python main.py
```

## References

Significant portion of environment code and scripts under `mazeenv` directory are modified versions of `microsoft/MazeExplorer` repository ([link](https://github.com/microsoft/MazeExplorer)). The copyright notice is included in `NOTICE`.

`main.py` and `eval.py` are modified versions of the corresponding scripts in the `kibeomKim/House3D_baseline` repository ([link](https://github.com/kibeomKim/House3D_baseline)).
