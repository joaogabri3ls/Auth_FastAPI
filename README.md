# Simple API with FastAPI

## Description

This project is a complete API for user management, including profile image manipulation. The API is built with FastAPI and uses SQLAlchemy, SQLModel, PostgreSQL, Alembic, and Docker to provide a robust and scalable solution.

## Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **SQLModel**: ORM and Pydantic for easy model definition and data validation.
- **PostgreSQL**: Relational database used to store API data.
- **Alembic**: Database migration tool.
- **Docker**: Containerization to simplify project execution.
- **JWT (JSON Web Tokens)**: Used for authentication and authorization.

## Installation and Setup

### Docker Downloads

- **Docker**: [Download Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Download Docker Compose](https://docs.docker.com/compose/install/)

### Project Initialization with Docker

1. **Build the project**

    ```bash
    docker-compose build
    ```

2. **Start the project**

    ```bash
    docker-compose up
    ```

    Docker will start the containers for the API and the database. The API will be available at `http://0.0.0.0:8000`.

## API Documentation

Interactive API documentation is available at [Swagger UI](http://0.0.0.0:8000/docs) and can be used to explore and test the API endpoints.

## API Usage Examples

### 1. Add a User

- **Method**: `POST`
- **Route**: `/user/register`
- **Description**: Registers a new user with a username, email, and password. The password will be hashed before being stored.
- **Request Example**:

    ```bash
    curl -d '{"username":"john_doe", "email":"john@example.com", "password":"strongpassword123"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/user/register
    ```

- **Response**:

    ```json
    {
        "msg": "success"
    }
    ```

### 2. Get All Users

- **Method**: `GET`
- **Route**: `/user/`
- **Description**: Retrieves a list of all registered users.
- **Request Example**:

    ```bash
    curl -X GET http://0.0.0.0:8000/user/
    ```

- **Response**:

    ```json
    [
        {
            "id": 1,
            "username": "john_doe",
            "email": "john@example.com",
            "imageURL": "https://s3.amazonaws.com/bucketname/imagename.jpg"
        }
    ]
    ```

### 3. User Login

- **Method**: `POST`
- **Route**: `/user/login`
- **Description**: Authenticates a user by providing the username and password. Returns a JWT token if authentication is successful.
- **Request Example**:

    ```bash
    curl -d 'username=john_doe&password=strongpassword123' -H "Content-Type: application/x-www-form-urlencoded" -X POST http://0.0.0.0:8000/user/login
    ```

- **Response**:

    ```json
    {
        "access_token": "<JWT_TOKEN>",
        "token_type": "bearer"
    }
    ```

### 4. Update User Profile Image

- **Method**: `PUT`
- **Route**: `/user/{user_id}/profile-image`
- **Description**: Updates the profile image of the specified user.
- **Request Example**:

    ```bash
    curl -F "file=@/path/to/image.jpg" -H "Authorization: Bearer <JWT_TOKEN>" -X PUT http://0.0.0.0:8000/user/1/profile-image
    ```

- **Response**:

    ```json
    {
        "msg": "Profile image updated successfully"
    }
    ```

## AWS Configuration

In the future, the API will be deployed to AWS. For details on AWS configuration and deployment, please refer to AWS-specific documentation.

