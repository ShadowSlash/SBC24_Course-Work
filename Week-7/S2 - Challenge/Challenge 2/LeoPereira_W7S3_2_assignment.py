import requests
import unittest
from unittest.mock import Mock, patch

# Write a class with an external dependency
class JokeService:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_joke(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json().get('joke')
        else:
            return "No joke available at the moment."

# Write tests using mock objects
class TestJokeService(unittest.TestCase):
    def setUp(self):
        self.api_url = "https://icanhazdadjoke.com/"
        self.joke_service = Joke_Service(self.api_url)

    @patch('requests.get')
    def test_get_joke_success(self, mock_get):
        # Define the mock response data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'joke': 'This is a mock joke.'}
        mock_get.return_value = mock_response

        # Test the function with the mocked response
        joke = self.joke_service.get_joke()
        self.assertEqual(joke, 'This is a mock joke.')
        mock_get.assert_called_once_with(self.api_url)

    @patch('requests.get')
    def test_get_joke_failure(self, mock_get):
        # Define the mock response data for a failed request
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test the function with the mocked response
        joke = self.joke_service.get_joke()
        self.assertEqual(joke, 'No joke available at the moment.')
        mock_get.assert_called_once_with(self.api_url)

# Print results
if __name__ == '__main__':
    unittest.main(verbosity=2)