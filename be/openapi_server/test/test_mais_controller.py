import unittest

from flask import json

from openapi_server.models.job_params import JobParams  # noqa: E501
from openapi_server.models.job_response import JobResponse  # noqa: E501
from openapi_server.models.mais_job_post_request import MaisJobPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMaisController(BaseTestCase):
    """MaisController integration test stubs"""

    def test_mais_job_job_id_get(self):
        """Test case for mais_job_job_id_get

        Get job details
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/mais/job/{job_id}'.format(job_id='job_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mais_job_params_get(self):
        """Test case for mais_job_params_get

        Get jobs configuration information
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/mais/job/params',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mais_job_post(self):
        """Test case for mais_job_post

        Create a new subtitles generation job
        """
        mais_job_post_request = openapi_server.MaisJobPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/mais/job',
            method='POST',
            headers=headers,
            data=json.dumps(mais_job_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
