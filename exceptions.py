from fastapi import HTTPException, status


class MongoException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)

class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")

class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

class InvalidPassword(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

class InvalidUsername(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")

class InvalidToken(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class DocNotExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Document dosn't exist")

class NotAuthUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="username does not have access to the todo document")

class DateFormatError(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=f"client date time field: {detail}")

class NotConfigured(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="CONFIG_PATH environment variable is not set")

class FileConError(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="can't open the config file")
