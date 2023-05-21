import unittest
from city_function import get_formatted_string_city_country

class CityFunctionTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string_city_country = get_formatted_string_city_country('santiago', 'chile')
        self.assertEqual(formatted_string_city_country, 'Santiago, Chile')


    def test_city_country_population(self):
        formatted_string_city_country = get_formatted_string_city_country('santiago', 'chile', '5000')
        self.assertEqual(formatted_string_city_country, 'Santiago, Chile - Population 5000')

if __name__ == '__main__':
    unittest.main()