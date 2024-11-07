import requests
import unittest
from unittest.mock import patch

# Write a Function
def fetch_joke():
    """
    Fetch a random joke from the icanhazdadjoke API.
    """
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "No joke available at the moment."

# Write Tests without Mocking
class TestWithoutMocking(unittest.TestCase):
    def test_fetch_joke(self):
        joke = fetch_joke()
        self.assertIsInstance(joke, str)

# Implement Mocking
class TestWithMocking(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_joke(self, mock_get):
        # Define the mock response data
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'joke': 'This is a mock joke.'}
        mock_get.return_value = mock_response

        # Test the function with the mocked response
        joke = fetch_joke()
        self.assertEqual(joke, 'This is a mock joke.')
        mock_get.assert_called_once_with("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})

# Print Results
if __name__ == '__main__':
    # Running tests without mocking
    print("Running tests without mocking:")
    unittest.main(verbosity=2, exit=False)

    # Running tests with mocking
    print("\nRunning tests with mocking:")
    unittest.main(verbosity=2)
