import FileUpload from "./file-upload";
import UploadedFilesGrid from "./uploaded-files-grid";
import GenerateButton from "./generate-button";

export default function Converter({ searchParams }) {
  return (
    <>
      <FileUpload />
      <UploadedFilesGrid />
      <GenerateButton videoFile={searchParams?.selectedVideo ?? ""} />
    </>
  );
}
