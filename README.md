# Game of Life Sandbox

> Cellular automatas rule


<!-- Project Shields -->
![contributors](https://img.shields.io/github/contributors/danmohedano/game_of_life.svg?style=flat-square) [![license](https://img.shields.io/github/license/danmohedano/game_of_life.svg?style=flat-square)](https://github.com/danmohedano/game_of_life/blob/main/LICENSE) ![stars](https://img.shields.io/github/stars/danmohedano/game_of_life.svg?style=flat-square) ![forks](https://img.shields.io/github/forks/danmohedano/game_of_life.svg?style=flat-square) [![PRs welcome](https://img.shields.io/badge/PRs-welcome!-green.svg)](https://github.com/danmohedano/game_of_life/issues)

<!-- TOC -->
## Table of Contents

- [But why?](#but-why)
- [But how (do I use it)?](#but-how-do-i-use-it)
- [But what?](#but-what)
- [But how (does it work)?](#but-how-does-it-work)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## But why?

The [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is probably the most famous cellular automata in the world, originally devised by John Conway. With some very simple rules it is able to create greate structures. I wanted to use it as an opportunity to practice my Python skills and learn the [pygame](https://www.pygame.org/news) library. 

## But how (do I use it)?

### Dependencies

The dependencies are listed in the [`requirements.txt`](https://github.com/danmohedano/game_of_life/blob/main/requirements.txt) file. These can be installed by simply executing: 

```  
$ pip install -r requirements.txt
```

### Running

```
$ python main.py
```

The execution can be configured by modifying the variables present in [`config.py`](https://github.com/danmohedano/game_of_life/blob/main/config.py).

## But what?

The project features both the game logic and a very simple representation of the state of the automata. A [camera module](https://github.com/danmohedano/game_of_life/blob/main/camera) has also been implemented to aid with the visualization.

![screenshot](https://user-images.githubusercontent.com/43313293/121348779-0e8e9700-c929-11eb-9a85-b91fd5963882.png)

A file can be used to prepopulate the grid with alive cells. Once the program is running, the user has the following options to control the display:

- `<up>`, `<down>`, `<left>`, `<right>`: allow the user to move the camera in the grid.
- `<z>`, `<x>`: allow the user to zoom in and out.
- `<space>`: pause/resume the execution.
- `<mouse-click>`: allows the user to change the value of cells by clicking on them.


## But how (does it work)?

Game of Life's universe is represented as a two-dimensional grid formed by squared cells. Each cell can be in one of two possible states, alive or dead. In each iteration of the simulation, each cell interacts with its immediate neighbours with the following rules:

- Any alive cell with two or three alive neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other alive cells die in the next generation, and all other dead cells stay dead.

## Roadmap

See the [open issues](https://github.com/danmohedano/game_of_life/issues) for a full list of proposed features (and known issues). 

## Contributing

If you have ideas on how to improve the project, go ahead!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the [license_name](https://github.com/danmohedano/game_of_life/blob/main/LICENSE) license © [danmohedano](https://github.com/danmohedano)
