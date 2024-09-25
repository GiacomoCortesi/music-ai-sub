from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from openapi_server.models.transcription import Transcription as ApiTranscription
from openapi_server.domain.models.transcription import Transcription as DomainTranscription
from openapi_server.models.video_get200_response_inner import VideoGet200ResponseInner as ApiFile
from openapi_server.domain.models.file import File as DomainFile
from openapi_server.domain.models.job import Job as DomainJob
from openapi_server.models.job_response import JobResponse as ApiJob

# Define type variables
TSource = TypeVar('TSource')
TDestination = TypeVar('TDestination')

class Mapper(ABC, Generic[TSource, TDestination]):
    @abstractmethod
    def map_to_domain(self, source: TSource) -> TDestination:
        pass

    @abstractmethod
    def map_to_api(self, source: TDestination) -> TSource:
        pass

class TranscriptionMapper(Mapper[ApiTranscription, DomainTranscription]):
    @classmethod
    def map_to_domain(self, source: ApiTranscription) -> DomainTranscription:
        return DomainTranscription(**source.to_dict())

    @classmethod
    def map_to_api(self, source: DomainTranscription) -> ApiTranscription:
        return ApiTranscription.from_dict(source.model_dump())
    
class FileMapper(Mapper[ApiFile, DomainFile]):
    @classmethod
    def map_to_domain(self, source: ApiFile) -> DomainFile:
        return DomainFile(**source.to_dict())

    @classmethod
    def map_to_api(self, source: DomainFile) -> ApiFile:
        return ApiFile(video_id=source.video_id, video_name=source.video_name, upload_date=source.upload_date)

class JobMapper(Mapper[ApiJob, DomainJob]):
    @classmethod
    def map_to_domain(self, source: ApiJob) -> DomainJob:
        return DomainJob(**source.to_dict())

    @classmethod
    def map_to_api(self, source: DomainJob) -> ApiJob:
        return ApiJob(**source.model_dump())