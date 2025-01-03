import unittest

from weather_info import  fetch_weather_data, parse_weather_data
from unittest.mock import patch

class TestWeatherInfo(unittest.TestCase):
    def test_parse_weather_data_valid(self):
        mock_data = {
            "main" : {"temp": 20.5, "humidity": 65},
            "weather":[{"description" : "clear sky"}]
        }
        expected_output = {
            "temperature" : 20.5,
            "weather" : "clear sky",
            "humidity": 65
        }
        self.assertEqual(parse_weather_data(mock_data), expected_output)

    def test_parse_weather_data_invalid(self):
        mock_data = {"main":{"temp":20.5}} # Missing weather key
        with self.assertRaises(ValueError):
            parse_weather_data(mock_data)

    # Mock Test
    @patch("weather_info.requests.get")
    def test_fetch_weather_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            "main" : {"temp": 20.5, "humidity": 65},
            "weather":[{"description" : "Rainy"}]
        }
        mock_response.raise_for_status.return_value = None

        data = fetch_weather_data("London", "dummy_key")
        self.assertEqual(data["main"]["temp"], 20.5)
        self.assertEqual(data["weather"][0]["description"], "Rainy")

if __name__ == "__main__":
    unittest.main()