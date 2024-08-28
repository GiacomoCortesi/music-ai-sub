import requests
import uuid
import json
import copy

class TranscriptionNotFoundException(Exception):
    pass

class TranscriptionService:
    def __init__(self, openai_token):
        self.openai_token = openai_token
        self.transcriptions = {}
    
    def add(self, transcription):
        transcription_id = str(uuid.uuid4())
        transcription["transcription_id"] = transcription_id
        transcription["original_data"] = copy.deepcopy(transcription["data"])
        self.transcriptions[transcription_id] = transcription
        return transcription

    def get_all(self):
        return list(self.transcriptions.values())

    def get(self, transcription_id):
        try:
            return self.transcriptions[transcription_id]
        except KeyError:
            raise TranscriptionNotFoundException

    def edit(self, transcription_id, transcription_data):
        transcription = self.get(transcription_id)
        transcription["data"] = transcription_data
        self.transcriptions[transcription_id] = transcription
    
    def delete(self, transcription_id):
        try:
            self.transcriptions.pop(transcription_id)
        except KeyError:
            raise TranscriptionNotFoundException
    
    def fit(self, transcription_id):
        transcription = self.get(transcription_id)
        segments = copy.deepcopy(transcription["data"]["segments"])
        for index, segment in enumerate(segments):
            if index == 0:
                segment_start = 0
            else:
                segment_start = segments[index - 1]["end"]
            segment_end = segment["end"]

            segment["start"] = segment_start
            segment["end"] = segment_end       
        
        transcription["data"]["segments"] = segments

        self.edit(transcription_id, transcription["data"])
        return transcription

    def fix(self, transcription_id):
        transcription = self.get(transcription_id)
        transcription_data = transcription["data"]
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_token}"
        }
        prompt = f'''
        The following data contains some text in {transcription_data.get("language", "en")} language code.
        The text may contain incorrect words, attempt to fix incorrect words.
        The text you need to consider is inside the segments array, each element in the array has a text field
        containing the target text. When doing the correction you can try to make meaningful corrections also based on the
        overall context of the text.
        Try to correct as little as possible.
        There may be some word in a different language (or wrongly translated), fix it in the original language but do not translate it.
        Only respond in valid JSON format
        In the returned JSON skip the "word_segments" and "language" keys. Only include the "segments" key.
        In the "segments" object skip the "words" key.
        {transcription_data}
        '''
        data = {
            "response_format": { "type": "json_object" },
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=data).json()
        segments = json.loads(response["choices"][0]["message"]["content"])["segments"]
        for index, segment in enumerate(segments):
            if index < len(transcription["data"]["segments"]):
                transcription["data"]["segments"][index]["text"] = segment["text"]
        
        self.edit(transcription_id, transcription["data"])
        