import requests
from requests.auth import HTTPBasicAuth


class User:
    __BASE_URL = "http://127.0.0.1:8080"

    def __init__(self, log):
        self.logger = log
        self.session = requests.Session()

    def get_token(self, username, password):
        url = f"{self.__BASE_URL}/auth"
        auth = HTTPBasicAuth(username, password)

        try:
            self.logger.info(f"Making request for getting access token")
            response = self.session.post(url, auth=auth)
            response_dict = {
                'status_code': response.status_code,
                'access_token': response.json().get('access_token'),
                'message': response.json().get('message')

            }

            self.logger.info(f"Access token was successfully obtained")
            return response_dict

        except requests.HTTPError as e:
            self.logger.error(f"HTTP error occurred {e}")
            raise RuntimeError(f"HTTP error occurred {e}")

    def get_cars(self, authenticate, sort_by: str = None, limit: int = None):
        url = f"{self.__BASE_URL}/cars"
        self.session.headers.update({'Authorization': 'Bearer ' + authenticate['access_token']})
        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        try:
            self.logger.info(f"Making request for getting cars list")
            response = self.session.get(url, params=params)

            self.logger.info(f"Cars list was successfully obtained")
            return response.json()

        except requests.HTTPError as e:
            self.logger.error(f"HTTP error occurred {e}")
            raise RuntimeError(f"HTTP error occurred {e}")
