import numpy as np
import math

class Spring:
    def __init__(self, x, y, k, m) -> None:
        self.x = x
        self.y = y
        self.k = k
        self.V_X = 0
        self.V_Y = 0
        self.F_X = 0 
        self.F_Y = 0 
        self.m = m
        self.l = y
        self.Y_init = y
        self.X_init = x

    def get_F_Y(self):
        return(self.k*(self.Y_init-self.y))

    def get_F_X(self):
        return(self.k*(self.X_init-self.x))
        
    def update(self, F_X, F_Y, dt):
        """Inertial implementation of spring motion"""
        self.V_X += (F_X/self.m)*dt
        self.V_Y += (F_Y/self.m)*dt
        
        self.x += self.V_X*dt + 0.5*(F_X/self.m)*dt**2
        self.y += self.V_Y*dt + 0.5*(F_Y/self.m)*dt**2