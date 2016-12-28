#Imports
import numpy as np
import matplotlib.pyplot as plt
#Globals
FRAME_TIME = 0.5
WINDOW = 4
WEIGHT = [0.2, 0.3, 0.1, 0.3, 0.1]
LAMBDA = 0.280

class Agent(object):
    def __init__(self, position=[0,0]):
        self.position = position
        self.actions_time = np.arange(0, 0.55, 0.05)
        self.actions_probs = [1.0/11]*11
        #iself.actions_probs = np.random.uniform(0.0, 1.0/11, 11)
        self.BL = 10
        self.IL = np.zeros(4)
        self.OH = np.zeros(4)
        self.UT = np.zeros(4)
        self.DQ = np.zeros(4)
        self.last_action = None
        self.EE = np.zeros(4)
        self.ESEE = None
    def __str__(self):
        return 'The agent on position {}'.format(self.position)


    def choose_action(self):
        action = np.random.choice(self.actions_time, None, True, self.actions_probs)
        self.last_action = np.where(self.actions_time == action)[0][0]
        return action

    def set_ee( self, sleep, frame):
        self.IL[frame] = sleep
        self.OH[frame] = FRAME_TIME - sleep
        #?UT
        #?DQ
        self.EE[frame] = WEIGHT[0]*(1-self.IL[frame]) + \
                         WEIGHT[1]*(1-self.OH[frame]) + \
                         WEIGHT[2]*(1-self.UT[frame]) + \
                         WEIGHT[3]*(1-self.DQ[frame]) + \
                         WEIGHT[4]*self.BL


    def set_esee(self, neighbours):

        sum_n = 0
        for N in neighbours:
            sum_n = np.sum(N.EE)

        self.ESEE = (1.0/WINDOW)*(np.sum(self.EE)+sum_n)/(len(neighbours)+1)


    def update_probs(self):

        for idx, p in enumerate(self.actions_probs):
            if( idx != self.last_action):
                p = p - LAMBDA*self.ESEE*p
            else:
                p = p + LAMBDA*self.ESEE*(1 - p)
            self.actions_probs[idx] = p



def test_agent():
    agent = Agent([1,1])
    plt.plot(agent.actions_time, agent.actions_probs)
    action = agent.choose_action()
    print 'Action sleep time = '+str(action)
    print 'Action position = '+str(agent.last_action)


    agent.set_ee( action, 0)
    print 'EE is ' + str(agent.EE)
    agent.set_esee([agent]*4)
    print 'ESEE is ' + str(agent.ESEE)

    agent.update_probs()
    print 'New actions sum '+str(sum(agent.actions_probs))
    plt.plot(agent.actions_time, agent.actions_probs)
    plt.show()

if __name__ == '__main__':
    test_agent()
