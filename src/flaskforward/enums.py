from enum import Enum


# sub class of Enum to return the string values in a list for values()
class EnumList(str, Enum):
    @classmethod
    def values(cls):
        return [e.value for e in cls]


# potential request methods
class RequestMethods(EnumList):
    GET    = "GET"
    DELETE = "DELETE"
    PATCH  = "PATCH"
    POST   = "POST"
    PUT    = "PUT"



# Request mimetypes that cause flask to automatically parse the body into the flask.Request.form object
class ParsedMimeTypes(EnumList):
    URL       = 'application/x-www-form-urlencoded'
    MULTIPART = 'multipart/form-data'