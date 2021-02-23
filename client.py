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

    def __compose_get_query(self, **kwargs):
        '''Compose the paramateres for the get payload.
        For queriable parameters
        '''
        params = {}
        for key, value in kwargs.items():
            if value:
                if 'page' not in key:
                    params[f'q[{key}]'] = value
                else:
                    params[key] = kwargs[key]
        return params

    def __compose_request(self, endpoint, *endpoints, **kwargs):
        '''Create a request dictionary to pass to the request function.'''
        url = self.__compose_endpoint(endpoint, *endpoints)
        payload = self.__compose_get_query(**kwargs)
        req_dict = dict(url=url, params=payload, headers=self.headers)
        return req_dict

    @check_request
    def get_sent_campaigns(
        self,
        page=None,
        per_page=None,
        id_eq=None,
        id_gteq=None,
        id_lteq=None,
        subject_eq=None,
        subject_cont=None,
        sender_id_eq=None,
        sender_id_gteq=None,
        sender_id_lteq=None,
        status_eq=None,
        status_cont=None,
    ):
        """
       Get sent campaigns for statistics.

        Parameters
        ----------
        **kwargs :
        page (int): Page number
        per_page (int): Number of records per page
        id_eq (int): Search: ID equals
        id_gteq (int): Search: ID greater than or equal to
        id_lteq (int): Search: ID less than or equal to
        subject_eq (str): Search: Subject equals
        subject_cont (str): Search: Subject contains
        sender_id_eq (int): Search: Sender equals
        sender_id_gteq (int): Search: Sender greater than or equal to
        sender_id_lteq (int): Search: Sender less than or equal to
        status_eq (str): Search: Status equals
        status_cont (str): Search: Status contains

        Returns
        ----------
        Response as dict.
        """
        params = locals()
        params.pop('self')
        req_dict = self.__compose_request(
            'sent_campaigns',
            **params
        )
        return requests.get(**req_dict)

    @check_request
    def get_sent_campaign(self, id):
        req_dict = self.__compose_request('sent_campaigns', id)
        return requests.get(**req_dict)


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    DOMAIN = os.getenv('DOMAIN')
    client = MailrelayClient(API_KEY, DOMAIN)
    campaigns = client.get_sent_campaigns(sender_id_eq=2)
    campaign = client.get_sent_campaign(20)
    print(campaign)
