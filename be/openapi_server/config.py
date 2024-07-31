from flask import g

from openapi_server.services.job import JobService
from openapi_server.services.video import VideoService
from openapi_server.services.transcription import TranscriptionService
import os

def get_config():
    return {
        'video_service': VideoService(),
        'job_service': JobService(),
        'transcription_service': TranscriptionService(os.environ.get('OPENAI_TOKEN', ""))
    }