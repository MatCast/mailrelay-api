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

    # ##### SENT CAMPAIGNS #####
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
        req_dict = self.__compose_request('sent_campaigns', **params)
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
        per_page=None,
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
        per_page=None,
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

    @check_request
    def get_sent_campaign_sent_emails(
        self,
        id,
        page=None,
        per_page=None,
        include_impressions=False,
        include_clicks=False,
        include_unsubscribe_events=False,
        email_eq=None,
        email_cont=None,
        status_eq=None,
        status_cont=None,
        processed_at_eq=None,
        processed_at_gteq=None,
        processed_at_lteq=None,
        delivered_at_eq=None,
        delivered_at_gteq=None,
        delivered_at_lteq=None,
        bounced_at_eq=None,
        bounced_at_gteq=None,
        bounced_at_lteq=None,
        bounce_category_eq=None,
        bounce_category_cont=None,
        soft_bounced_at_eq=None,
        soft_bounced_at_gteq=None,
        soft_bounced_at_lteq=None,
    ):
        """
       Get sent campaigns for statistics.

        Parameters
        ----------
        page (int): Page number
        per_page (int): Number of records per page
        include_impressions (bool): Include impressions in the results,
        include_clicks (bool): Include clicks in the results,
        include_unsubscribe_events (bool): Include unsubscribe events in the results,
        email_eq (str): Search: Email equals,
        email_cont (str): Search: Email contains,
        status_eq (str): Search: Status equals,
        status_cont (str): Search: Status contains,
        processed_at_eq (date_time): Search: Processed at equals,
        processed_at_gteq (date_time): Search: Processed at greater than or equal to,
        processed_at_lteq (date_time): Search: Processed at less than or equal to,
        delivered_at_eq (date_time): Search: Delivered at equals,
        delivered_at_gteq (date_time): Search: Delivered at greater than or equal to,
        delivered_at_lteq (date_time): Search: Delivered at less than or equal to,
        bounced_at_eq (date_time): Search: Bounced at equals,
        bounced_at_gteq (date_time): Search: Bounced at greater than or equal to,
        bounced_at_lteq (date_time): Search: Bounced at less than or equal to,
        bounce_category_eq (str): Search: Bounce category equals,
        bounce_category_cont (str): Search: Bounce category contains,
        soft_bounced_at_eq (date_time): Search: Soft bounced at equals,
        soft_bounced_at_gteq (date_time): Search: Soft bounced at greater than or equal to,
        soft_bounced_at_lteq (date_time): Search: Soft bounced at less than or equal to,

        Returns
        ----------
        Response as dict.
        """
        params = locals()
        params.pop('self')
        req_dict = self.__compose_request('sent_campaigns', id, 'sent_emails',
                                          **params)
        return requests.get(**req_dict)

    @check_request
    def get_sent_campaign_unsubscribe_events(
        self,
        id,
        page=None,
        per_page=None,
        email_eq=None,
        email_cont=None,
        sent_email_id_eq=None,
        sent_email_id_gteq=None,
        sent_email_id_lteq=None,
        source_eq=None,
        source_cont=None,
    ):
        """
       Get sent campaigns for statistics.

        Parameters
        ----------
        id (int): ID of the record,
        page (int): Page number,
        per_page (int): Number of records per page,
        email_eq (str): Search: Email equals,
        email_cont (str): Search: Email contains,
        sent_email_id_eq (int): Search: Sent email equals,
        sent_email_id_gteq (int): Search: Sent email greater than or equal to,
        sent_email_id_lteq (int): Search: Sent email less than or equal to,
        source_eq (str): Search: Processed at greater than or equal to,
        source_cont (str): Search: Processed at less than or equal to,

        Returns
        ----------
        Response as dict.
        """
        params = locals()
        params.pop('self')
        req_dict = self.__compose_request('sent_campaigns', id,
                                          'unsubscribe_events', **params)
        return requests.get(**req_dict)

    # ##### END SENT CAMPAIGNS #####


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')
    DOMAIN = os.getenv('DOMAIN')
    client = MailrelayClient(API_KEY, DOMAIN)
    # campaigns = client.get_sent_campaigns(sender_id_eq=2)
    campaign = client.get_sent_campaign_impressions(21)
    print(campaign)
