import requests
from dotenv import load_dotenv
import os
import json
from errors import check_request


load_dotenv()


class MailrelayClient(object):
    def __init__(self, api_key, domain):
        self.headers = {'x-auth-token': api_key}
        self.base_url = f'https://{domain}/api/v1/'

    def __compose_request(self, endpoint, payload=None):
        req_dict = dict(url=f'{self.base_url}{endpoint}',
                        params=payload,
                        headers=self.headers)
        return req_dict

    @check_request
    def get_sent_campaigns(self):
        req_dict = self.__compose_request('sent_campaigns')
        return requests.get(**req_dict)


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    DOMAIN = os.getenv('DOMAIN')
    client = MailrelayClient(API_KEY, DOMAIN)
    campaigns = client.get_sent_campaigns()
