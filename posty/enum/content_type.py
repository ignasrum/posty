from enum import Enum


class ContentType(Enum):
    JSON = "application/json"
    URL_ENCODE = "application/x-www-form-urlencoded"
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"
    MULTIPART = "multipart/form-data"
    JPEG = "image/jpeg"
