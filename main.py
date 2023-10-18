from Global_Var import *
from laberinto import *
from personaje import *
from meta import *
from juego import *

laberinto = Laberinto("laberinto.txt")
personaje = Personaje(1, 1) 
meta = Meta(5, 5)  
juego = Juego(laberinto, personaje, meta)
juego.run()
