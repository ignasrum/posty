import json
import os

import requests

from posty.enum.http_method import HTTPMethod
from posty.logger import Logger


logger = Logger()

class Posty:
    def _load_file(self, file_path):
        filename = os.path.basename(file_path)
        return filename, open(file_path, "rb")

    def _populate_string_from_env(self, string, env):
        return string.format(**env)
    
    def _populate_list_from_env(self, listi, env):
        for index, value in enumerate(listi):
            if type(value) == str:
                listi[index] = self._populate_string_from_env(value, env)
        return listi

    def populate_dict_from_env(self, dicti, env):
        for key in dicti:
            typeof = type(dicti[key])
            if typeof == str:
                dicti[key] = self._populate_string_from_env(dicti[key], env)
            elif typeof == dict:
                dicti[key] = self.populate_dict_from_env(dicti[key], env)
            elif typeof == list:
                dicti[key] = self._populate_list_from_env(dicti[key], env)
            else:
                print("ERROR: UNKNOWN DATA STRUCTURE IN JSON")
        return dicti
    
    def load_json(self, file_path):
        req = json.loads(open(file_path, "r").read())
        return req

    def execute_json_request(self, req, env={}):
        req = self.populate_dict_from_env(req, env)
        files = {}
        if len(req["files"]) > 0:
            for file_path in req["files"]:
                filename, file_obj = self._load_file(file_path)
                files[filename] = file_obj
        self.request(
            req["url"],
            req["method"],
            url_params=req["url_params"],
            json=req["json"],
            auth=None,
            files=files,
            headers=req["headers"]
        )

    def request(self, url, method, url_params=None, json=None, auth=None, files={}, headers={}):
        response = requests.request(
            method=method,
            url=url,
            params=url_params,
            json=json,
            files=files,
            auth=auth,
            headers=headers)
        logger.log_request(response.request)
        print("\n")
        logger.log_time(response.elapsed)
        logger.log_response(response)
