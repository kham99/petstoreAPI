from typing import Optional
import allure
import requests
from urllib.parse import urljoin


class HTTPClient:

    def __init__(self, base_url: str):
        self._base_url = base_url

    def get(self, path: str, expected_status_code: Optional[int] = None,
            params: Optional[dict] = None) -> requests.Response:
        response = self._send_request(path=path, method="get", params=params, expected_status_code=expected_status_code)
        return response

    def post(self, path: str, expected_status_code: Optional[int] = None,
             json: Optional[dict] = None) -> requests.Response:
        response = self._send_request(path=path, method="post", json=json, expected_status_code=expected_status_code)
        return response

    def delete(self, path: str, expected_status_code: Optional[int] = None):
        response = self._send_request(path=path, method="delete", expected_status_code=expected_status_code)
        return response

    def put(self, path: str, expected_status_code: Optional[int] = None,
            json: Optional[dict] = None) -> requests.Response:
        response = self._send_request(path=path, method="put", json=json, expected_status_code=expected_status_code)
        return response

    def _send_request(self, path: str, method: str, expected_status_code: Optional[int] = None,
                      **kwargs) -> requests.Response:
        print(f"base url: {self._base_url}")
        url = f"{self._base_url}/{path}"
        print("url: ", url)
        with allure.step(f"Send {method.upper()} to {url}"):
            response = requests.request(method=method, url=url, **kwargs)
            allure.attach(response.text, name="Response", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Check status code"):
            if expected_status_code:
                assert response.status_code == expected_status_code, (f"Expected status code {expected_status_code},"
                                                                      f"got {response.status_code}")
        return response
