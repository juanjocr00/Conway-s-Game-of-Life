# Conway's Game of Life
Conway's Game of Life by Juan José Creus Ramos (2019)

This code was a college assignment for a Python course.

The Game of Life was invented by mathematician John Conway in 1970. His goal was to create a system that simulates life and its unpredictable nature. The way it represents life is very simple. A grid of cells, some are alive, some are dead. Each cell has eight neighboring cells, vertically, horizontally and on the diagonals. This seemingly simple system can generate complex and unpredictable patterns thanks to a few simple rules.

Conway tried applying many different rules, some of which caused the cells to die very early and some of which caused them to never die. The rules in the final version of the game maintain a balance. This makes it very difficult to tell at first glance whether a group of cells will live or die after a certain time.

![Vida](https://user-images.githubusercontent.com/108018294/220268369-6950df64-2ae8-49e3-b655-a0a63883755c.gif)

## Game Rules
The rules of the game are as follows:

- If a cell is alive and has two or three living neighbors, it survives.

- If a cell is dead and has three live neighbors, it is born.

- If a cell is alive and has more than three live neighbors, it dies.


This process can run indefinitely.


![Gospers_glider_gun](https://user-images.githubusercontent.com/108018294/220268857-a0cc4493-249d-41f7-a47a-760b2a6e36ac.gif)
