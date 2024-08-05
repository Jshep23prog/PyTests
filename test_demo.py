import unittest
import demo

#skip decorator
# @unittest.skip("Skipping this test for example reasons")
class TestCalculate(unittest.TestCase):
#add a setup method to keep code DRY
    def setUp(self):
        self.calculate = demo.Calculate() #is now an instance variable

    #teardown is useful to perfomr certain actions after the test has been completed
    # def tearDown(self):
    #     print("This is a teardown method, executes after each test")

    def test_add(self):
        self.assertEqual(self.calculate.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculate.subtract(5, 3), 2)

    # @unittest.skipIf(True, "Skipping because cond is true")
    def test_multiply(self):
        self.assertEqual(self.calculate.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calculate.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calculate.divide(10, 0)



if __name__ == '__main__':
    unittest.main()





# #use a built in unit testing module
# import unittest
# #to test functions, we need to import from where function is housed
# import demo

# #create a class that inherits from UTM

# class TestDemo(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(demo.add(2, 3), 5)
#         self.assertEqual(demo.add(5, 5), 10)
#         self.assertEqual(demo.add(23, 5), 28)

#     def test_subtract(self):
#         self.assertEqual(demo.subtract(5, 3), 2)
#         self.assertEqual(demo.subtract(15, 3), 12)
#         self.assertEqual(demo.subtract(100, 7), 93)

#     def test_multiply(self):
#         self.assertEqual(demo.multiply(5, 3), 15)
#         self.assertEqual(demo.multiply(15, 3), 45)
#         self.assertEqual(demo.multiply(100, 7), 700)

#     def test_divide(self):
#         self.assertEqual(demo.divide(9, 3), 3)
#         self.assertEqual(demo.divide(15, 3), 5)
#         self.assertEqual(demo.divide(100, 10), 10)

# #write code to run unit tests with fewer keystrokes
# if __name__ == '__main__':
#     unittest.main()