from openapi_server.services.job import JobService
from openapi_server.services.video import VideoService
from openapi_server.services.transcription import TranscriptionService
import os
from redis import Redis

def get_config():
    r = Redis()
    return {
        'video_service': VideoService(),
        'job_service': JobService(r),
        'transcription_service': TranscriptionService(os.environ.get('OPENAI_TOKEN', ""))
    }