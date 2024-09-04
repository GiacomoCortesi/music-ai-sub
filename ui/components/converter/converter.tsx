import FileUpload from "./file-upload";
import UploadedFilesGrid from "./uploaded-files-grid";
import GenerateButton from "./generate-button";

type Props = {
  videoFile: string;
};

export default function Converter({ videoFile }: Props) {
  return (
    <>
      <FileUpload />
      <UploadedFilesGrid />
      <GenerateButton videoFile={videoFile} />
    </>
  );
}
