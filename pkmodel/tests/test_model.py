import unittest
import unittest.mock as mock
from io import StringIO 
import pkmodel as pk

class ModelTest(unittest.TestCase):
    """
    Tests the `Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        #test default model creation#
        model = pk.Model(name = "TestModel")
        self.assertEqual(model.name, "TestModel") #name
        self.assertEqual(model.V_c, 1) #V_c
        self.assertEqual(model.CL, 1) #CL
        self.assertEqual(model.X, 1) #X
        print(model.Q_p)
        self.assertEqual(model.Q_p, []) #Q_p
        self.assertEqual(model.V_p, []) #V_p

        #test print function#
        expectedOutput = "testModel: a model with 0 peripheral compartment(s)"
        with mock.patch('sys.stdout', new = StringIO()) as fake_out: 
            print(model)
            self.assertEqual(fake_out.getvalue(), expectedOutput) 

        #test correct non-default inputs of correct type#
        model = pk.Model(name = "TestModel",
                      V_c = 2,
                      CL = 2,
                      X = 2,
                      Q_p = [1],
                      V_p = [1])
        self.assertEqual(model.name, "TestModel") #name
        self.assertEqual(model.V_c, 2) #V_c
        self.assertEqual(model.CL, 2) #CL
        self.assertEqual(model.X, 2) #X
        self.assertEqual(model.Q_p, [1]) #V_c
        self.assertEqual(model.V_p, [1]) #V_p

        #test incorrect input types#
        with self.assertRaises(TypeError):
            model = pk.Model(name = 1) #name
            model = pk.Model(name = "testModel", V_c = "wrong") #V_c
            model = pk.Model(name = "testModel", CL = "wrong") #CL
            model = pk.Model(name = "testModel", X = "wrong") #X
            model = pk.Model(name = "testModel", Q_p = "wrong") #Q_p
            model = pk.Model(name = "testModel", Q_p = ["a"]) #Q_p values
            model = pk.Model(name = "testModel", V_p = "wrong") #V_p
            model = pk.Model(name = "testModel", V_p = ["a"]) #V_p values
        #Q_p and V_p not equal length
        expectedOutput = "Q_p and V_p must be of equal length"
        with mock.patch('sys.stdout', new = StringIO()) as fake_out: 
            print(model)
            self.assertEqual(fake_out.getvalue(), expectedOutput)

    """
    Test addition of compartments.
    """
    def test_add_compartment(self):
        #initiate model#
        model = pk.Model(name = "TestModel")
        #test correct addition of compartment#
        model.add_compartment(Q_p = 2, V_p = 2)
        self.assertEqual(model.Q_p, [2])
        self.assertEqual(model.V_p, [2])
        #test incorrect variables inputs#
        with self.assertRaises(TypeError):
            model.add_compartment(Q_p = "a", V_p = 2) #Q_p
            model.add_compartment(Q_p = 2, V_p = "a") #V_p