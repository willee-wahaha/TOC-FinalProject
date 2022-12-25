# TOC-FinalProject
 
## Requirement

- python 3.10.8  
- Visual Studio C/C++
- graphviz(version > 2.24.0)(remember add graphviz to PATH)  
- pipenv

## Build enviroment  
need to install Requirement before build enviroment  

    pipenv shell  
    pip install -r requirements.txt  
    python -m pip install --global-option=build_ext `
              --global-option="-IC:\Program Files\Graphviz\include" `
              --global-option="-LC:\Program Files\Graphviz\lib" `
              pygraphviz

## Run

    python app.py

or

    python3 app.py

## How to use
![GITHUB](https://github.com/willee-wahaha/TOC-FinalProject/blob/main/fsm.png)

The initial state is "user"  
#### there is three command in "user"
- `new game`  
  enter the "new_game" state  
  this state will reset all the data
  
- `load game`  
  enter the "load_game" state  
  this state will load the saved data

- `show fsm`  
  enter the "draw" state  
  ths state will draw a FSM Diagram and show it, then go back to "user"
  
In "new_game" and "load_game", say `play` can enter the "in_game" state, it means starting the game  
#### there is some command in "in_game"

- `load game`  
  enter the "load_game" state  
  this state will load the saved data
  
- `quit game`  
  enter the "no_save" state  
  this state is just check if you want to exit the game without save

- `save`  
  enter the "new_game" state  
  this state will save the data
  
- `create`  
  enter the "create_player" state  
  this state will create a new character with level 1 and rewrite current character
  
- `find monster`  
  enter the "meet_monster" state  
  this state will create a new monster with random level and rewrite current monster
  
- `show my photo`  
  enter the "output_image" state  
  ths state will show the image of the character, then go back to "in_game"

- `fight`  
  enter the "fighting" state  
  ths state will randomly decide your character win or lose, then go back to "in_game"
  

In "save" and "no_save", say `quit game` can go to "user" state

In "save", "no_save", "create_player" and "meet_monster", say `play` can enter the "in_game" state  

In "create_player" and "meet_monster", you also can enter "load_game", "save" and "no_save" by saying the same word  
  
In "create_player" state you also can enter "create_player", "output_image" and "meet_monster" by saying the same word  
  
In "meet_monster" state you also can enter "meet_monster" and "fighting" by saying the same word  

