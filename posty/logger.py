import json
import io

from PIL import Image

from posty.enum.content_type import ContentType


def print_cyan(skk): print("\033[96m{}\033[00m".format(skk))
def print_green(skk): print("\033[92m{}\033[00m".format(skk))
def print_yellow(skk): print("\033[93m{}\033[00m".format(skk))
def print_red(skk): print("\033[91m{}\033[00m".format(skk))
def print_purple(skk): print("\033[95m{}\033[00m".format(skk))


class Logger:
    def log_data(self, data, content_type):
        print_green("Data:")
        match content_type:
            case ContentType.JSON.value:
                json_data = json.loads(data.decode("utf8"))
                json_formatted = json.dumps(json_data, indent=4)
                print(f"{json_formatted}")
            case ContentType.JPEG.value:
                print("JPEG")
                img = Image.open(io.BytesIO(data))
                img.show()
            case ContentType.MULTIPART.value:
                print("MULTIPART")
            case ContentType.URL_ENCODE.value:
                print(data)
            case ContentType.TEXT_HTML.value:
                print(data)
            case ContentType.TEXT_PLAIN.value:
                print(data)
            case _:
                print(f"Unexpected data type: {content_type}")

    def log_request(self, request):
        print_yellow("Request:")
        print_green("URL:")
        print(f"{request.url}")
        print_green("Method:")
        print(f"{request.method}")
        try:
            # may fail getting content-type
            # may fail opening image (Pillow not installed etc)
            content_type = request.headers["content-type"]
            print_green("Content-Type:")
            print(f"{content_type}")
            self.log_data(request.body, content_type)
        except Exception:
            pass
        print_green("Headers:")
        print(f"{json.dumps(request.headers.__dict__['_store'], indent=4)}")

    def log_response(self, response):
        print_yellow("Response:")
        print_green("Status code:")
        print(f"{response.status_code}")
        print_green("Headers:")
        print(f"{json.dumps(response.headers.__dict__['_store'], indent=4)}")
        data = response.content
        self.log_data(data, response.headers["content-type"])

    def log_time(self, time):
        print_yellow("Response time:")
        time = time.total_seconds()
        if time < 1:
            print(f"--- {(time) * 1000} milliseconds ---")
        else:
            print(f"--- {time} seconds ---")