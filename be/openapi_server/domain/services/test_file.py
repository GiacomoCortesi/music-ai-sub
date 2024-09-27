import unittest
from openapi_server.domain.services.file import FileService
from openapi_server.domain.repositories.file_repository import InMemoryFileRepository
from openapi_server.domain.services.file import InvalidFileException
from openapi_server.domain.services.file import FileStore
from unittest.mock import MagicMock
from faker import Faker
from openapi_server.domain.models.file import File
from pathlib import Path
import io

fake = Faker()

def create_random_file() -> File:
    return File(
        filename=fake.word(),
        id=fake.uuid4(),
        video_url=fake.url(),
        image_url=fake.url(),
        upload_date=fake.date_time_this_decade(),
        video_path=fake.file_path(),
        image_path=fake.file_path()
    )

class TestFile(unittest.TestCase):
    file_repo = InMemoryFileRepository()
    file_store = FileStore(file_root_dir=Path("/tmp/mais/file"))
    file_service = FileService(file_repo)

    def test_get_all(self):
        expected_files = [create_random_file() for _ in range(5)]
        self.file_repo.get_all = MagicMock(return_value = expected_files)
        files = self.file_service.get_all()
        self.assertEqual(files, expected_files)

    def test_get(self):
        expected_file = create_random_file()
        self.file_repo.get_by_id = MagicMock(return_value = expected_file)
        f = self.file_service.get("dummy")
        self.assertEqual(f, expected_file)
    
    def test_add_success(self):
        filename = Path("dummy.mov")
        content = io.BytesIO()
        content.write(b'dummy data')
        expected_file_path = self.file_store._get_file_path(filename)
        self.file_service.add(filename, content)
        self.assertTrue(expected_file_path.exists())
    
    def test_add_invalid_file(self):
        filename = Path("dummy.asdf")
        content = io.BytesIO()
        content.write(b'dummy data')
        with self.assertRaises(InvalidFileException):
            self.file_service.add(filename, content)
        
    
    def test_delete(self):
        filename = Path("dummy.mov")
        expected_file_path = self.file_store._get_file_path(filename)
        self.file_repo.delete = MagicMock(return_value=None)
        self.file_service.delete(filename)
        self.assertTrue(not expected_file_path.exists())

    def test_delete_all(self):
        self.file_repo.delete_all = MagicMock(return_value=None)
        self.file_service.delete_all()  
        self.assertTrue(not any(self.file_store.file_root_dir.iterdir()))
