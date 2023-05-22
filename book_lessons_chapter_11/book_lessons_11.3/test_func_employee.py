import unittest
from class_Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('Mikhail', 'Kuznetsov', 10000)

    def test_give_default_raise(self):
        self.my_employee.five_raise()
        self.assertEqual(self.my_employee.salary, 15000)

    def test_give_custom_result(self):
        self.my_employee.five_raise(3000)
        self.assertEqual(self.my_employee.salary, 13000)

if __name__ == '__main__':
    unittest.main()

