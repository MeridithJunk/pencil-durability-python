import unittest

from pencil import Pencil


class TestPencil(unittest.TestCase):
    def test_when_ISupplyPencilWithAString_ThenTheStringIsReturned(self):
        pencil = Pencil()
        self.assertEqual(pencil.write("She sells sea shells"), "She sells sea shells")

    def test_when_ISupplyPencilWithTwoStrings_ThenTheStringAppendedAndIsReturned(self):
        pencil = Pencil()
        pencil.write("She sells sea shells")
        self.assertEqual("She sells sea shells by the seashore", pencil.write(" by the seashore"))


if __name__ == '__main__':
    unittest.main()
