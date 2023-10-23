import unittest
from unittest.mock import patch
from git import getData

class TestGit(unittest.TestCase):
    
     @patch('Git.requests.get')
    def test_getData(self, mock_requests):
        mock_response = [{'commit': {'message': 'Initial commit'}}, 
                         {'commit': {'message': 'Updated readme file'}}]
        mock_requests.return_value.json.return_value = mock_response

        result = getData("hboinippa", "triangle567")
        self.assertEqual(result, 19)

     @patch('Git.requests.get')
    def test_getData_error(self, mock_requests):
        mock_requests.side_effect = Exception('error')
        with self.assertRaises(Exception):
            getData("hboinipa", "triangle567")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
