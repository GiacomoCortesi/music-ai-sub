from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class JobConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, model_size=None, subtitles_frequency=None, language=None, speaker_detection=None, hugging_face_token=None):  # noqa: E501
        """JobConfig - a model defined in OpenAPI

        :param model_size: The model_size of this JobConfig.  # noqa: E501
        :type model_size: str
        :param subtitles_frequency: The subtitles_frequency of this JobConfig.  # noqa: E501
        :type subtitles_frequency: int
        :param language: The language of this JobConfig.  # noqa: E501
        :type language: str
        :param speaker_detection: The speaker_detection of this JobConfig.  # noqa: E501
        :type speaker_detection: bool
        :param hugging_face_token: The hugging_face_token of this JobConfig.  # noqa: E501
        :type hugging_face_token: str
        """
        self.openapi_types = {
            'model_size': str,
            'subtitles_frequency': int,
            'language': str,
            'speaker_detection': bool,
            'hugging_face_token': str
        }

        self.attribute_map = {
            'model_size': 'model_size',
            'subtitles_frequency': 'subtitles_frequency',
            'language': 'language',
            'speaker_detection': 'speaker_detection',
            'hugging_face_token': 'hugging_face_token'
        }

        self._model_size = model_size
        self._subtitles_frequency = subtitles_frequency
        self._language = language
        self._speaker_detection = speaker_detection
        self._hugging_face_token = hugging_face_token

    @classmethod
    def from_dict(cls, dikt) -> 'JobConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobConfig of this JobConfig.  # noqa: E501
        :rtype: JobConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model_size(self) -> str:
        """Gets the model_size of this JobConfig.


        :return: The model_size of this JobConfig.
        :rtype: str
        """
        return self._model_size

    @model_size.setter
    def model_size(self, model_size: str):
        """Sets the model_size of this JobConfig.


        :param model_size: The model_size of this JobConfig.
        :type model_size: str
        """
        if model_size is None:
            raise ValueError("Invalid value for `model_size`, must not be `None`")  # noqa: E501

        self._model_size = model_size

    @property
    def subtitles_frequency(self) -> int:
        """Gets the subtitles_frequency of this JobConfig.


        :return: The subtitles_frequency of this JobConfig.
        :rtype: int
        """
        return self._subtitles_frequency

    @subtitles_frequency.setter
    def subtitles_frequency(self, subtitles_frequency: int):
        """Sets the subtitles_frequency of this JobConfig.


        :param subtitles_frequency: The subtitles_frequency of this JobConfig.
        :type subtitles_frequency: int
        """
        if subtitles_frequency is None:
            raise ValueError("Invalid value for `subtitles_frequency`, must not be `None`")  # noqa: E501

        self._subtitles_frequency = subtitles_frequency

    @property
    def language(self) -> str:
        """Gets the language of this JobConfig.


        :return: The language of this JobConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the language of this JobConfig.


        :param language: The language of this JobConfig.
        :type language: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def speaker_detection(self) -> bool:
        """Gets the speaker_detection of this JobConfig.


        :return: The speaker_detection of this JobConfig.
        :rtype: bool
        """
        return self._speaker_detection

    @speaker_detection.setter
    def speaker_detection(self, speaker_detection: bool):
        """Sets the speaker_detection of this JobConfig.


        :param speaker_detection: The speaker_detection of this JobConfig.
        :type speaker_detection: bool
        """
        if speaker_detection is None:
            raise ValueError("Invalid value for `speaker_detection`, must not be `None`")  # noqa: E501

        self._speaker_detection = speaker_detection

    @property
    def hugging_face_token(self) -> str:
        """Gets the hugging_face_token of this JobConfig.


        :return: The hugging_face_token of this JobConfig.
        :rtype: str
        """
        return self._hugging_face_token

    @hugging_face_token.setter
    def hugging_face_token(self, hugging_face_token: str):
        """Sets the hugging_face_token of this JobConfig.


        :param hugging_face_token: The hugging_face_token of this JobConfig.
        :type hugging_face_token: str
        """
        if hugging_face_token is None:
            raise ValueError("Invalid value for `hugging_face_token`, must not be `None`")  # noqa: E501

        self._hugging_face_token = hugging_face_token
