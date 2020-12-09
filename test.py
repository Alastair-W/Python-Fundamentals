import unittest
import math


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

print(coins(87))
print(coins(30))
print(coins(1267))
print(coins(20))
print(coins(1))
print(coins(0))
print(coins(-43))


class coinsTest(unittest.TestCase):
    def calculations(self):
        self.assertEqual(coins(87), [3,1,0,2])
        self.assertEqual(coins(30), [1,0,1,0])
        self.assertEqual(coins(1267), [50,1,1,2])
        self.assertEqual(coins(20), [0,2,0,0])
        self.assertEqual(coins(1), [0,0,0,1])
    def errors(self):
        self.assertFalse(coins(0))
        self.assertFalse(coins(-43))
    def setUp(self):
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
    # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests