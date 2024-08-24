from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(None, description="The unique identifier of the user.")
    username: str = Field(..., description="The username of the user.", example="john_doe")
    email: str = Field(..., description="The email address of the user.", example="john@example.com")
    password: str = Field(..., description="The user's password.", example="strongpassword123")
    imageURL: str = Field(None, description="The URL of the user's profile image stored in AWS S3.", example="https://s3.amazonaws.com/bucketname/imagename.jpg")


class UserLogin(BaseModel):
    username: str = Field(..., description="The username of the user.", example="john_doe")
    password: str = Field(..., description="The user's password.", example="strongpassword123")    