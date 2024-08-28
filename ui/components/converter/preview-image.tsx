"use client";
import { Image } from "@nextui-org/image";
import { FaImage } from "react-icons/fa";
import { useState } from "react";
import { AiFillCloseCircle } from "react-icons/ai";

import deleteVideo from "@/actions/video";

export default function PreviewImage({
  isSelected,
  alt,
  src,
  width,
  onSelectVideo,
}) {
  const [imageLoaded, setImageLoaded] = useState(true);
  const deleteVideoWithName = deleteVideo.bind(null, alt);

  const onDeleteButtonClick = () => {
    deleteVideoWithName();
  };

  return (
    <div
      className={`my-2 mx-2 relative ${isSelected ? "rounded-large border-2 border-blue-500" : ""}`}
      onClick={() => onSelectVideo(alt)}
    >
      {imageLoaded ? (
        <Image
          isZoomed
          alt={alt}
          className="object-fit"
          src={src}
          width={width}
          onError={() => setImageLoaded(false)}
        />
      ) : (
        <div className="flex flex-col items-center justify-center h-full">
          <p className="my-6">{alt}</p>
          <FaImage size={50} />
        </div>
      )}
      <button
        className="absolute top-0 right-0 m-1 z-10 focus:outline-none"
        onClick={() => onDeleteButtonClick()}
      >
        <AiFillCloseCircle size={20} />
      </button>
    </div>
  );
}
