# pyoneer

So far our cells matrix is relatively simple, it contains only an int and that tells you if the player is there or not.

In this step, we'll introduce complex cells in order to handle more. The cell will be able to contain objects, and will have walls. For now the walls will be initialised as expected, no fancy maze or whatever, but the movement will be restricted by the walls and not by the position.

The map will still be static and hardcoded, we'll keep that fun for later.

The game will tell you what you see, walls and objects.

Bonus just for fun, get one random wall down, and you win the game if you can get outside the map!

![example](https://raw.githubusercontent.com/PiTiLeZarD/pyoneer/step_2/example.png)