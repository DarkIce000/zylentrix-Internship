# User Management API

A Django REST framework based API that provides user management functionality with token-based authentication.

## Features

- User registration with password confirmation
- Token-based authentication
- Admin-only CRUD operations on user data
- Custom user model with additional fields (age)

## Requirements

- Python 3.8+
- Django 5.1.7
- Django REST framework 3.15.2
  
## Video Demo

<video src="https://github.com/user-attachments/assets/8eec7471-525b-46d5-8ee4-138bd29fdc86" > 


## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DarkIce000/zylentrix-Internship.git
   cd zylentrix-internship
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (required for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication Endpoints

- **Login:** `POST /api/login`

  - Requires username and password
  - Returns authentication token

- **Register:** `POST /api/register`
  - Fields: username, password, confirm_password, email, first_name, last_name, age

### User Management Endpoints (Admin Only )
> ⚠️ **Admin Access Required**
>
> To access these endpoints, you must either:
> - Create a superuser: `python manage.py createsuperuser`
> - Or enable staff status via Django admin dashboard
>
> Regular users cannot perform CRUD operations on user data.

- **List Users:** `GET /api/users/`
- **Create User:** `POST /api/users/`
- **Retrieve User:** `GET /api/users/<username>/`
- **Update User:** `PUT /api/users/<username>/`
- **Partial Update:** `PATCH /api/users/<username>/`
- **Delete User:** `DELETE /api/users/<username>/`

## Authentication

The API uses token-based authentication. To access protected endpoints:

1. Obtain a token through the login endpoint
2. Include the token in the Authorization header:
   ```
   Authorization: Token <your-token>
   ```

## User Model Fields

- username (required, unique)
- password (required)
- email
- first_name
- last_name
- age (optional)
- is_staff (for admin access)
- is_superuser (for superuser privileges)

## Security Features

- Password confirmation during registration
- Token-based authentication
- Admin-only access to user management endpoints
- Session and Basic authentication support
- Password hashing using Django's default hasher

## Project Structure

- `core/`: Project settings and root URL configuration
- `usermanagement/`: User management application
  - `models.py`: Custom user model
  - `views.py`: API views for user operations
  - `serializers.py`: User data serialization
  - `urls.py`: API endpoint routing

## License

This project is licensed under the MIT License.
