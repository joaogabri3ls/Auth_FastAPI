# Simple API with FastAPI

## Description

This project provides a complete API for user management with CRUD operations, including handling profile images. Built with FastAPI, SQLAlchemy, PostgreSQL, and Docker, it uses JWT for authentication.

## Technologies

- **FastAPI**: Web framework for building APIs with Python.
- **SQLAlchemy**: ORM for PostgreSQL database interaction.
- **PostgreSQL**: Relational database.
- **Docker**: Containerization for deployment.
- **JWT**: JSON Web Tokens for authentication.

## Installation and Setup

### Docker Requirements

- **Docker**: [Download Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Download Docker Compose](https://docs.docker.com/compose/install/)

### Building and Running the Project

1. **Build the Docker images:**

    ```bash
    docker-compose build
    ```

2. **Start the Docker containers:**

    ```bash
    docker-compose up
    ```

    The API will be available at `http://localhost:8000`.

## API Documentation

Interactive API documentation is available at [Swagger UI](http://localhost:8000/docs).

## API Endpoints

### 1. Register a New User

- **Method**: `POST`
- **Route**: `/user/register`
- **Description**: Registers a new user with a username, email, and password. The password will be hashed before being stored.
- **Request Body Example**:

    ```json
    {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "strongpassword123"
    }
    ```

- **Response**:

    ```json
    {
        "msg": "success"
    }
    ```

### 2. User Login

- **Method**: `POST`
- **Route**: `/user/login`
- **Description**: Authenticates a user by providing a username and password. Returns a JWT token if authentication is successful.
- **Request Form Example**:

    ```bash
    curl -d 'username=john_doe&password=strongpassword123' -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:8000/user/login
    ```

- **Response**:

    ```json
    {
        "access_token": "<JWT_TOKEN>",
        "token_type": "bearer"
    }
    ```

### 3. Get User Details

- **Method**: `GET`
- **Route**: `/user/{user_id}`
- **Description**: Retrieves details of a user by their ID.
- **Request Example**:

    ```bash
    curl -X GET http://localhost:8000/user/1
    ```

- **Response**:

    ```json
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "password": "hashedpassword",
        "imageURL": "https://s3.amazonaws.com/bucketname/imagename.jpg"
    }
    ```

### 4. Update User Details

- **Method**: `PUT`
- **Route**: `/user/{user_id}`
- **Description**: Updates details of a user by their ID.
- **Request Body Example**:

    ```json
    {
        "username": "john_doe",
        "email": "john.doe@example.com",
        "password": "newpassword123"
    }
    ```

- **Response**:

    ```json
    {
        "msg": "User updated successfully"
    }
    ```

### 5. Delete a User

- **Method**: `DELETE`
- **Route**: `/user/{user_id}`
- **Description**: Deletes a user by their ID.
- **Request Example**:

    ```bash
    curl -X DELETE http://localhost:8000/user/1
    ```

- **Response**:

    ```json
    {
        "msg": "User deleted successfully"
    }
    ```

### 6. Test Endpoint

- **Method**: `GET`
- **Route**: `/test`
- **Description**: A simple test endpoint to verify that the API is working.
- **Response**:

    ```json
    "It works"
    ```

## AWS Configuration

The API is planned to be deployed on AWS in the future. Documentation for AWS deployment will be provided separately.


