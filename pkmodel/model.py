#
# Model class
#

class Model:

    """A Pharmokinetic (PK) model

    Parameters
    ----------

    name: character, name of model
    Q_p1: numeric, def = 1
    V_c: numeric, def = 1
    V_p1: numeric, def = 1
    CL: numeric, def = 1
    X: numeric, def = 1

    """
    def __init__(self,
                 name,
                 Q_p1 = 1,
                 V_c = 1,
                 V_p1 = 1,
                 CL = 1,
                 X = 1):
        self.name = name
        self.Q_p1 = Q_p1
        self.V_c = V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X = X

    def __str__(self):
        return "model named " + self.name