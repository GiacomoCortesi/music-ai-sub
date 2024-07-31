import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.transcription_post200_response import TranscriptionPost200Response  # noqa: E501
from openapi_server.models.transcription_post_request import TranscriptionPostRequest  # noqa: E501
from openapi_server import util
from flask import current_app

def transcription_get():  # noqa: E501
    """Fetch all transcriptions

     # noqa: E501


    :rtype: Union[List[Transcription], Tuple[List[Transcription], int], Tuple[List[Transcription], int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    return transcription_service.get_all()


def transcription_post(transcription_post_request):  # noqa: E501
    """Creates a new transcription

     # noqa: E501

    :param transcription_post_request: 
    :type transcription_post_request: dict | bytes

    :rtype: Union[Transcription, Tuple[Transcription, int], Tuple[Transcription, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        transcription_post_request = TranscriptionPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    transcription_service =  current_app.config['transcription_service']
    transcription  = transcription_service.add(transcription_post_request.to_dict())
    
    return transcription

def transcription_transcription_id_clear_post(transcription_id):  # noqa: E501
    """Restores initial transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    job_service =  current_app.config['job_service']
    transcription_service =  current_app.config['transcription_service']
    current_transcription = transcription_service.get(transcription_id)
    original_transcription = job_service.get_result(current_transcription["job_id"])
    transcription_service.edit(transcription_id, original_transcription["data"])

    return 204

def transcription_transcription_id_delete(transcription_id):  # noqa: E501
    """Deletes a specific transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.delete(transcription_id)
    return 204

def transcription_transcription_id_fit_post(transcription_id):  # noqa: E501
    """Fit start and end of each subtitles segment

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.fit(transcription_id)
    return 204

def transcription_transcription_id_fix_post(transcription_id):  # noqa: E501
    """Attempts to fix all subtitles text with AI

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.fix(transcription_id)
    return 204

def transcription_transcription_id_get(transcription_id):  # noqa: E501
    """Retrieves a specific transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[Transcription, Tuple[Transcription, int], Tuple[Transcription, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription = transcription_service.get(transcription_id)
    return transcription