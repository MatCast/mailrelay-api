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
        no_query = ['page', 'unique', 'include']
        for key, value in kwargs.items():
            if value:
                is_query = True
                for keyword in no_query:
                    if key in keyword:
                        is_query = False
                if is_query:
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

    @check_request
    def get_sent_campaign_clicks(
        self,
        id,
        unique=False,
        page=None,
        browser_eq=None,
        browser_cont=None,
        city_eq=None,
        city_cont=None,
        state_eq=None,
        state_cont=None,
        country_eq=None,
        country_cont=None,
        ip_eq=None,
        ip_cont=None,
    ):
        """
       Get sent campaigns for statistics.

        Parameters
        ----------
        page (int): Page number
        per_page (int): Number of records per page
        unique (bool): Unique impressions grouped by sent email
        browser_eq (str): Search: Browser equals
        browser_cont (str): Search: Browser contains
        city_eq (str): Search: City equals
        city_cont (str): Search: City contains
        state_eq (str): Search: State equals
        state_cont (str): Search: State contains
        country_eq (str): Search: Country equals
        country_cont (str): Search: Country contains
        ip_eq (str): Search: IP equals
        ip_cont (str): Search: IP contains

        Returns
        ----------
        Response as dict.
        """
        params = locals()
        params.pop('self')
        req_dict = self.__compose_request('sent_campaigns', id, 'clicks',
                                          **params)
        return requests.get(**req_dict)

    @check_request
    def get_sent_campaign_impressions(
        self,
        id,
        unique=False,
        page=None,
        browser_eq=None,
        browser_cont=None,
        city_eq=None,
        city_cont=None,
        state_eq=None,
        state_cont=None,
        country_eq=None,
        country_cont=None,
        ip_eq=None,
        ip_cont=None,
    ):
        """
       Get sent campaigns for statistics.

        Parameters
        ----------
        page (int): Page number
        per_page (int): Number of records per page
        unique (bool): Unique impressions grouped by sent email
        browser_eq (str): Search: Browser equals
        browser_cont (str): Search: Browser contains
        city_eq (str): Search: City equals
        city_cont (str): Search: City contains
        state_eq (str): Search: State equals
        state_cont (str): Search: State contains
        country_eq (str): Search: Country equals
        country_cont (str): Search: Country contains
        ip_eq (str): Search: IP equals
        ip_cont (str): Search: IP contains

        Returns
        ----------
        Response as dict.
        """
        params = locals()
        params.pop('self')
        req_dict = self.__compose_request('sent_campaigns', id, 'impressions',
                                          **params)
        return requests.get(**req_dict)


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    DOMAIN = os.getenv('DOMAIN')
    client = MailrelayClient(API_KEY, DOMAIN)
    campaigns = client.get_sent_campaigns(sender_id_eq=2)
    campaign = client.get_sent_campaign(20)
    print(campaign)
