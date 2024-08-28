"use client";
import { useState } from "react";
import { useRouter, usePathname } from "next/navigation";

import PreviewImage from "./preview-image";
export default function UploadedFiles({ uploaded_video_files }) {
  const [selectedVideo, setSelectedVideo] = useState(null);
  const router = useRouter();
  const pathName = usePathname();
  const handleClick = (video) => {
    setSelectedVideo(video);
    // Update the URL's search parameters
    const newSearchParams = new URLSearchParams(router.query);

    newSearchParams.set("selectedVideo", video);
    router.push(`${pathName}?${newSearchParams.toString()}`, undefined, {
      shallow: true,
    });
  };

  return (
    <>
      {uploaded_video_files.map((uploaded_video_file) => {
        return (
          <PreviewImage
            key={uploaded_video_file.video_id}
            alt={uploaded_video_file.video_name}
            isSelected={uploaded_video_file.video_name === selectedVideo}
            src={uploaded_video_file.image_url}
            width={100}
            onSelectVideo={handleClick}
          />
        );
      })}
    </>
  );
}
