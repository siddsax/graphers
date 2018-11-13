from visdom import Visdom
import numpy as np
import matplotlib.pyplot as plt


refresh = 100
y = np.array([90.800, 92.330, 93.180, 93.760, 94.140, 94.130, 94.270, 94.220, 94.210, 94.170 ]*3)
num_epochs = len(y)


#######  Preparation  ############
viz = Visdom()
options=dict(
            ytickmin=90,
            ytickmax=100,
            xlabel='This X Label',
            ylabel='This Y Label',
            title='The Title',
        )
##################################


for iteration in range(num_epochs):
    if iteration % refresh == 0:
        ################## To Refresh after some time ##################
        win = viz.line(X=np.arange(iteration, iteration +.1), Y=np.arange(0, .1))
        ################################################################
    if iteration == 0:
        loss = y[0]
    else:
        loss_old = loss
        loss = y[iteration]
        #################        Plotting        #######################
        viz.line(X=np.linspace(iteration-1,iteration,50), Y=np.linspace(loss_old, loss,50), name='1', update='append', win=win, opts=options)
        ################################################################
    plt.pause(.5)
