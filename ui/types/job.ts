export interface ISubtitleJobOptions {
  speaker_detection: boolean;
  subtitles_frequency: number;
  language: string;
  model_size: string;
  hugging_face_token: string;
}

export interface ISubtitleJobConfig {
  config: ISubtitleJobOptions;
  video_file: string;
}
