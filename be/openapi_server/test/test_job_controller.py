import unittest

from flask import json

from openapi_server.models.job_request import JobRequest  # noqa: E501
from openapi_server.models.job_response import JobResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestJobController(BaseTestCase):
    """JobController integration test stubs"""

    def test_job_get(self):
        """Test case for job_get

        Get all job details
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/job',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_job_id_get(self):
        """Test case for job_job_id_get

        Get job details
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/job/{job_id}'.format(job_id='job_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_post(self):
        """Test case for job_post

        Create a new subtitles generation job
        """
        job_request = {"video_file":"video_file","config":{"speaker_detection":True,"subtitles_frequency":0,"hugging_face_token":"hugging_face_token","language":"language","model_size":"model_size"}}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/job',
            method='POST',
            headers=headers,
            data=json.dumps(job_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
