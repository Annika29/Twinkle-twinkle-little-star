import random as rnd

stars = [] # an empty list called 'stars'

class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        
    def set_fill(self): # a method that sets the fill
        fill(self.red, self.green, self.blue, self.alpha)
        
    def twinkle(self):
        if self.alpha < 255:
            self.alpha += 1
        else:
            self.alpha = 250
            self.a
        
class Coordinate:
    
    screen_size = 800
    screen_offset = screen_size/2
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Star:
    
    max_color = 200 
    
    # each star has a coordinate (x,y), a diameter, a distance, and a color
    def __init__(self, coordinate, diameter, distance, color, speedx, speedy, directionx, directiony):
        self.coordinate = coordinate
        self.diameter = diameter
        self.distance = distance
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.directionx = directionx
        self.directiony = directiony
    
    def draw_star(self):
        scale = 1.0 / (1.0 + self.distance)
        screen_x = Coordinate.screen_offset + scale*self.coordinate.x
        screen_y = Coordinate.screen_offset - scale*self.coordinate.y  # Y is inverted
        screen_diameter = scale*self.diameter
        self.color.set_fill()
        ellipse(screen_x, screen_y, screen_diameter, screen_diameter)
        
    def step(self):
        self.coordinate.x += self.speedx * self.directionx
        self.coordinate.y += self.speedy * self.directiony
        self.diameter -= .9
    
    @staticmethod
    def make_random_star(number):
        rand_star = Star(Coordinate(rnd.randrange(Coordinate.screen_size)-Coordinate.screen_offset, rnd.randrange(Coordinate.screen_size)-Coordinate.screen_offset), \
        40, number, Color(255, 255, 0, 192), rnd.randrange(20, 40), rnd.randrange(20, 40), rnd.random(), rnd.random())
    
        return rand_star

def setup():    
    size(800, 800)
    noStroke()
    frameRate(10)

def draw():
    background(0)
    
    for a in range(0, 30):
        fill(255, 255, 255)
        ellipse(rnd.randrange(800), rnd.randrange(800), rnd.randrange(3, 10), rnd.randrange(3, 10))
    
    fill(255, 255, 255) # moon
    ellipse(150, 150, 200, 200)

    fill(0, 0, 0)
    ellipse(120, 120, 150, 150)

    for i in range(0, 1):
        stars.append(Star.make_random_star(i/10.0))

    for star in stars:
        star.draw_star()
        star.color.twinkle()
        star.step()
        
'''
        if star.coordinate.x  <= -Coordinate.screen_offset - star.diameter or \
            star.coordinate.x  >= Coordinate.screen_offset + star.diameter:
            star.directionx *= -1
        
        if star.coordinate.y  <= -Coordinate.screen_offset - star.diameter*2 or \
            star.coordinate.y  >= Coordinate.screen_offset + star.diameter*2:
            star.directiony *= -1
'''