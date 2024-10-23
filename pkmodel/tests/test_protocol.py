import unittest
import pkmodel as pk
import pytest


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_dosage(self):
        """
        Tests Protocol dosage default.
        """
        protocol_test = pk.Protocol()
        protocol_test.set_dose()
        self.assertEqual(protocol_test.dose, 'intra')

    def test_dosage2(self):
        """
        Tests Protocol set_dose for 'intra'.
        """
        protocol_test = pk.Protocol()
        protocol_test.set_dose('insta')
        self.assertEqual(protocol_test.dose, 'intra')

    def test_dosage3(self):
        """
        Tests Protocol set_dose for 'subc'.
        """
        protocol_test = pk.Protocol()
        protocol_test.set_dose('subc')
        self.assertEqual(protocol_test.dose, 'subc')

    def test_invalid_type_fails(self):
        protocol_test = pk.Protocol
        with pytest.raises(Exception) as e_info:
         protocol_test.set_dose('invalid_type')