import unittest
from vm import VM, Currencies

class VMTests(unittest.TestCase):
  def test_insertCoins(self):
    vm = VM()
    self.assertEqual(vm.insertCoin('0.05'), 0.05)
    self.assertEqual(vm.insertCoin('0.02'), None)

  def test_returnCoins(self):
    vm = VM()
    self.assertEqual(vm.insertCoin('2.0'), 2.0)
    self.assertEqual(vm.returnCoins(), 2.0)
    self.assertEqual(vm.getAmount(), 0.0)
if __name__ == '__main__':
  unittest.main()