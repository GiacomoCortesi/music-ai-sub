import {
  revalidateTranscription,
  revalidateTranscriptions,
} from "./revalidateActions";

export async function createTranscription(transcription, jobId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: transcription, job_id: jobId }),
      },
    );

    if (!res.ok) throw new Error(await res.text());

    const data = await res.json();

    return data;
  } catch (e: any) {
    console.error(e);
  }
}

export async function clearTranscription(transcriptionId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}/clear`,
      {
        method: "POST",
      },
    );

    if (!res.ok) throw new Error(await res.text());
    revalidateTranscription(transcriptionId);
  } catch (e: any) {
    console.error(e);
  }
}

export async function fitTranscription(transcriptionId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}/fit`,
      {
        method: "POST",
      },
    );

    if (!res.ok) throw new Error(await res.text());
    revalidateTranscription(transcriptionId);
  } catch (e: any) {
    console.error(e);
  }
}

export async function fixTranscription(transcriptionId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}/fix`,
      {
        method: "POST",
      },
    );

    if (!res.ok) throw new Error(await res.text());
    revalidateTranscription(transcriptionId);
  } catch (e: any) {
    console.error(e);
  }
}

export async function editTranscription(transcriptionId, transcription) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}`,
      {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: transcription }),
      },
    );

    if (!res.ok) throw new Error(await res.text());

    revalidateTranscription(transcriptionId);
  } catch (e: any) {
    console.error(e);
  }
}

export async function deleteTranscription(transcriptionId) {
  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}`,
      {
        method: "DELETE",
      },
    );

    if (!res.ok) throw new Error(await res.text());
    revalidateTranscriptions();
  } catch (e: any) {
    console.error(e);
  }
}
