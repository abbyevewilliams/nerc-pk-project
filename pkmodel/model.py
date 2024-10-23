#
# Model class
#
def checkTypes(value):
     """checks that inputs are numbers
     
     Parameters
     ----------
     value: can be any class

     """
     #check that type is 'int' or 'float'#
     if type(Q_p) != float and type(Q_p) != int:
        raise TypeError("Q_p must be of type 'int' or 'float'")
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
                 V_c = 1,
                 CL = 1,
                 X = 1,
                 Q_p = [],
                 Q_v = []):
        self.name = name
        self.Q_p = Q_p
        self.V_c = V_c
        self.V_p = Q_v
        self.CL = CL
        self.X = X

        #check arguments for addiotnal compartments are of equal length#
        assert len(Q_p) == len(Q_v), "Q_p and Q_p must be of equal length"
    
    ##
    def __str__(self):
        return self.name + ": a model with " + str(len(self.Q_p)) + " peripheral compartment(s)"
    
    ##
    def add_compartment(self, Q_p, V_p):
        #check that inputted values are numbers
        if type(Q_p) != float and type(Q_p) != int:
            raise TypeError("Q_p must be of type 'int' or 'float'")
        if type(V_p) != float and type(V_p) != int:
            raise TypeError("V_p must be of type 'int' or 'float'")
        #add variables for additional compartments
        self.Q_p.append(Q_p)
        self.V_p.append(V_p)


##tests##
#initiate model#
testModel = Model(name = "testModel", Q_p = [1], Q_v = [1])

#test print command#
print(testModel)

#add module wrong#
try:
    testModel.add_compartment(Q_p = 1, V_p = 1)
except TypeError as e:
    print(e)

#test print again#
print(testModel)




