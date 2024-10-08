from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.config import Config
from openapi_server import util

from openapi_server.models.config import Config  # noqa: E501

class MaisJobPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, video_file=None, config=None):  # noqa: E501
        """MaisJobPostRequest - a model defined in OpenAPI

        :param video_file: The video_file of this MaisJobPostRequest.  # noqa: E501
        :type video_file: str
        :param config: The config of this MaisJobPostRequest.  # noqa: E501
        :type config: Config
        """
        self.openapi_types = {
            'video_file': str,
            'config': Config
        }

        self.attribute_map = {
            'video_file': 'video_file',
            'config': 'config'
        }

        self._video_file = video_file
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'MaisJobPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _mais_job_post_request of this MaisJobPostRequest.  # noqa: E501
        :rtype: MaisJobPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def video_file(self) -> str:
        """Gets the video_file of this MaisJobPostRequest.


        :return: The video_file of this MaisJobPostRequest.
        :rtype: str
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file: str):
        """Sets the video_file of this MaisJobPostRequest.


        :param video_file: The video_file of this MaisJobPostRequest.
        :type video_file: str
        """
        if video_file is None:
            raise ValueError("Invalid value for `video_file`, must not be `None`")  # noqa: E501

        self._video_file = video_file

    @property
    def config(self) -> Config:
        """Gets the config of this MaisJobPostRequest.


        :return: The config of this MaisJobPostRequest.
        :rtype: Config
        """
        return self._config

    @config.setter
    def config(self, config: Config):
        """Sets the config of this MaisJobPostRequest.


        :param config: The config of this MaisJobPostRequest.
        :type config: Config
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config
