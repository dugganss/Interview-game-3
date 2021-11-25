#SCREEN SIZE VARIABLES
WINDOW_W = 800
WINDOW_H = 800

#2D ARRAYS
grid_size = 40

LAYOUT = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,8,9,7,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,4,"m",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,8,9,9,"j","k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"l","k","k","k",3,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k",0,"h",1,5,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k",0,"i",0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k","k","k",3,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,6,1,"g","k",3,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,4,"k",3,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,8,9,"j","k","i",9,7,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k","k","k","k","k",3,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k",0,"k","d","k",3,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k",0,"k","f","k",3,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,"k","k","k","f","k",3,0,0,0,0,0,0,0],
  [0,0,0,8,9,9,9,"a",1,1,4,"k",3,0,0,0,0,0,0,0],
  [0,0,0,4,"k","k","k","k",3,0,4,"k",3,0,0,0,0,0,0,0],
  [0,0,0,4,"k","h","g","k","i",9,"j","k",3,0,0,0,0,0,0,0],
  [0,0,0,4,"k",3,4,"k","k","k","k","k",3,0,0,0,0,0,0,0],
  [8,9,9,"j","k","i",9,"a","a","a",1,1,9,9,9,9,7,0,0,0],
  [4,"k","k","k","k","k","k","k","k","k","i","j","l","k","k","k",3,0,0,0],
  [4,"k",0,0,"k","h",1,1,"g","k","k","k","k",0,0,"k",3,0,0,0],
  [4,"k",0,0,"k",3,0,0,6,1,1,"a","a","b",0,"k",3,0,0,0],
  [4,"l","k","k","k",3,0,0,0,0,4,0,0,0,0,"k",3,0,0,0],
  [6,1,1,1,1,5,0,0,0,0,4,0,0,0,0,"k",3,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,4,0,0,2,0,"k",3,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,6,1,1,1,1,1,5,0,0,0],
  ]