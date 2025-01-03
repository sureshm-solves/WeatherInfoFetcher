
# Weather Info Fetcher 🌦️

A Python project to fetch and display the current weather information for a specified city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data, including:
    - Temperature
    - Weather condition
    - Humidity
- Uses the OpenWeatherMap API.
- Simple and modular code design for easy extensibility.
- Includes unit tests for improved reliability.

---

## Requirements
- Python 3.7 or above
- An OpenWeatherMap API Key

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/WeatherInfoFetcher.git
   cd WeatherInfoFetcher
   ```

2. **Set Up a Virtual Environment (Optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install requests
   ```

---

## Usage
1. **Obtain an API Key**:
    - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key.

2. **Run the Script**:
   ```bash
   python main.py
   ```
    - Enter the city name when prompted.

3. **Sample Output**:
   ```plaintext
   Enter the city name: London
   Weather in London:
   Temperature: 15°C
   Condition: Clear sky
   Humidity: 60%
   ```

---

## Testing
This project includes unit tests for key functionality.

1. **Run Tests**:
   ```bash
   python -m unittest discover tests
   ```

---

## Project Structure
```
WeatherInfoFetcher/
├── main.py                # Main script to run the application
├── weather_info.py        # Contains weather-fetching logic
├── tests/                 # Unit test folder
│   ├── __init__.py
│   └── test_weather_info.py
└── README.md              # Project documentation
```

---

## Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- OpenWeatherMap API for providing free weather data.
