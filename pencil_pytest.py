import pencil
import unittest


class TestPencil(unittest.TestCase):
    def test_when_ISupplyPencilWithAString_ThenTheStringIsReturned(self):
        self.assertEqual(pencil.write("She sells sea shells"), "She sells sea shells")

    def test_when_ISupplyPencilWithTwoStrings_ThenTheStringAppendedAndIsReturned(self):
        pencil.write("She sells sea shells")
        self.assertEqual(pencil.write(" by the seashore"), "She sells sea shells by the seashore")


if __name__ == '__main__':
    unittest.main()
