from datetime import datetime
import os
from moviepy.editor import VideoFileClip
import shutil
from PIL import Image
from openapi_server.domain.repositories.file_repository import FileRepository, InMemoryFileRepository
from pathlib import Path
from typing import IO
from typing import List
from openapi_server.domain.models.file import File
import uuid
from werkzeug.utils import secure_filename

class InvalidFileException(Exception):
    pass

class FileStore:
    def __init__(self, file_root_dir: Path = "/tmp/mais/file"):
        self.file_root_dir = file_root_dir
        os.makedirs(self.file_root_dir, exist_ok = True)

    def _get_file_dir_path(self, filename: Path) -> Path:
        return self.file_root_dir / Path(filename.stem)

    def _get_file_path(self, filename: Path) -> Path:
        return self._get_file_dir_path(filename) / filename
    
    def store(self, filename: Path, content: IO[bytes]) -> Path:
        # sanitize filename for secure fs storage
        filename = Path(secure_filename(str(filename)))
        if not filename:
            return

        os.makedirs(self._get_file_dir_path(filename), exist_ok=True)

        file_path = self._get_file_path(filename)

        # write file in chunks
        chunk_size = 1024 * 1024
        with open(file_path, 'wb') as file:
            while True:
                chunk = content.read(chunk_size)
                if not chunk:
                    break
            file.write(chunk)
        
        return file_path
    
    def delete(self, filename: Path) -> None:
        dir_path = self._get_file_dir_path(filename)
        if dir_path.exists():
            shutil.rmtree(dir_path)
    
    def delete_all(self) -> None:
        for f in os.listdir(self.file_root_dir):
            shutil.rmtree(self.file_root_dir / Path(f))

class FileService:
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    audio_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma']

    def __init__(self, repository: FileRepository = None, file_store: FileStore = None):
        if not repository:
            repository = InMemoryFileRepository()

        self.repository = repository

        if not file_store:
            file_store = FileStore()
        self.file_store = file_store
    
    @staticmethod
    def _extract_image(file_path, time=1) -> Image:
        clip = VideoFileClip(file_path)
    
        frame = clip.get_frame(time)
        return Image.fromarray(frame)

    @staticmethod
    def _is_video_file(file_path: Path)->bool:
        try:
            clip = VideoFileClip(file_path)
            clip.close()
        except Exception:
            return False
        
        return True

    def delete(self, filename: str):
        self.file_store.delete(Path(filename))
        self.repository.delete(filename)

    def delete_all(self):
        self.file_store.delete_all()
        self.repository.delete_all()

    def is_valid(self, filename: Path):
        if filename.suffix in FileService.video_extensions or filename.suffix in FileService.audio_extensions:
            return True
        return False
            
    
    def add(self, filename: Path, content: IO[bytes]):
        if not self.is_valid(filename):
            raise InvalidFileException

        id = str(uuid.uuid4())

        # store file
        file_path = self.file_store.store(filename, content)

        # if it is a video file, extract a preview image
        image_path = Path()
        if self._is_video_file(file_path):
            try:
                preview_image = self._extract_image(file_path)
            except Exception as e:
                print(e)
            # store the preview image
            image_path = self.file_store.store(Path(filename.stem + ".jpg"), preview_image)

        # store file metadata
        f_metadata = {
            "filename": str(filename),
            "video_path": str(file_path),
            "image_path": str(image_path),
            "video_url": f'/videos/{id}/{filename}',
            "image_url": f'/videos/{id}/{image_path.name}',
            "upload_date": datetime.now(),
            "id": id,
        }
        self.repository.add(File(**f_metadata))
    
    def get(self, filename: str):
        return self.repository.get_by_id(filename)

    def get_all(self) -> List[File]:
        return self.repository.get_all()