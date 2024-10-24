#Script to run the model and then calculate and plot the output

"""
More work needed on this file. The next step would be to add in the values of parameters of Model in line 14, 
check the output of protocol.py and ensure the qp and qc outputs are arrays of the same length as the time
array defined in model.py

Finally should make a test_solutions.py file to make sure the steps are running as intended. 
"""


from pkmodel.model import Model
from pkmodel.protocol import Protocol
from pkmodel.plot_function import plot_data

m= Model("parameters")

p= Protocol(m, "intravenous")

p.calculate("intravenous")

fig =plot_data(protocol.t, protocol.qp, protocol.qc)
plt.show()

