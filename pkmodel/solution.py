#Script to run the model and then calculate and plot the output

from pkmodel.model import Model
from pkmodel.protocol import Protocol
from pkmodel.plot_function import plot_data

m= Model("parameters")

p= Protocol(m, "intravenous")

p.calculate("intravenous")

fig =plot_data(protocol.t, protocol.qp, protocol.qc)
plt.show()

