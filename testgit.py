import unittest
from unittest.mock import patch
from git import getData

class TestGit(unittest.TestCase):
    
    def test_getData_successful(self):
        result = getData("hboinippa", "triangle567")
        self.assertEqual(result, 19)

    def test_getData_unsuccessful(self):
        result = getData("ahsgdkeh", "ahsjdgs")
        self.assertNotEqual(result, 19)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
