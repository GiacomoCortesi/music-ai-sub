import FileUpload from "./file-upload";
import GenerateButton from "./generate-button";
import UploadedFileCnt from "./uploaded-file-cnt";

type Props = {
  videoFile: string;
};

export default function Converter({ videoFile }: Props) {
  return (
    <>
      <FileUpload />
      <UploadedFileCnt videoFile={videoFile} />
      <GenerateButton videoFile={videoFile} />
    </>
  );
}
