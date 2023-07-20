# DogProject - Django Web Application

![Django](https://img.shields.io/badge/Django-3.2.6-green.svg)

## Introduction

This repository contains the source code for the DogProject, a Django web application developed for the CSE2252 Web Application Development Lab Final Exam. You will find the question of the exam in the [Questions.md](./Questions.md) file. The DogProject allows users to manage a list of dogs available in a DogShop through a RESTful API.

## Getting Started

To get started with the DogProject, follow the instructions below:

### Prerequisites

Before running the project, make sure you have the following installed on your system:

- Python (>= 3.6)
- Django (3.2.6)
- Django Rest Framework
- Git

### Installation

1. Clone the repository using the following command:

```
git clone https://github.com/mdhasnainali/CSE2252-Web-Application-Development-Lab-Final-Exam.git
```

2. Change the directory to the project folder:

```
cd CSE2252-Web-Application-Development-Lab-Final-Exam
```

3. Create and activate a virtual environment (optional but recommended):

```
python -m venv env
source env/bin/activate   # On Windows, use: env\Scripts\activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Generate a secret key for Django settings:

```
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated secret key and paste it in the `DogProject/settings.py` file under the `SECRET_KEY` variable.

### Database Setup

1. Apply the migrations to set up the database:

```
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser to access the Django admin interface (optional but useful for testing):

```
python manage.py createsuperuser
```

### Running the Development Server

Start the Django development server with the following command:

```
python manage.py runserver
```

The development server should now be running at `http://127.0.0.1:8000/`.

## API Documentation

The DogProject provides a RESTful API for managing dogs in the DogShop. Below is the documentation for the available endpoints:

### Retrieving a Single Dog by ID

**URL:** `/api/dogs/<dog_id>/`
**Method:** GET
**Description:** Retrieves a single dog by its ID.

### Listing All Dogs

**URL:** `/api/dogs/`
**Method:** GET
**Description:** Retrieves a list of all dogs in the DogShop.

### Creating a New Dog

**URL:** `/api/dogs/`
**Method:** POST
**Description:** Creates a new dog in the DogShop.

**Request Body:**

```json
{
  "name": "Example Dog",
  "price": 50,
  "breed": "Example Breed",
  "description": "Example Description"
}
```

### Updating an Existing Dog

**URL:** `/api/dogs/<dog_id>/`
**Method:** PUT
**Description:** Updates an existing dog in the DogShop.

**Request Body:**

```json
{
  "name": "Updated Dog Name",
  "price": 60,
  "breed": "Updated Breed",
  "description": "Updated Description"
}
```

### Deleting a Dog

**URL:** `/api/dogs/<dog_id>/`
**Method:** DELETE
**Description:** Deletes a dog from the DogShop.

## API Documentation with Swagger

The DogProject API is documented using Swagger, which provides an interactive and user-friendly interface to explore and test the API endpoints.

### Swagger Documentation URL

You can access the Swagger documentation at:

```
http://127.0.0.1:8000/swagger/
```

Click on the above URL to open the Swagger UI, where you can find detailed information about the API endpoints, request and response payloads, and even perform API testing directly from the browser.

### Swagger UI

![Swagger UI](./swagger.gif)


## Testing Strategy

Testing is crucial to ensure the functionality and reliability of the DogProject. Below is the testing strategy:

### Unit Testing

Unit tests will be used to test individual components of the application, such as models, views, and serializers. For example, to test the Dog model:

```
python manage.py test
```

## Conclusion

The DogProject is a fully functional Django web application that provides a RESTful API for managing dogs in the DogShop. Feel free to explore the API endpoints and use it for your web application development needs.

If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request. Happy coding! 🐶

