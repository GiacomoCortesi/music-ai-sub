import UploadedFile from "./uploaded-file";
import { IVideoFile } from "@/types/video";

export interface Props {
  videoFile: string;
}
export default async function UploadedFileCnt({ videoFile }: Props) {
  const response = await fetch(`${process.env.API_URL}/video`, {});

  if (!response.ok) {
    throw new Error("failed to fetch uploaded video files");
  }

  const uploaded_video_files: IVideoFile[] = await response.json();

  const selectedVideoFile = uploaded_video_files.filter((value: IVideoFile) => {
    return value.video_name == videoFile;
  })[0];
  return (
    <div className="w-full flex items-center justify-center h-52">
      <UploadedFile uploadedFile={selectedVideoFile} />
    </div>
  );
}
