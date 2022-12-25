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
  
In "new_game" and "load_game" say `play` can enter the "in_game" state, it means starting the game  
#### there is some command in "in_game"

- `load game`  
  enter the "load_game" state  
  this state will load the saved data
  
- `quit game`  
  enter the "load_game" state  
  this state will load the saved data

- `save`  
  enter the "new_game" state  
  this state will reset all the data
  
- `create`  
  enter the "load_game" state  
  this state will load the saved data
  
- `find monster`  
  enter the "load_game" state  
  this state will load the saved data
  
- `show my photo`  
  enter the "draw" state  
  ths state will draw a FSM Diagram and show it, then go back to "user"

- `fight`  
  enter the "draw" state  
  ths state will draw a FSM Diagram and show it, then go back to "user"
  

