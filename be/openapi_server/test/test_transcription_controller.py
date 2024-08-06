import unittest

from flask import json
from unittest.mock import MagicMock

from openapi_server.models.transcription_post200_response import TranscriptionPost200Response  # noqa: E501
from openapi_server.models.transcription_post_request import TranscriptionPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTranscriptionController(BaseTestCase):
    """TranscriptionController integration test stubs"""

    def test_transcription_post(self):
        """Test case for transcription_post

        Creates a new transcription
        """
        transcription_post_request = TranscriptionPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/transcription',
            method='POST',
            headers=headers,
            data=json.dumps(transcription_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_clear_post(self):
        """Test case for transcription_transcription_id_clear_post

        Restores initial transcription
        """
        headers = { 
        }

        js = self.app.config['job_service']
        ts = self.app.config['transcription_service']

        ts.get = MagicMock(return_value = {"data": {}, "job_id": "job_id"})
        ts.edit = MagicMock(return_value = None)
        js.get = MagicMock(return_value = {"job_id": "job_id",
                "data": {}, 
                "config": {}, 
                "status": "pending"})

        response = self.client.open(
            '/transcription/{transcription_id}/clear'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assertStatus(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_delete(self):
        """Test case for transcription_transcription_id_delete

        Deletes a specific transcription
        """
        headers = { 
        }

        ts = self.app.config["transcription_service"]
        ts.delete = MagicMock()

        response = self.client.open(
            '/transcription/{transcription_id}'.format(transcription_id='transcription_id_example'),
            method='DELETE',
            headers=headers)
        self.assertStatus(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_fix_post(self):
        """Test case for transcription_transcription_id_fix_post

        Attempts to fix all subtitles text with AI
        """
        headers = { 
        }
        
        ts = self.app.config["transcription_service"]
        ts.fix = MagicMock()
        response = self.client.open(
            '/transcription/{transcription_id}/fix'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assertStatus(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_get(self):
        """Test case for transcription_transcription_id_get

        Retrieves a specific transcription
        """
        headers = { 
            'Accept': 'application/json',
        }

        ts = self.app.config["transcription_service"]
        ts.get = MagicMock(return_value = {"data": {}, "job_id": "job_id"})

        response = self.client.open(
            '/transcription/{transcription_id}'.format(transcription_id='transcription_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_fit_post(self):
        """Test case for transcription_transcription_id_fit_post

        Adapts all subtitles time windows to make them adjacent
        """
        headers = { 
        }
        ts = self.app.config["transcription_service"]
        ts.fit = MagicMock()
        response = self.client.open(
            '/transcription/{transcription_id}/fit'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assertStatus(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
