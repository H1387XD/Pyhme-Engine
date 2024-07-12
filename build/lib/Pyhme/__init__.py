import pygame as pg
import sys
print("\nWelcome To Pyhme Engine [1.0]! A Wrapper for Pygame!")

QUIT = 32787, "quit"
CLICK1 = 1026, "left"
CLICK2 = 1026, "right"
KEYRELEASED = 769, "keyreleased"
KEYPRESSED = 768, "keypressed"
KEYDOWN = 771, "keydown"

types=[
	CLICK1[0],
	KEYRELEASED[0],
	KEYPRESSED[0],
	KEYDOWN[0],
]

def _ClickCheck1(target, event):
	if event.button==3:
		return False
	return target.rect.collidepoint(event.pos) if target is not None else True
def _ClickCheck2(target, event):
	if event.button==1:
		return False
	return target.rect.collidepoint(event.pos) if target is not None else True
def _KeyCheck(target, event):
	return event.dict['unicode']==target
def _KeyDownCheck(target, event):
	return event.dict['text']==target
EventChecks={
	CLICK1[1]: _ClickCheck1,
	CLICK2[1]: _ClickCheck2,
	KEYRELEASED[1]: _KeyCheck,
	KEYPRESSED[1]: _KeyCheck,
	KEYDOWN[1]: _KeyDownCheck,
}

class Event:

	def __init__(self, func, target, type):
		self.func = func
		self.target = target
		self.type = type
		if self.type[1] not in EventChecks:
			raise Exception("Event Type Not Found! " + str(self.type[1]))
		self.check=EventChecks[self.type[1]]

	def checkFunction(self, event):
		if self.type[0] not in types:
			return
		if event.type!=self.type[0]:
			return
		if self.check(self.target, event):
			self.func()
	def __repr__(self):
		return f"{self.type[1]} {self.func}"

class Entity():

	def __init__(self, size, pos, col):
		self.size = size
		self.x=pos[0]
		self.y=pos[1]
		self.pos = [self.x, self.y]
		self.col = col
		self.rect = pg.Rect(self.pos, self.size)
	def draw(self, screen, layer=0):
		self.pos = [self.x, self.y]
		self.rect = pg.Rect(self.pos, self.size)
		pg.draw.rect(screen, self.col, self.rect, layer)


class App():

	def __init__(self, windowsize: str, windowname: str = "Phyme Engine!"):
		self.Size = windowsize.split("x")
		self.Size[0] = int(self.Size[0])
		self.Size[1] = int(self.Size[1])
		self.Name = windowname
		self.rootScreen = pg.display.set_mode(self.Size)
		
		self.entities = []
		self.BGColor = "#000000"
		self.events = []
		self.running = True

	def quad(self, size: str, pos: list, col: tuple = (0, 0, 0)):
		self.size = []
		self.pos = pos
		self.col = col
		for thing in size.split("x"):
			self.size.append(int(thing))

		return Entity(self.size, self.pos, self.col)

	def append(self, entity):
		self.entities.append(entity)

	def destroy(self, entity):
		try:
			self.entities.remove(entity)
		except ValueError:
			pass #dafuck

	def draw(self):
		for entity in self.entities:
			entity.draw(self.rootScreen)

	def eventKeyReleased(self, target):
		def wrapper(func):
			self.events.append(Event(func, target, KEYRELEASED))

		return wrapper
	def eventKeyPressed(self, target):
		def wrapper(func):
			self.events.append(Event(func, target, KEYRELEASED))

		return wrapper

	def eventKeyDown(self, target):
		def wrapper(func):
			self.events.append(Event(func, target, KEYDOWN))

		return wrapper

	def eventRightClick(self, target=None):
		def wrapper(func):
			self.events.append(Event(func, target, CLICK2))
		return wrapper
	def eventLeftClick(self, target=None):
		def wrapper(func):
			self.events.append(Event(func, target, CLICK1))
		return wrapper
	def update(self):
		pg.display.set_caption(str(self.Name))
		for pygameEvent in pg.event.get():
			if pygameEvent.type==QUIT[0]:
				self.running=False
			for event in self.events:
				if event.type[0]==pygameEvent.type:
					event.checkFunction(pygameEvent)
			else:
				break

		self.rootScreen.fill(self.BGColor)

		self.draw()
		pg.display.flip()
		return False
	def run(self):
		while self.running:
			self.update()
