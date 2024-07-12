# Pyhme-Engine
A Python Pygame Wrapper!

## DISCLAIMER
### PYHME ENGINE IS NOT INSTALLABLE USING PIP | PLEASE NOTE THAT THIS IS A WORK IN PROGRESS MANY THINGS MAY CHANGE!

## LATEST CHANGE!
### RELEASE! [1.0]

-Added Events.
-  MOUSELEFTCLICK
-  MOUSERIGHTCLICK
-  ENTITYCLICK
-  KEYDOWN
-  KEYPRESSED
-  KEYRELEASED

-Added Shapes.
-  Quads / Quadrilaterals

## TUTORIAL
### HOW TO USE:

You can initialize a new window by doing the following:
```py
import Phyme
window = Phyme.App("600x500", "HELLO WORLD") #CREATES A WINDOW WITH THE SIZE 600x500 WITH THE WINDOW NAME AS "HELLO WORLD"
window.BGColor = "#FFFFFF" # SETS WINDOW BACKGROUND COLOR TO WHITE IN HEXADECIMAL #FFFFFF -> (255,255,255)
window.Name = "Hello World" # SETS NAME OF WINDOW AGAIN | OPTIONAL

window.run() #DISPLAYS WINDOW!
```

You can add events by doing the following:
```py
import Phyme
window = Phyme.App("600x500", "HELLO WORLD")
window.BGColor = "#FFFFFF"
window.Name = "Hello World"

#Letter should be lowercase or else it doesnt detect it!
@window.KeyDown("b") #CREATES A NEW EVENT WHICH EXECUTES A FUNCTION WHEN THE LETTER B IS PRESSED!
def b_is_pressed(): #MAIN FUNCTION
  print("b is pressed")

window.run()
```

These are all the currently available events!

```py
import Phyme
window = Phyme.App("600x500", "HELLO WORLD")

window.KeyDown("a")
def A():
  print("A SPAM")
window.KeyPressed("b")
def B():
  print("B IS PRESSED!!")
window.KeyReleased("c):
def C():
  print("C IS RELEASED!")
window.LeftClick() # - May have an entity or not
def LeftClicked():
  print("LEFT CLICKED!")
window.RightClick() # - May have an entity or not
def RightClicked():
  print("RIGHT CLICKED!")
```
### HOW TO MAKE ENTITIES!
```py
#You can add entities / shapes
Square=window.Quad("50x50", [0,0], "#FF00FF") #Creates a quadrilateral with size 50px and position at 0,0 with the color pink (#FF00FF)
window.append(Square) #Shows the square

window.LeftClick(Square) # Triggers When Square is Left Clicked!
def SquareISLeftClicked():
  print("SQUARE IS LEFTCLICKED")

window.RightClick(Square) # Triggers When Square is Left Clicked!
def SquareISRightClicked():
  print("SQUARE IS RIGHTCLICKED")
window.run()
```
