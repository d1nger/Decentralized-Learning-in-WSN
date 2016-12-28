# Imports
import numpy as np
import matplotlib.pyplot as plt
from agents import Agent
import time, sys
from threading import Timer
# Constants
N = 10                              # Number of sensors (nodes, agents)
SYNC_TIME =  20                     # Synchronizaion time, 20s
FRAME_TIME = 0.5                    # Frame duration
MEASURE_RATE = 1                    # Number of measurements during one frame
WINDOW = 4                          # Number of frames in a window
TOTAL_TIME = 500                    # Total simulation time
TOTAL_FRAMES = TOTAL_TIME / FRAME_TIME


def run():
    agents = [Agent() for i in range(10)]

    count = 1

    #General simulation duration
    while count < TOTAL_FRAMES:

        #Frame simulation
        t = time.time()
        while (time.time()-t) < FRAME_TIME:
            sys.stdout.flush()


        print 'Frame ' + str(count)
        #Window counter
        if count % WINDOW == 0:
            print 'New window {}'.format(count/WINDOW)
            print 'Frame time is {}'.format((time.time() - t))

        count += 1

if __name__ == '__main__':
    'Starting simulation'
    run()
