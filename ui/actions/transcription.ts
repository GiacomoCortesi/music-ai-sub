export default async function createTranscription(transcription, jobId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: transcription, job_id: jobId }),
      }
    );

    if (!res.ok) throw new Error(await res.text());

    const data = await res.json();

    return data;
  } catch (e: any) {
    console.error(e);
  }
}
