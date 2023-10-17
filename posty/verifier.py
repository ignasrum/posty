class Verifier:
    def key_in_request(self, key, request):
        if key not in request.keys():
            print(f"Key \"{key}\" not in request")
            return False
        return True
    
    def key_is_dict(self, key, request):
        if not isinstance(request[key], dict):
            print(f"Value of \"{key}\" is not a JSON object")
            return False
        return True

    def key_is_list(self, key, request):
        if not isinstance(request[key], list):
            print(f"Value of \"{key}\" is not a JSON array")
            return False
        return True

    def key_is_str(self, key, request):
        if not isinstance(request[key], str):
            print(f"Value of \"{key}\" is not a string")
            return False
        return True

    def verify_request(self, request):
        if not isinstance(request, dict):
            print("Request is not a JSON object")
            return 1
        if len(request.keys()) != 7:
            print("Request key count is not 7")
            return 1
        if not self.key_in_request("url", request): return 1
        if not self.key_in_request("method", request): return 1
        if not self.key_in_request("url_params", request): return 1
        if not self.key_in_request("json", request): return 1
        if not self.key_in_request("auth", request): return 1
        if not self.key_in_request("files", request): return 1
        if not self.key_in_request("headers", request): return 1

        if not self.key_is_str("url", request): return 1
        if not self.key_is_str("method", request): return 1
        if not self.key_is_dict("url_params", request): return 1
        if not self.key_is_dict("json", request): return 1
        if not self.key_is_dict("auth", request): return 1
        if not self.key_is_list("files", request): return 1
        if not self.key_is_dict("headers", request): return 1

        return 0
