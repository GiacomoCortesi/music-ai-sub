import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.transcription_post200_response import TranscriptionPost200Response  # noqa: E501
from openapi_server.models.transcription_post_request import TranscriptionPostRequest  # noqa: E501
from openapi_server import util
from flask import current_app
import copy
from connexion.problem import problem
from openapi_server.domain.services.transcription import TranscriptionNotFoundException
from flask import send_file
import io
from connexion import request
from openapi_server.mappers.mappers import TranscriptionMapper

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
    transcription  = transcription_service.add(TranscriptionMapper.map_to_domain(body))
    
    return TranscriptionMapper.map_to_api(transcription)

def transcription_transcription_id_clear_post(transcription_id):  # noqa: E501
    """Restores initial transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    try:
        current_transcription = transcription_service.get(transcription_id)
    except TranscriptionNotFoundException:
        return problem(title="NotFound",
        detail="The requested transcription ID was not found on the server",
        status=404)
    transcription_service.edit(transcription_id, copy.deepcopy(current_transcription.original_data))

def transcription_transcription_id_delete(transcription_id):  # noqa: E501
    """Deletes a specific transcription

     # noqa: E501

    :param transcription_id: 
    :type transcription_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    try:
        transcription_service.delete(transcription_id)
    except TranscriptionNotFoundException:
        return problem(title="NotFound",
        detail="The requested transcription ID was not found on the server",
        status=404)

def transcription_transcription_id_patch(transcription_id, body):  # noqa: E501
    """Edit a specific transcription

     # noqa: E501

    :param transcription_id:
    :type transcription_id: str
    :param transcription_transcription_id_patch_request:
    :type transcription_transcription_id_patch_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        body = TranscriptionPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    transcription_service =  current_app.config['transcription_service']
    transcription_service.edit(transcription_id, TranscriptionMapper.map_to_domain(body.to_dict()).data)

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

    return TranscriptionMapper.map_to_api(transcription)

def transcription_transcription_id_export_get(transcription_id, format=None):  # noqa: E501
    """Export transcription in several subtitle formats

     # noqa: E501

    :param transcription_id:
    :type transcription_id: str
    :param format: The format to export the transcription in
    :type format: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    transcription_service =  current_app.config['transcription_service']
    content=""
    # needed because of https://github.com/spec-first/connexion/issues/1291
    format = request.args["format"]
    
    try:
        if format == "stt":
            content = transcription_service.create_stt(transcription_id)
            filename=f"{transcription_id}.stt"
        elif format =="srt" or format == None:
            content = transcription_service.create_srt(transcription_id)
            filename=f"{transcription_id}.srt"
        else:
            return problem(title="BadRequest", detail="Unsupported export format", status=400)
    except TranscriptionNotFoundException:
        return problem(title="NotFound",
        detail="The requested transcription ID was not found on the server",
        status=404)
    return send_file(io.BytesIO(content.encode()), attachment_filename=filename, as_attachment=True)
    

