from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.word import Word
from openapi_server import util

from openapi_server.models.word import Word  # noqa: E501

class Segment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, end=None, text=None, words=None):  # noqa: E501
        """Segment - a model defined in OpenAPI

        :param start: The start of this Segment.  # noqa: E501
        :type start: float
        :param end: The end of this Segment.  # noqa: E501
        :type end: float
        :param text: The text of this Segment.  # noqa: E501
        :type text: str
        :param words: The words of this Segment.  # noqa: E501
        :type words: List[Word]
        """
        self.openapi_types = {
            'start': float,
            'end': float,
            'text': str,
            'words': List[Word]
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'text': 'text',
            'words': 'words'
        }

        self._start = start
        self._end = end
        self._text = text
        self._words = words

    @classmethod
    def from_dict(cls, dikt) -> 'Segment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Segment of this Segment.  # noqa: E501
        :rtype: Segment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> float:
        """Gets the start of this Segment.


        :return: The start of this Segment.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start: float):
        """Sets the start of this Segment.


        :param start: The start of this Segment.
        :type start: float
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self) -> float:
        """Gets the end of this Segment.


        :return: The end of this Segment.
        :rtype: float
        """
        return self._end

    @end.setter
    def end(self, end: float):
        """Sets the end of this Segment.


        :param end: The end of this Segment.
        :type end: float
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def text(self) -> str:
        """Gets the text of this Segment.


        :return: The text of this Segment.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Segment.


        :param text: The text of this Segment.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def words(self) -> List[Word]:
        """Gets the words of this Segment.


        :return: The words of this Segment.
        :rtype: List[Word]
        """
        return self._words

    @words.setter
    def words(self, words: List[Word]):
        """Sets the words of this Segment.


        :param words: The words of this Segment.
        :type words: List[Word]
        """

        self._words = words
