import numpy as np
import math

class Projectile:
    def __init__(self,Mass,V_x, V_y, x, y, R):
        self.M = Mass
        self.V_X = V_x
        self.V_Y = V_y
        self.X = x
        self.Y = y
        self.R = R


    def getSpeed(self):
        return((self.V_X**2 + self.V_Y**2)**(1/2))
    def getEnergy(self):
        return(self.M*self.getSpeed()**2)

    def update(self,F_X,F_Y,dt):
        """Updates the velocity for the given force and then changes its position"""
        self.V_X += (F_X/self.M)*dt
        self.V_Y += (F_Y/self.M)*dt
        
        self.X = self.X + self.V_X*dt + 0.5*(F_X/self.M)*dt**2
        self.Y = self.Y + self.V_Y*dt + 0.5*(F_Y/self.M)*dt**2