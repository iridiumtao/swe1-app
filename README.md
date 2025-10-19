# swe1-app

[![Build Status](https://app.travis-ci.com/iridiumtao/swe1-app.svg?token=WDPk8NaA3e3AEm6N3wdc&branch=main)](https://app.travis-ci.com/iridiumtao/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/iridiumtao/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/iridiumtao/swe1-app?branch=main)

somerandomtexts

## Testing

This project uses pytest for testing. To run the tests:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

The test suite includes:
- Model tests for Question and Choice models
- View tests for index, detail, and results views
- Integration tests using pytest-django

## Running the Project

1.  **Install dependencies:**
    ```bash
    uv sync
    # or
    pip install -r requirements.txt
    ```

2.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

3.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.
