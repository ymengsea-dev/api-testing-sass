class AppException(Exception):
    """Base for all app-specific errors."""
    def __init__(self, message: str, status_code: int = 400, code: str = "error", details: any = None):
        self.message = message
        self.status_code = status_code
        self.code = code
        self.details = details
        super().__init__(message)
    
class InvalidCredentialsError(AppException):
    def __init__(self):
        super().__init__(
            message="Incorrect username or password",
            status_code=401,
            code="invalid_credentials",
        )

class UserAlreadyExistsError(AppException):
    def __init__(self, field: str):
        super().__init__(
            message=f"{field.capitalize()} already registered",
            status_code=400,
            code="user_already_exists",
            details={"field": field},
        )

class NotFoundError(AppException):
    def __init__(self, resource: str):
        super().__init__(
            message=f"{resource} not found",
            status_code=404,
            code="not_found",
        )