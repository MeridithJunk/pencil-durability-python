import pencil
import unittest


class TestPencil(unittest.TestCase):
    def test_when_ISupplyPencilWithAString_ThenTheStringIsReturned(self):
        self.assertEqual(pencil.write("She sells sea shells"), "She sells sea shells")


if __name__ == '__main__':
    unittest.main()
