import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functions import *
import os



def main():
    path= '/Users/lynnre/Documents/drake/001_2024Spring/03_MISFIT_Mech/mechanical-group/output.csv'
    os.remove(path)
    N_springs = 10
    dx = 0.3
    k = 0.1
    M = 10
    m = 1
    V_X = 0
    V_Y = -0.1
    X = 1.4
    Y = 2
    R = 1
    dt = 0.01
    timesteps = 5000
    show_frame_timer = 2500
    f = 0
    epsilon = 0.01
    Force = 0

    springs = init_springs(N_springs, dx, k, m)
    projectile = Projectile(M,V_X, V_Y, X, Y, R)

    # Storage for history
    px=[]
    py=[]
    springx = []
    springy = []
    is_touching_list = []
    push_outside_list = []
    add_forces_list = []
    

    
    #Simulation start
    for i in range(timesteps):
        for spring in springs:
            if is_touching(spring, projectile, epsilon):
                push_outside(spring, projectile,epsilon)
        
        Force = add_forces(springs, projectile, epsilon)
        projectile.update(Force[0], Force[1], dt)
        for spring in springs: 
            # spring.F_X = Force[0]
            # spring.F_Y = Force[1]
            # spring.update(spring.F_X , spring.F_Y, dt)
            spring.update(spring.get_F_X(), spring.get_F_Y(), dt)
    
        
        #if i % show_frame_timer == 0:
            #print("Projectile energy:", projectile.getEnergy())
            #print("Projectile Y Position:", projectile.Y)
            #print("Projectile Y Velocity:", projectile.V_Y)
            #for spring in springs:
                #print("spring position: ", spring.Y)
            #print('===================================================')
            
        # Store history
        px.append(projectile.X)
        py.append(projectile.Y)
        springx.append([spring.X for spring in springs])
        springy.append([spring.Y for spring in springs])
        is_touching_list.append([ is_touching(spring, projectile, epsilon)for spring in springs])
        push_outside_list.append([push_outside(spring, projectile,epsilon) for spring in springs])
        add_forces_list.append([add_forces(springs, projectile, epsilon) for spring in springs])


    #Final output
    #print("Final energy:\n", projectile.getEnergy())
    #print("Projectile Y Position:", projectile.Y)
    #print("Projectile Y Velocity:", projectile.V_Y)
    #for spring in springs:
        #print("spring y position: ", spring.Y)

    #Convert final data to a DataFrame
    p_df = pd.DataFrame(np.column_stack([px,py]),columns=["pX","pY"])

    sx_df = pd.DataFrame(springx, columns=[f"{i}_x" for i in range(1,N_springs+1)])
    sy_df = pd.DataFrame(springy, columns=[f"{i}_y" for i in range(1,N_springs+1)])
    is_touching_list_df = pd.DataFrame(is_touching(spring, projectile, epsilon), columns=[f"{i}_x" for i in range(1,N_springs+1)])
    push_outside_list_df = pd.DataFrame(push_outside(spring, projectile,epsilon), columns=[f"{i}_x" for i in range(1,N_springs+1)])
    add_forces_list_df = pd.DataFrame(add_forces(springs, projectile, epsilon), columns=[f"{i}_x" for i in range(1,N_springs+1)])

    data = pd.concat([p_df,sx_df,sy_df,is_touching_list_df,push_outside_list_df,add_forces_list_df],axis=1)

    #print(data.info())

    #write data to csv
    
    output_filename = 'output.csv'
    data.to_csv(output_filename, index_label="timestep")

main()

