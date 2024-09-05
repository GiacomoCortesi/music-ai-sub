"use client";

import { IVideoFile } from "@/types/video";

import PreviewImageCard from "./preview-image-card";

export interface Props {
  uploadedFile: IVideoFile;
}

export default function UploadedFile({ uploadedFile }: Props) {
  return (
    <>
      <div className="flex items-center justify-center w-full h-52">
        {uploadedFile ? (
          <PreviewImageCard
            isSelected
            alt={uploadedFile.video_name}
            src={uploadedFile.image_url}
            onSelectVideo={(_: string) => {}}
          />
        ) : (
          <p>No file uploaded</p>
        )}
      </div>
    </>
  );
}
