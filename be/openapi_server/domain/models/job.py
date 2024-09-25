from pydantic import BaseModel
from openapi_server.domain.models.id import ID
from typing import Any

class Config(BaseModel):
    model_size: str
    subtitles_frequency: int
    language: str
    speaker_detection: bool

class Info(BaseModel):
    video_file: str
    config: Config

class Job(BaseModel):
    job_id: ID
    data: Any
    config: Info
    status: str
