import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.job_request import JobRequest  # noqa: E501
from openapi_server.models.job_response import JobResponse  # noqa: E501
from openapi_server import util

from openapi_server.services.subtitle import SubtitleService
from flask import current_app

from connexion.problem import problem

def job_get():  # noqa: E501
    """Get all job details

     # noqa: E501


    :rtype: Union[List[JobResponse], Tuple[List[JobResponse], int], Tuple[List[JobResponse], int, Dict[str, str]]
    """
    job_service =  current_app.config['job_service']
    jobs = job_service.get_all()
    ret_jobs = []
    for job in jobs:
        ret_jobs.append({"job_id": job.get_id(), "data": job.result, "config":job_service.get_info(job.get_id()), "status": job.get_status()})
    return ret_jobs, 200

def job_job_id_get(job_id):  # noqa: E501
    """Get job details

     # noqa: E501

    :param job_id: 
    :type job_id: str

    :rtype: Union[JobResponse, Tuple[JobResponse, int], Tuple[JobResponse, int, Dict[str, str]]
    """
    job_service =  current_app.config['job_service']
    job = job_service.get(job_id)
    if not job:
        return problem(title="NotFound",
        detail="The requested job ID was not found on the server",
        status=404)
    return {"job_id": job.get_id(), "data": job.result, "config":job_service.get_info(job.get_id()), "status": job.get_status()}


def job_post(job_request=None):  # noqa: E501
    """Create a new subtitles generation job

     # noqa: E501

    :param job_request: 
    :type job_request: dict | bytes

    :rtype: Union[JobResponse, Tuple[JobResponse, int], Tuple[JobResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        mais_job_post_request = JobRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # Create an instance of MyService
    # subtitle_service = SubtitleService(model_size=mais_job_post_request.config.model_size, language=mais_job_post_request.config.language)
    subtitle_service = SubtitleService()
    job_service =  current_app.config['job_service']
    video_service =  current_app.config['video_service']
    # video = video_service.get(mais_job_post_request.video_file)
    job_info = {"video_file": mais_job_post_request.video_file, "config": {"speaker_detection": subtitle_service.speaker_detection, "subtitles_frequency": subtitle_service.subtitles_frequency, "language": subtitle_service.language, "model_size": subtitle_service.model_size}}
    # TODO: eventyally handle subtitle generation in the job runner with a specific task. Multiple jobs that depend on each other? (e.g. subtitle gen job depends on vocal extraction etc.)
    # job = job_service.run(job_config, subtitle_service.generate_subtitles, video["video_path"])
    job = job_service.run(job_info, subtitle_service.generate_subtitles_mock)
    return {"job_id": job.get_id(), "data": {}, "config":job_service.get_info(job.get_id()), "status": "pending"}
