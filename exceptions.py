from fastapi import HTTPException, status


class MongoException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code= 503, detail=detail)

class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code = 404, detail = "User not found")

class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail="Username already exists")

class InvalidPassword(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid password")

class InvalidUsername(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid username")

class InvalidToken(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=401, detail=detail)

class DocNotExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Document dosn't exist")

class NotAuthUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="username does not have access to the todo document")

class DateFormatError(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=409, detail=f"client date time field: {detail}")
