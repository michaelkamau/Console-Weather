import unittest
from console_weather.utilities import degrees_to_direction


class DegreesToDirectionTests(unittest.TestCase):
    def test_converts_to_north(self):
        """
        Should convert to North direction correctly
        """
        self.assertEqual('North', degrees_to_direction(10))

    def test_converts_to_NorthNorthEast(self):
        """
        Should convert to NNE direction correctly
        """
        self.assertEqual('North North East', degrees_to_direction(11.26))

    def test_converts_to_NorthEast(self):
        """
        Should convert to NE direction correctly
        """
        self.assertEqual('North East', degrees_to_direction(33.76))


if __name__ == '__main__':
    unittest.main()