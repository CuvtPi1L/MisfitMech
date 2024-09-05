import numpy as np
import math

class Projectile:
        def __init__(self, mass, V_x, V_y, x,y,R):
                self.M = mass
                self.V_x = V_x
                self.V_y = V_y 
                self.x = x
                self.y = y 
                self.r = R
                self.V = (self.V_X**2 + self.V_Y**2)**(1/2)
                self.KE = self.M*self.V**2

        def update(self,F_X,F_Y,dt):
                self.V_X = self.V_X + (F_X/self.M)*dt
                self.V_Y = self.V_Y + (F_Y/self.M)*dt

                self.X = self.X + self.V_X*dt + 0.5*(F_X/self.M)*dt**2
                self.Y = self.Y + self.V_Y*dt + 0.5*(F_Y/self.M)*dt**2
