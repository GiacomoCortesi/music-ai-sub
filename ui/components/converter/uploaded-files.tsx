"use client";
import { useState } from "react";
import { useRouter, usePathname } from "next/navigation";

import PreviewImageCard from "./preview-image-card";
import { IVideoFile } from "@/types/video";

export interface Props {
  uploaded_video_files: IVideoFile[];
}

export default function UploadedFiles({ uploaded_video_files }: Props) {
  const [selectedVideo, setSelectedVideo] = useState("");
  const router = useRouter();
  const pathName = usePathname();
  const handleClick = (video: string) => {
    setSelectedVideo(video);
    // Update the URL's search parameters
    const newSearchParams = new URLSearchParams();

    newSearchParams.set("selectedVideo", video);
    router.push(`${pathName}?${newSearchParams.toString()}`);
  };

  return (
    <>
      {uploaded_video_files.map((uploaded_video_file) => {
        return (
          <PreviewImageCard
            key={uploaded_video_file.video_id}
            alt={uploaded_video_file.video_name}
            isSelected={uploaded_video_file.video_name === selectedVideo}
            src={uploaded_video_file.image_url}
            onSelectVideo={handleClick}
          />
        );
      })}
    </>
  );
}
