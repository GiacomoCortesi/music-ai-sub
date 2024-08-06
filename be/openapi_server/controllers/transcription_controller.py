import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.transcription_post200_response import TranscriptionPost200Response  # noqa: E501
from openapi_server.models.transcription_post_request import TranscriptionPostRequest  # noqa: E501
from openapi_server import util
from flask import current_app

from connexion.problem import problem
from openapi_server.services.transcription import TranscriptionNotFoundException

def transcription_get():  # noqa: E501
    """Fetch all transcriptions

     # noqa: E501


    :rtype: Union[List[Transcription], Tuple[List[Transcription], int], Tuple[List[Transcription], int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    return transcription_service.get_all()


def transcription_post(body):  # noqa: E501
    """Creates a new transcription
    NOTE: If you don't rename the transcription_post_request parameter into body, connexion will complain about
    the parameter being missing from the request. Inside job controller we do the same but it words, it may be
    a bug of connexion that depends on the openapi definition.
    May be related to: https://github.com/spec-first/connexion/issues/1939

     # noqa: E501

    :param transcription_post_request: 
    :type transcription_post_request: dict | bytes

    :rtype: Union[Transcription, Tuple[Transcription, int], Tuple[Transcription, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = TranscriptionPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    transcription_service =  current_app.config['transcription_service']
    transcription  = transcription_service.add(body.to_dict())
    
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
    try:
        current_transcription = transcription_service.get(transcription_id)
    except TranscriptionNotFoundException:
        return problem(title="NotFound",
        detail="The requested transcription ID was not found on the server",
        status=404)
    original_transcription = job_service.get(current_transcription["job_id"])["data"]
    transcription_service.edit(transcription_id, original_transcription)

def transcription_transcription_id_delete(transcription_id):  # noqa: E501
    """Deletes a specific transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.delete(transcription_id)

def transcription_transcription_id_fit_post(transcription_id):  # noqa: E501
    """Fit start and end of each subtitles segment

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.fit(transcription_id)

def transcription_transcription_id_fix_post(transcription_id):  # noqa: E501
    """Attempts to fix all subtitles text with AI

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    transcription_service.fix(transcription_id)

def transcription_transcription_id_get(transcription_id):  # noqa: E501
    """Retrieves a specific transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[Transcription, Tuple[Transcription, int], Tuple[Transcription, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    try:
        transcription = transcription_service.get(transcription_id)
    except TranscriptionNotFoundException:
        return problem(title="NotFound",
        detail="The requested transcription ID was not found on the server",
        status=404)
    return transcription