sz = 10
speed = 1

class Snake:
  def __init__(self):
    self.pos = PVector(300,300)
    self.sz = sz
    self.vel = PVector(speed,0)
    self.dead = False
    self.tail_length = 3
    self.tail = [self.pos,PVector(self.pos.x-self.sz,self.pos.y),
                 PVector(self.pos.x-2*self.sz,self.pos.y)]
    
  def update(self):
    #movement code
    self.pos.x += self.vel.x * self.sz
    self.pos.y += self.vel.y * self.sz
    #can't touch tail
    for segment in self.tail[3:]:
        if dist(self.pos.x,self.pos.y, segment.x,
                    segment.y)<self.sz:
            self.dead = True
    #top
    if self.pos.y <= self.sz/2.0:
        self.dead = True
        #self.pos.y = self.sz/2.0
    #bottom
    if self.pos.y >= 600 - self.sz/2.0:
        self.dead = True
        #self.pos.y = 600 - self.sz/2.0
        
    #left
    if self.pos.x <= self.sz/2.0:
        self.dead = True
        #self.pos.x = self.sz/2.0
    #bottom
    if self.pos.x >= 600 - self.sz/2.0:
        self.dead = True
        #self.pos.x = 600 - self.sz/2.0
        
    self.tail = [PVector(self.pos.x,self.pos.y)]+self.tail[:self.tail_length-1]
    
    #draw the square
    stroke(0,255,0)
    fill(0,150,0)
    for segment in self.tail:
        rect(segment.x,segment.y,self.sz,self.sz)
    
class Apple:
    def __init__(self):
        self.pos = PVector(random(20,580),
                           random(20,580))
        self.eaten = False
        
    def update(self,snake):
        if dist(self.pos.x,self.pos.y,
                snake.pos.x,snake.pos.y) < sz:
            score.increment()
            snake.tail_length += 1
            self.pos = PVector(random(600),
                           random(600))
        fill(255,0,0)
        stroke(255,0,0)
        rect(self.pos.x,self.pos.y,
                sz,sz)
        
class Score:
    def __init__(self):
        self.num = 0
        
    def increment(self):
        self.num += 1
        
    def display(self):
        textSize(24)
        fill(0,0,255)
        text(self.num,100,100)
    
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
score = Score()

def setup():
  size(600,600)
  rectMode(CENTER)
  
def draw():
    global snake,apple,score
    frameRate(10)
    background(0,255,0) #green 
    snake.update()
    if snake.dead:
        score = Score()
        del(snake)
        snake = Snake()
  
    apple.update(snake)
    score.display()
