import { title } from "@/components/primitives";
import SubtitleEditor from "@/components/editor/subtitle-editor";
import MagicButtons from "@/components/editor/magic-buttons";
export default async function Page({ params }: { params: { id: string } }) {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/transcription/${params.id}`,
  );

  if (!response.ok) {
    throw new Error("failed to fetch transcription");
  }

  const transcription = await response.json();

  return (
    <div>
      <h1 className={title()}>MAIS Editor</h1>
      <SubtitleEditor
        job_id={transcription.job_id}
        language={transcription.data.language}
        segments={transcription.data.segments}
        transcription_id={transcription.transcription_id}
        word_segments={transcription.data.word_segments}
      />
      <MagicButtons />
    </div>
  );
}
