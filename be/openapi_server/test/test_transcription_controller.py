import unittest

from flask import json

from openapi_server.models.transcription_post200_response import TranscriptionPost200Response  # noqa: E501
from openapi_server.models.transcription_post_request import TranscriptionPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTranscriptionController(BaseTestCase):
    """TranscriptionController integration test stubs"""

    def test_transcription_post(self):
        """Test case for transcription_post

        Creates a new transcription
        """
        transcription_post_request = openapi_server.TranscriptionPostRequest()
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
        response = self.client.open(
            '/transcription/{transcription_id}/clear'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_delete(self):
        """Test case for transcription_transcription_id_delete

        Deletes a specific transcription
        """
        headers = { 
        }
        response = self.client.open(
            '/transcription/{transcription_id}'.format(transcription_id='transcription_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_fix_post(self):
        """Test case for transcription_transcription_id_fix_post

        Attempts to fix all subtitles text with AI
        """
        headers = { 
        }
        response = self.client.open(
            '/transcription/{transcription_id}/fix'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_get(self):
        """Test case for transcription_transcription_id_get

        Retrieves a specific transcription
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/transcription/{transcription_id}'.format(transcription_id='transcription_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transcription_transcription_id_post(self):
        """Test case for transcription_transcription_id_post

        Adapts all subtitles time windows to make them adjacent
        """
        headers = { 
        }
        response = self.client.open(
            '/transcription/{transcription_id}'.format(transcription_id='transcription_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
