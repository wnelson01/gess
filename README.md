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

Bugs:
doesn't allow starting piece centers that are off the 18x18 board (this is necessary to move stones that are on the edge of the "playable" area). 

Allows moves that have opponent stones in the footprint.  
