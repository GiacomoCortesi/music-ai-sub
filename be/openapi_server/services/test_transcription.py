import unittest
from unittest.mock import MagicMock
from transcription import TranscriptionService
class TestTranscription(unittest.TestCase):
    def test_fit(self):
        transcription_mock_success = {'data': {'segments': [{'start': 1.099, 'end': 2.763, 'text': ' Cialo come il sole', 'words': [{'word': 'Cialo', 'start': 1.099, 'end': 1.4, 'score': 0.491}, {'word': 'come', 'start': 1.58, 'end': 1.921, 'score': 0.587}, {'word': 'il', 'start': 2.041, 'end': 2.081, 'score': 0.157}, {'word': 'sole', 'start': 2.262, 'end': 2.763, 'score': 0.559}]}, {'start': 4.238, 'end': 6.104, 'text': ' che mi scalda il cuore', 'words': [{'word': 'che', 'start': 4.238, 'end': 4.439, 'score': 0.253}, {'word': 'mi', 'start': 4.539, 'end': 4.619, 'score': 0.722}, {'word': 'scalda', 'start': 4.7, 'end': 5.302, 'score': 0.814}, {'word': 'il', 'start': 5.402, 'end': 5.462, 'score': 0.814}, {'word': 'cuore', 'start': 5.643, 'end': 6.104, 'score': 0.904}]}, {'start': 7.556, 'end': 9.306, 'text': ' e blu come il mare.', 'words': [{'word': 'e', 'start': 7.556, 'end': 7.616, 'score': 0.531}, {'word': 'blu', 'start': 7.737, 'end': 7.918, 'score': 0.709}, {'word': 'come', 'start': 8.079, 'end': 8.541, 'score': 0.774}, {'word': 'il', 'start': 8.682, 'end': 8.722, 'score': 0.255}, {'word': 'mare.', 'start': 8.803, 'end': 9.306, 'score': 0.681}]}], 'word_segments': [], 'language': 'it'}}
        transcription_mock_success_expected = {'data': {'segments': [{'start':0, 'end': 2.763, 'text': ' Cialo come il sole', 'words': [{'word': 'Cialo', 'start': 1.099, 'end': 1.4, 'score': 0.491}, {'word': 'come', 'start': 1.58, 'end': 1.921, 'score': 0.587}, {'word': 'il', 'start': 2.041, 'end': 2.081, 'score': 0.157}, {'word': 'sole', 'start': 2.262, 'end': 2.763, 'score': 0.559}]}, {'start': 2.763, 'end': 6.104, 'text': ' che mi scalda il cuore', 'words': [{'word': 'che', 'start': 4.238, 'end': 4.439, 'score': 0.253}, {'word': 'mi', 'start': 4.539, 'end': 4.619, 'score': 0.722}, {'word': 'scalda', 'start': 4.7, 'end': 5.302, 'score': 0.814}, {'word': 'il', 'start': 5.402, 'end': 5.462, 'score': 0.814}, {'word': 'cuore', 'start': 5.643, 'end': 6.104, 'score': 0.904}]}, {'start': 6.104, 'end': 9.306, 'text': ' e blu come il mare.', 'words': [{'word': 'e', 'start': 7.556, 'end': 7.616, 'score': 0.531}, {'word': 'blu', 'start': 7.737, 'end': 7.918, 'score': 0.709}, {'word': 'come', 'start': 8.079, 'end': 8.541, 'score': 0.774}, {'word': 'il', 'start': 8.682, 'end': 8.722, 'score': 0.255}, {'word': 'mare.', 'start': 8.803, 'end': 9.306, 'score': 0.681}]}], 'word_segments': [], 'language': 'it'}}
        service = TranscriptionService("")
        service.get = MagicMock(return_value = transcription_mock_success)
        self.assertEqual(service.fit("dummy"), transcription_mock_success_expected)