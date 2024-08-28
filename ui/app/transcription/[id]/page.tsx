import { title } from "@/components/primitives";
import SubtitleEditor from "@/components/editor/subtitle-editor";

export default async function Page({ params }: { params: { id: string } }) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/transcription/${params.id}`,
    {
      method: "GET",
    },
    { cache: "no-store" },
  );

  if (!response.ok) {
    throw new Error("failed to fetch transcription");
  }

  const transcription = await response.json();

  return (
    <div>
      <h1 className={title()}>MAIS Editor</h1>
      <SubtitleEditor
        defaultSegments={transcription.data.segments}
        jobId={transcription.job_id}
        language={transcription.data.language}
        transcriptionId={transcription.transcription_id}
        wordSegments={transcription.data.word_segments}
      />
    </div>
  );
}
