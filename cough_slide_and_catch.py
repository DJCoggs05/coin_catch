# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:20 2024

@author: cough
"""
import sys
sys.path.insert(0, "C:/Users/cough/Downloads")
import simpleGE, pygame, random

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect((0,0, 240), (25,25))
        self.setSize(50, 50)
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Mickey(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("C:/Users/cough/Downloads/Mickey_Mouse.jpg")
        self.setSize(50, 50)
        
        #setBoundAction(BOUNCE) 
        
    def process(self):   
        if self.isKeyPressed(pygame.K_a):
            self.x -= 10
        if self.isKeyPressed(pygame.K_d):
            self.x += 10
        if self.isKeyPressed(pygame.K_w):
            self.y -= 10
        if self.isKeyPressed(pygame.K_s):
            self.y += 10
            
class Game(simpleGE.Scene):
    scene = simpleGE.Scene()
    scene.setImage("C:/Users/cough/Downloads/sky.jpeg")
    scene.setCaption("Game")
    mickey = Mickey(scene)
    coin = Coin(scene)
    scene.sprites = [mickey, coin]
    scene.start()
    
def main():
    game = Game()
    game()
    
if __name__ == "__main__":
    main()
