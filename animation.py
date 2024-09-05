import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

path= '/Users/lynnre/Documents/drake/001_2024Spring/03_MISFIT_Mech/mechanical-group/output.csv'
df = pd.read_csv(path)
fig, ax = plt.subplots()


def update(frame):
    ax.clear()
    for i in range((len(df.axes[1]) - 3)//2): # (len(df.axes[1]) - 3)//2 = number of springs
        a = 3
        px = df.iloc[frame,3 + i]#f'{i + 1}_x']
        py = df.iloc[frame,3 + i + 10]#f'{i + 1}_y']
        ax.scatter(px, py, label=f'Spring {i + 1}')
        ax.annotate(f'{i + 1}', (px, py), textcoords="offset points", xytext=(-5,5), ha='center')
        #if i == 0:
            #print(f'y = {py}')
    ax.set_title(f'Frame {frame}')
    px = df.iloc[frame,1]#'pX']
    py = df.iloc[frame,2]#'pY']
    particle_radius = R  # Adjust the radius as needed
    ax.scatter(px, py, color='blue')  # Solid core
    ax.scatter(px, py, color='blue', s=particle_radius**2, alpha = 0.5)
    ax.legend()

ani = animation.FuncAnimation(fig, update, frames=range(0,len(df),50), interval=100)

plt.show()
