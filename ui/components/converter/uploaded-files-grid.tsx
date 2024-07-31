import UploadedFiles from "./uploaded-files";

export default async function UploadedFilesGrid() {
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/video`, {
    next: { tags: ["uploaded_video_files"] },
  });

  if (!response.ok) {
    throw new Error("failed to fetch uploaded video files");
  }

  const uploaded_video_files = await response.json();

  return (
    <>
      <p className="text-lg">Uploaded files</p>
      <div className="grid grid-cols-4 gap-4 overflow-y-auto min-h-[50px] m-4 border-2 rounded-large border-opacity-50 border-white">
        <UploadedFiles uploaded_video_files={uploaded_video_files} />
      </div>
    </>
  );
}
