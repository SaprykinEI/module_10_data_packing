import unittest
from classEmployer import Employer

class TestEmployer(unittest.TestCase):
    employer = Employer('test_name', 'test_surname', 'test_phone')

    def test_1_init(self):
        self.assertEqual(len(Employer.employers_dict), 1)
        self.assertEqual(Employer.employers_dict, {'test_phone': ['test_name', 'test_surname']})