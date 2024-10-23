#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    dose: string, ['intravenous bolus', 'subcutaneous']

    """
class Protocol:

    def __init__(self):
        self.dose = 'intra'

    def __str__(self): 
        return self.dose
    
    def set_dose(self, type):
        valid_types =['intra', 'subc']
        if type not in valid_types:
            raise ValueError(f"Invalid dose type. Choose from: {valid_types}")
        self.dose = type
        return f"Dose set to: {type}"




