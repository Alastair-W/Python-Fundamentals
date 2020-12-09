import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result = num
        for n in nums:
            self.result += n
        return self
    def subtract(self, num, *nums):
        if num < 0:
            print('Please type a positive integer')
            return False
        else:
            self.result -= num
            for n in nums:
                if n < 0:
                    print('Please only type in a positive integer')
                    return False
                else:
                    self.result -= n
        return self


# create an instance:
# md = MathDojo()
# # to test:
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	# should print 5
# run each of the methods a few more times and check the result!


class mathDojoTest(unittest.TestCase):
    def testAddition(self):
        self.assertGreater(MathDojo().add(2,5,1).result, 0)
        self.assertEqual(MathDojo().add(2,5,1).result, 8)
        self.assertEqual(MathDojo().add(21,25,10).result, 56)
        self.assertEqual(MathDojo().add(112,225,10.1).result, 347.1)
    def testSubtraction(self):
        self.assertLess(MathDojo().subtract(3,2,1).result, -5)
        self.assertEqual(MathDojo().subtract(12,225,10.1).result, -247.1)
    def testNegInt(self):
        self.assertFalse(MathDojo().subtract(-3,2,1))
        self.assertFalse(MathDojo().subtract(3,-2,1))
        
    def setUp(self):
        print('running setUp')
    def tearDown(self):
        print('running tearDown task')

if __name__ == '__main__':
    unittest.main()