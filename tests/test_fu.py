import unittest

class FuTest(unittest.TestCase):
 
    def test_someHit(self):
        fu = 3 + 3
        self.assertEqual(fu, 6)

    def test_another(self):
        fu = 3-3
        self.assertEqual(fu,3)



if __name__ == "__main__":
    unittest.main()
