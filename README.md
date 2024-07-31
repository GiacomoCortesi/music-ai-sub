![GitHub commit activity](https://img.shields.io/github/commit-activity/m/GiacomoCortesi/music-ai-sub)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1vGiYb6ODdaRhMo6KMXC3lSFDkTCU1jc_?usp=sharing)

# music-ai-sub
AI-powered app for transcribing music lyric videos into multiple subtitle formats (e.g. srt, vtt) with an integrated editor for smart and simplified subtitle modifications.

Note that this is a full stack app where:
 - frontend side is built upon Next js with nextui and tailwind for styling
 - web server is API first, code stubs generated through openapi generator CLI for python flask with connexion library
 - AI services use whisperx for subtitles generation, spleeter for audio to stems separation, and ChatGPT for smart subtitle fixes.

Main features:
 - whisperx speech-to-text and diarization
 - spleeter vocals extraction
 - redis queue for generation jobs management
 - smart subtitles editor

### TODOs:
 - job/transcription data persistence
 - UI - edit/delete/details button implementation
 - UI - fit/fix/clear/export button implementation
 - unit tests
 - user authentication/management
 - docker/k8s deployment
 - settings editor for subtitles generation configuration (model size, speaker detection, etc.)

## Run & Develop
### UI
```bash
cd ui
npm install
npm run dev
```

### Backend
Prerequisites:
 - install and start redis server (e.g. with [docker](https://hub.docker.com/_/redis/))
 - start redis queue worker process:
  `rq worker --with-scheduler`

Run:
```bash
cd be
python3 -m openapi_server
```

### Generate code stubs with openapi CLI generator tool
With Docker:

```bash
cd be

docker run --rm -v "${PWD}:/local"  -v /home/gcortesi/music-ai-sub/openapi.yml:/openapi.yml openapitools/openapi-generator-cli generate    -i /openapi.yml     -g python-flask     -o /local/
```