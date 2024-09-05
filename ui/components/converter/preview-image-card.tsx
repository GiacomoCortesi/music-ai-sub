import { Card, CardFooter, CardHeader } from "@nextui-org/card";
import { AiFillCloseCircle } from "react-icons/ai";
import { Button } from "@nextui-org/button";
import { usePathname, useRouter } from "next/navigation";

import deleteVideo from "@/actions/video";

import PreviewImage from "./preview-image";

interface Props {
  alt: string;
  src: string;
  isSelected: boolean;
  onSelectVideo: any;
}

export default function PreviewImageCard({
  alt,
  src,
  isSelected,
  onSelectVideo,
}: Props) {
  const router = useRouter();
  const pathName = usePathname();

  const deleteVideoWithName = deleteVideo.bind(null, alt);

  const onDeleteButtonClick = () => {
    deleteVideoWithName();

    // Update the URL's search parameters
    const newSearchParams = new URLSearchParams();

    newSearchParams.set("selectedVideo", "");
    router.push(`${pathName}?${newSearchParams.toString()}`);
  };

  return (
    <Card
      className={`m-1 ${isSelected ? "rounded-large border-2 border-blue-500" : ""}`}
      onPress={() => onSelectVideo(alt)}
    >
      <CardHeader className="justify-end p-0">
        <Button
          isIconOnly
          className="z-10 focus:outline-none"
          radius="full"
          variant="light"
          onClick={() => onDeleteButtonClick()}
        >
          <AiFillCloseCircle size={20} />
        </Button>
      </CardHeader>

      <PreviewImage alt={alt} src={src} onSelectVideo={onSelectVideo} />

      <CardFooter className="p-1 flex justify-center">
        <p>{alt}</p>
      </CardFooter>
    </Card>
  );
}
