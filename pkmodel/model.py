#
# Model class
#
def checkTypes(value, validTypes):
     """checks that inputs are numbers
     
     Parameters
     ----------
     value: input variable (any class)
     validTypes: list of accepted types

     """
     #check that type is 'int' or 'float'#
     if type(value) not in validTypes:
        types = [t.__name__ for t in validTypes]
        raise TypeError(f"'{str(value)}' is not of type {' or '.join(types)}")
     
class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    name: character, name of model
    V_c: numeric/int, def = 1
    CL: numeric/int, def = 1
    X: numeric/int, def = 1
    Q_p: list of numeric/int, def = []
    V_p: list of numeric/int, def = []

    """
    def __init__(self,
                 name,
                 V_c = 1,
                 CL = 1,
                 X = 1,
                 Q_p = [],
                 V_p = []):
        self.name = name
        self.Q_p = Q_p
        self.CL = CL
        self.X = X
        self.V_c = V_c
        self.V_p = V_p

        #check that values are correct types#
        for var in [self.V_c, self.CL, self.X]:
            checkTypes(value = var,
                       validTypes = [float, int])
        for var in [self.Q_p, self.V_p]:
            checkTypes(value = var,
                       validTypes = [list])
        for val in self.Q_p:
            checkTypes(value = val,
                       validTypes = [float, int])
        for val in self.V_p:
            checkTypes(value = val,
                       validTypes = [float, int])
        checkTypes(value = self.name,
                   validTypes = [str])

        #check arguments for additional compartments are of equal length#
        assert len(self.Q_p) == len(self.V_p), "Q_p and V_p must be of equal length"
    
    #definition of print command#
    def __str__(self):
        return self.name + ": a model with " + str(len(self.Q_p)) + " peripheral compartment(s)"
    
    #command for adding additional compartments#
    def add_compartment(self, Q_p, V_p):
        #check variable types#
        for var in [Q_p, V_p]:
            checkTypes(value = var,
                       validTypes = [float, int])
        #add variables for additional compartments
        self.Q_p.append(Q_p)
        self.V_p.append(V_p)
        return "model named " + self.name

