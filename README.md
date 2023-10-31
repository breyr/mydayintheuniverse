# My Day in the Universe (MDitU)

My Day in the Universe (MDitU) is a Flask web application that allows users to explore the Astronomy Picture of the Day (APOD) provided by NASA's API. This application retrieves and displays the APOD image for a selected date.

## Prerequisites

Before running this project, ensure you have the following dependencies installed:

- Python >3.10.0
- Flask
- Requests
- Python-dotenv

You can install these dependencies using pip:

```bash
pip install Flask Flask-Session requests python-dotenv
```

## Getting Started

Clone the project repository:

```bash
Copy code
git clone https://github.com/breyr/mydayintheuniverse.git
cd mydayintheuniverse
```

Create a .env file in the project directory and set your environment variables:
API_KEY: Your API key for NASA's APOD API.
SECRET_KEY: A secret key for your Flask application.
Run the Flask application:

```bash
flask --app app.py run
```

The app will be available at http://127.0.0.1:5000/.

## Usage

Access the application by opening a web browser and navigating to http://127.0.0.1:5000/.

Enter a date in the provided date picker and click the "Submit" button to retrieve the APOD image for that date.

The application will display the image and additional information.

## Project Structure

app.py: The main Flask application file.

templates/: Contains HTML templates for the application.

static/: Contains static files, such as CSS and JavaScript.

styles.css: CSS file for styling the application.

index.js: JavaScript file for additional functionality

.env: Configuration file for storing environment variables.

## API Credits

This project utilizes NASA's Astronomy Picture of the Day (APOD) API. You can find more information about the API here: https://api.nasa.gov/.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

This project was created for educational and learning purposes.
