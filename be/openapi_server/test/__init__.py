import logging

import connexion
from flask_testing import TestCase

from openapi_server.encoder import JSONEncoder
from openapi_server.services.job import JobService
from openapi_server.services.video import VideoService
from openapi_server.services.transcription import TranscriptionService
from fakeredis import FakeStrictRedis
import os

class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../openapi/')
        app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        js = JobService(FakeStrictRedis())
        app.app.config.update({
        'video_service': VideoService(),
        'job_service': js,
        'transcription_service': TranscriptionService(os.environ.get('OPENAI_TOKEN', ""))
        })
        return app.app
    
    
