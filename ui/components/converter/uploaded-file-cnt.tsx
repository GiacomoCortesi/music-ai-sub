import UploadedFile from "./uploaded-file";
import { IVideoFile } from "@/types/video";

export interface Props {
  videoFile: string;
}
export default async function UploadedFileCnt({ videoFile }: Props) {
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/video`, {
    next: { tags: ["uploaded_video_files"] },
  });

  if (!response.ok) {
    throw new Error("failed to fetch uploaded video files");
  }

  const uploaded_video_files: IVideoFile[] = await response.json();

  const selectedVideoFile = uploaded_video_files.filter((value: IVideoFile) => {
    return value.video_name == videoFile;
  })[0];

  return <UploadedFile uploadedFile={selectedVideoFile} />;
}
