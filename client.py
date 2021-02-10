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

    def __compose_endpoint(self, endpoint, *endpoints):
        url = self.base_url + endpoint + '/'
        for endpoint in endpoints:
            url += str(endpoint) + '/'
        return url[:-1]

    def __compose_request(self, endpoint, *endpoints, **kwargs):
        url = self.__compose_endpoint(endpoint, *endpoints)
        payload = kwargs.get('payload')
        req_dict = dict(url=url, params=payload, headers=self.headers)
        return req_dict

    @check_request
    def get_sent_campaigns(self, payload=None):
        req_dict = self.__compose_request('sent_campaigns', payload)
        return requests.get(**req_dict)

    @check_request
    def get_sent_campaign(self, id):
        req_dict = self.__compose_request('sent_campaigns', id)
        return requests.get(**req_dict)


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    DOMAIN = os.getenv('DOMAIN')
    client = MailrelayClient(API_KEY, DOMAIN)
    campaigns = client.get_sent_campaigns(payload={'q[sender_id_eq]': 2})
