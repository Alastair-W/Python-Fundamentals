#import Python test framework
import unittest
#import libraries
import math

# our 'unit'
# this is what we are running our test on

def reverseList(revArray):
    loopCount = math.floor(len(revArray)/2)
    for i in range(loopCount):
        revArray[i], revArray[-1-i] = revArray[-1-i], revArray[i]
    return revArray


# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase

class reverseListTests(unittest.TestCase):
    def testPositiveInt(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
    def testNegativeInt(self):
        self.assertEqual(reverseList([-1,-2,-3,-4]), [-4,-3,-2,-1])
    def testMixInt(self):
        self.assertEqual(reverseList([-1,0,2,3]), [3,2,0,-1])
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


def isPalindrome(paliString):
    if type(paliString) != str:
        print(f'Sorry, "{paliString}" is not a string!')
    elif type(paliString) == str and len(paliString.split()) > 1:
        print(f'Sorry, "{paliString}" is more than 1 word!')
    else:
        looper = math.floor(len(paliString)/2)
        for i in range(looper):
            if paliString[i] != paliString[-1-i]:
                return False
            else:
                return True


class isPalindromeTests(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(isPalindrome('racecar'))
        self.assertTrue(isPalindrome('kayak'))
    def testFalse(self):
        self.assertFalse(isPalindrome('Was it a cat I saw'))
        self.assertFalse(isPalindrome('racing'))
    def testInt(self):
        self.assertFalse(isPalindrome(1))
    def testList(self):
        self.assertFalse(isPalindrome([1,2,3]))
    def testDict(self):
        self.assertFalse(isPalindrome({1,2,3}))
    def setUp(self):
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

def coins(money):
    if money == 0:
        print("That is the exact amount so there is no change!")
        return False
    elif money < 0:
        balance = money * -1
        print(f'Ummm, well this is awkward - you still owe me 0.{balance} cents ...')
        return False
    else:
        newList = []
        if money % 25 == 0:
            q = math.floor(money / 25)
            newList.extend((q,0,0,0))
        else:
            q = math.floor(money / 25)
            newList.append(q)
            money %= 25
            if money % 10 == 0:
                d = math.floor(money / 10)
                newList.extend((d,0,0))
            else:
                d = math.floor(money / 10)
                newList.append(d)
                money %= 10
                if money % 5 == 0:
                    n = math.floor(money / 5)
                    newList.extend((n,0))
                else:
                    n = math.floor(money / 5)
                    newList.append(n)
                    money %= 5
                    newList.append(money)
        return newList

class coinsTest(unittest.TestCase):
    def testCalculations(self):
        self.assertEqual(coins(87), [3,1,0,2])
        self.assertEqual(coins(30), [1,0,1,0])
        self.assertEqual(coins(1267), [50,1,1,2])
        self.assertEqual(coins(20), [0,2,0,0])
        self.assertEqual(coins(1), [0,0,0,1])
    def testExceptions(self):
        self.assertFalse(coins(0))
        self.assertFalse(coins(-43))
    def setUp(self):
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


def factorial(max):
    if max == 0:
        fact = 1
    elif max < 0:
        print('You cannot have a negative factorial')
        return False
    else:
        fact = max
        for i in range(1,max):
            fact *= i
    return fact




class factorialTest(unittest.TestCase):
    def testTrue(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
    def testZero(self):
        self.assertEqual(factorial(0), 1)
    def testNegativeInt(self):
        self.assertFalse(factorial(-5))
    def setUp(self):
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
    # add the tearDown tasks
        print("running tearDown tasks")


def fibonacci(n):
    fibList = [0,1]
    if n == 0:
        return 0
    elif n < 0:
        print('I need a positive number!')
        return False
    else: 
        for i in range(1,n-1):
            fibList.append(fibList[i] + fibList[i-1])
        return fibList[-1]


class fibonacciTest(unittest.TestCase):
    def testCorrect(self):
        self.assertEquals(fibonacci(5), 3)
        self.assertEquals(fibonacci(9), 21)
        self.assertEquals(fibonacci(20), 4181)
        self.assertEquals(fibonacci(0), 0)
    def testIncorrect(self):
        self.assertNotEqual(fibonacci(4), 3)
        self.assertNotEqual(fibonacci(8), 21)
        self.assertNotEqual(fibonacci(19), 4181)
        self.assertNotEqual(fibonacci(7), 0)
    def testExceptions(self):
        self.assertFalse(fibonacci(-5))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

    



if __name__ == '__main__':
    unittest.main() # this runs our tests

