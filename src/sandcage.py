# -*- coding: utf-8 -*-
import requests
import certifi
import os

class SandCage:
    API_ROOT = 'https://api.sandcage.com/'
    API_VERSION = '0.2'
    TIMEOUT = 30
    TRUSTED = certifi.where()
    
    def __init__(self, api_key=None):
        """Give your SandCage API Key as a constructor parameter
        This can be retrieved from https://www.sandcage.com/panel/api_key
        """
        
        self.api_key = api_key
        self.sandcage_api_endpoint = '{0}/{1}/'.format(self.API_ROOT,
                                                       self.API_VERSION)
        self.user_agent = '{0} - {1}'.format('SandCage', self.API_VERSION)

    def _get_post_data(self, payload=None):
        """Combine payload with API KEY and return the dictionary."""
        
        d = {'key': self.api_key}
        if payload:
            d.update(payload)
        return d

    def _update_callback(self, data, callback_endpoint=None):
        """Update data with callback_endpoint address."""
        
        if callback_endpoint:
            data.update({'callback_url': callback_endpoint})

    def call_endpoint(self, endpoint, post=False, data=None):
        """The call_endpoint method

        * This method sends http request to the endpoint

        * First parameter "endpoint" (string) is the url of the endpoint.
        * Second parameter "post" (boolean) indicates the http method type.
          True => POST
          False => GET
        * Third parameter "data" (dictionary) is the data to be sent.
        * Method's return type is Response object.
        """
        
        headers = {'User-Agent': self.user_agent}
        if post:
            r = requests.post(endpoint, headers=headers, timeout=self.TIMEOUT,
                              json=data, verify=self.TRUSTED)
        else:
            r = requests.get(endpoint, headers=headers, timeout=self.TIMEOUT,
                             verify=self.TRUSTED)
        return r

    def get_info_service(self, payload=None):
        """The "get-info" service
        
        * First parameter "payload" (dictionary) contains the data to be sent.
        * Method's return type is Response object.
        """
        return self.call_endpoint(self.sandcage_api_endpoint + 'get-info', post=True,
                         data=self._get_post_data(payload))

    def list_files_service(self, payload=None):
        """The "list-files" service
        
        * First parameter "payload" (dictionary) contains the data to be sent.
        * Method's return type is Response object.
        """
        return self.call_endpoint(self.sandcage_api_endpoint + 'list-files', post=True,
                         data=self._get_post_data(payload))

    def destroy_files_service(self, payload=None, callback_endpoint=None):
        """The "destroy-files" service
        
        * First parameter "payload" (dictionary) contains the data to be sent.
        * Second parameter "callback_endpoint" (string) is the url, where the 
          callback should be send to.
        * Method's return type is Response object.
        """

        data = self._get_post_data(payload)
        self._update_callback(data, callback_endpoint)
        return self.call_endpoint(self.sandcage_api_endpoint + 'destroy-files', post=True,
                         data=data)

    def schedule_files_service(self, payload=None, callback_endpoint=None):
        """The "schedule-tasks" service

        * First parameter "payload" (dictionary) contains the data to be sent.
        * Second parameter "callback_endpoint" (string) is the url, where the 
          callback should be send to.
        * Method's return type is Response object.
        """
         
        data = self._get_post_data(payload)
        self._update_callback(data, callback_endpoint)
        return self.call_endpoint(self.sandcage_api_endpoint + 'schedule-tasks',
                         post=True, data=data)

