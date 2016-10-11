import unittest
from console_weather.utilities import degrees_to_direction


class DegreesToDirectionTests(unittest.TestCase):
    def test_converts_to_north(self):
        """
        Should convert to North direction correctly
        """
        self.assertEqual('North', degrees_to_direction(10))


if __name__ == '__main__':
    unittest.main()