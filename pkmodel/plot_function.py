#Define a function, plot_data, to plot the outputs of the PK model. 
#t, Y are the outputs called from protocol.py, where Y is an array
#Plots.py is run within Solution.py

import matplotlib.pyplot as plt

#need to give the inputs labels
def plot_data(t, qp, qc):
    fig = plt.figure()
    plt.plot(t, qp[:])
    plt.plot(t, qc[:])
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    
    return fig




