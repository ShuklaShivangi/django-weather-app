# Django Weather App

This is a weather application built with Django that retrieves weather data from the OpenWeatherMap API and displays it in a user-friendly interface.

## Features

- Fetches and displays current weather data based on user input.
- Uses the OpenWeatherMap API for weather data.
- Built with Django framework.

## Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/django-weather-app.git
    ```
    
2. **Navigate to Project Directory:**
    ```bash
    cd django-weather-app
    ```

3. **Set Up Virtual Environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

7. **Open in Browser:**
    Visit `http://127.0.0.1:8000/` to view the application.

## Configuration

- **API Key:** Ensure you have a valid OpenWeatherMap API key. Configure it in your Django settings file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
