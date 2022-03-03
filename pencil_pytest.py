import unittest

from pencil import Pencil


class TestPencil(unittest.TestCase):
    def test_when_ISupplyPencilWithAString_ThenTheStringIsReturned(self):
        pencil = Pencil(100)
        self.assertEqual(pencil.write("She sells sea shells"), "She sells sea shells")

    def test_when_ISupplyPencilWithTwoStrings_ThenTheStringAppendedAndIsReturned(self):
        pencil = Pencil(100)
        pencil.write("She sells sea shells")
        self.assertEqual("She sells sea shells by the seashore", pencil.write(" by the seashore"))

    def test_when_ISupplyPencilWithADurabilityOf2_Then_sh_isReturned(self):
        pencil = Pencil(2)
        self.assertEqual("sh", pencil.write("she sells"))

    def test_when_ISupplyPencilWithADurabilityOf4_Then_She_isReturned(self):
        pencil = Pencil(4)
        self.assertEqual("She", pencil.write("Shesells"))

    def test_when_ISupplyPencilWithADurabilityOf4AndSpaces_Then_spacesDontDegradation(self):
        pencil = Pencil(4)
        self.assertEqual("she s", pencil.write("she sells"))


if __name__ == '__main__':
    unittest.main()
