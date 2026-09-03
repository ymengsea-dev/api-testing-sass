from enum import Enum

# store generate purpose custom enum

class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"

class TestStatus(str, Enum):
    FAILED = "Failed"
    PASSED = "Passed"

