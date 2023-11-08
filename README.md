# Django REST API Project

This is a simple Django REST API project built using the Django REST framework. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a collection of drinks through the `/drinks` endpoint.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Running the Server](#running-the-server)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Provides CRUD operations (Create, Read, Update, Delete) for managing drinks.
- Built with the Django REST framework, making it easy to extend and customize.
- Ready to be used as a foundation for building RESTful APIs.

## Getting Started

### Prerequisites

Before you get started, make sure you have the following prerequisites installed:

- Python 3.12
- Django 4.2.7
- Django REST framework 3.14.0

You can install these packages using pip.

```bash
pip install django djangorestframework
```

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/siranchao/django_rest.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django_rest
   ```

3. Perform the initial setup of the Django project:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Runing the server:

   ```bash
   python manage.py runserver
   ```
