"use server";

import { revalidatePath, revalidateTag } from "next/cache";

export async function revalidateVideoFiles() {
  revalidateTag("uploaded_video_files");
}

export async function revalidateTranscription(transcriptionId: string) {
  revalidatePath(`/transcription/${transcriptionId}`);
}

export async function revalidateTranscriptions() {
  revalidatePath(`/transcription`);
}
