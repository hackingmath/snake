from processing import *

sz = 10
speed = 3

class Snake:
  def __init__(self):
    self.pos = PVector(300,300)
    self.sz = sz
    self.vel = PVector(0,0)
    
  def update(self):
    #movement code
    self.pos += self.vel
    #top
    if self.pos.y <= self.sz/2.0:
        self.pos.y = self.sz/2.0
    #bottom
    if self.pos.y >= 600 - self.sz/2.0:
        self.pos.y = 600 - self.sz/2.0
        
    #left
    if self.pos.x <= self.sz/2.0:
        self.pos.x = self.sz/2.0
    #bottom
    if self.pos.x >= 600 - self.sz/2.0:
        self.pos.x = 600 - self.sz/2.0
    #draw the square
    stroke(0,50,0)
    fill(0,50,0)
    rect(self.pos.x,self.pos.y,10,10)
    
class Apple:
    def __init__(self):
        self.pos = PVector(random(600),
                           random(600))
        self.eaten = False
        
    def update(self,snake):
        if dist(self.pos.x,self.pos.y,
                snake.pos.x,snake.pos.y) < sz:
            self.pos = PVector(random(600),
                           random(600))
        fill(255,0,0)
        stroke(255,0,0)
        rect(self.pos.x,self.pos.y,
                sz,sz)
    
def keyPressed():
  if key == CODED:
    if keyCode == UP:
      snake.vel = PVector(0,-speed)
    if keyCode == DOWN:
      snake.vel = PVector(0, speed)
    if keyCode == RIGHT:
      snake.vel = PVector(speed,0)
    if keyCode == LEFT:
      snake.vel = PVector(-speed,0)

snake = Snake()
apple = Apple()

def setup():
  size(600,600)
  rectMode(CENTER)
  
def draw():
  background(0,255,0) #green 
  snake.update()
  apple.update(snake)
  
