from datetime import datetime
import uuid
from werkzeug.utils import secure_filename
import os
from moviepy.editor import VideoFileClip
import shutil

class VideoService:
    def __init__(self, video_dir="/tmp/mais/video"):
        self.video_dir = video_dir
        os.makedirs(self.video_dir, exist_ok = True)
        self.videos = {}
    
    @staticmethod
    def _extract_image(video_path, image_path, time=1):
        clip = VideoFileClip(video_path)
        clip.save_frame(image_path, time)
    
    def get_all(self):
        return list(self.videos.values())

    def get_with_url(self, base_url="http://localhost:8080"):
        videos_with_url = []
        
        for uploaded_video in self.get_all():
            videos_with_url.append({
            "video_name": uploaded_video["video_name"],
            "video_url": f'/videos/{uploaded_video["video_id"]}/{uploaded_video["video_name"]}',
            "image_url": f'/videos/{uploaded_video["video_id"]}/{os.path.basename(uploaded_video["image_path"])}',
            "upload_date": uploaded_video["upload_date"],
            "video_id": uploaded_video["video_id"],
        })
        return videos_with_url

    def get(self, video_filename):
        return self.videos[video_filename]

    def delete_all(self):
        for f in os.listdir(self.video_dir):
            os.remove(os.path.join(self.video_dir, f))
        self.videos = {}
    
    def add(self, file):
        video_id = str(uuid.uuid4())
        os.makedirs(os.path.join(self.video_dir, video_id), exist_ok=True)
        video_filename = secure_filename(file.filename)
        video_path = os.path.join(self.video_dir, video_id, video_filename)
        file.save(video_path)

        image_filename = os.path.splitext(video_filename)[0] + ".jpg"
        image_path = os.path.join(self.video_dir, video_id, image_filename)
        try:
            self._extract_image(video_path, image_path)
        except Exception as e:
            print(e)
        self.videos[video_filename] = {
            "video_name": video_filename,
            "video_path": video_path,
            "image_path": image_path,
            "upload_date": datetime.now(),
            "video_id": video_id,
        }

    def delete(self, video_filename):
        video = self.get(video_filename)
        shutil.rmtree(os.path.join(self.video_dir, video["video_id"]))
        return self.videos.pop(video_filename, None)