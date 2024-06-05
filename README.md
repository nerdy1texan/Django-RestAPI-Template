# Django Rest Framework API Template for Courses

This repository contains a Django Rest Framework (DRF) API template for managing a list of courses. The API provides endpoints to list, create, retrieve, update, and delete course entries.

## Features

- List all courses
- Retrieve details of a specific course
- Create a new course
- Update an existing course
- Delete a course

## Requirements

- Python 3.x
- Django
- Django Rest Framework

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

The API provides the following endpoints:

### List all courses

- **URL:** `/courses/`
- **Method:** `GET`
- **Response:**

    ```json
    [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/courses/1/",
            "name": "Python Programming For Everyone",
            "language": "Python",
            "price": "$49"
        },
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/courses/2/",
            "name": "Ruby Programming For Everyone",
            "language": "Ruby",
            "price": "$49"
        },
        {
            "id": 3,
            "url": "http://127.0.0.1:8000/courses/3/",
            "name": "Javascript Programming For Everyone",
            "language": "JS Programming",
            "price": "$49"
        },
        {
            "id": 4,
            "url": "http://127.0.0.1:8000/courses/4/",
            "name": "HTML Programming",
            "language": "HTML",
            "price": "$49"
        }
    ]
    ```

### Retrieve details of a specific course

- **URL:** `/courses/{id}/`
- **Method:** `GET`
- **Response:**

    ```json
    {
        "id": 1,
        "url": "http://127.0.0.1:8000/courses/1/",
        "name": "Python Programming For Everyone",
        "language": "Python",
        "price": "$49"
    }
    ```

### Create a new course

- **URL:** `/courses/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "name": "Full Stack Development For Everyone",
        "language": "Python, HTML, JavaScript, CSS",
        "price": "$69"
    }
    ```

- **Response:**

    ```json
    {
        "id": 5,
        "url": "http://127.0.0.1:8000/courses/5/",
        "name": "Full Stack Development For Everyone",
        "language": "Python, HTML, JavaScript, CSS",
        "price": "$69"
    }
    ```

### Update an existing course

- **URL:** `/courses/{id}/`
- **Method:** `PUT`
- **Request Body:**

    ```json
    {
        "name": "Updated Course Name",
        "language": "Updated Language",
        "price": "$99"
    }
    ```

### Delete a course

- **URL:** `/courses/{id}/`
- **Method:** `DELETE`

## Project Structure

- `courses/`: Contains the Django app for courses.
- `courses/urls.py`: URL routing for the courses app.
- `courses/views.py`: View logic for the courses app.
- `courses/serializers.py`: Serializers for the courses app.
- `manage.py`: Django management script.
- `db.sqlite3`: SQLite database file.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License.
