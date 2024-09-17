"use server";

import { revalidatePath } from "next/cache";

export async function revalidateVideoFiles() {
  revalidatePath("/video");
}

export async function revalidateTranscription(transcriptionId: string) {
  revalidatePath(`/transcription/${transcriptionId}`);
}

export async function revalidateTranscriptions() {
  revalidatePath(`/transcription`);
}
