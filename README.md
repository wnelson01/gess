# gess
Go + Chess Hybrid

A combination of Go + Chess

https://en.wikipedia.org/wiki/Gess

Here's a very simple example of how the class could be used:
```
game = GessGame()
move_result = game.make_move('m3', 'm6')
game.make_move('e14', 'g14')
state = game.get_game_state()
game.resign_game()
```
