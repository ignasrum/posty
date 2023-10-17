# posty
A free and open source CLI API platform

# Dependencies
Python 3.10+ <br>
Pip packages:
* [requests](https://github.com/psf/requests)
* [pillow](https://github.com/python-pillow/Pillow)

# Installation
```
pip install "git+https://github.com/ignasrum/posty.git"
```

# Usage
```
posty environment.json request.json
```

# Environment example
```
{
    "bearer_token": "testing_bearer",
    "hello": "world",
    "file.txt": "./path/to/file.txt"
}
```

# Request example
```
{
    "url": "https://httpbin.org/bearer",
    "method": "GET",
    "url_params": {},
    "json": {},
    "auth": {},
    "files": [],
    "headers": {"Authorization": "Bearer {bearer_token}"}
}
```
