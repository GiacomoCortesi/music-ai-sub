import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.video_get200_response_inner import VideoGet200ResponseInner  # noqa: E501
from openapi_server import util

from flask import current_app
from flask import request

def video_delete(filename=None):  # noqa: E501
    """Delete uploaded video file(s)

     # noqa: E501

    :param filename: Filename of the video to be deleted, if no filename, all uploaded videos are deleted
    :type filename: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if filename:
        current_app.config['video_service'].delete(filename)
    else:
        current_app.config['video_service'].delete_all()
    return {'success': True}, 204

def video_get():  # noqa: E501
    """Retrieves the list of uploaded videos

     # noqa: E501


    :rtype: Union[List[VideoGet200ResponseInner], Tuple[List[VideoGet200ResponseInner], int], Tuple[List[VideoGet200ResponseInner], int, Dict[str, str]]
    """
    video_files = current_app.config['video_service'].get_with_url()
    return video_files

def video_post(file=None):  # noqa: E501
    """Uploads a video file

     # noqa: E501

    :param file: 
    :type file: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if 'file' not in connexion.request.files:
        return {'success': False}, 400

    file = connexion.request.files['file']

    if file.filename == '':
        return {'success': False}, 400

    if file:
        current_app.config['video_service'].add(file)
        return {'success': True}, 200
