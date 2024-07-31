"use server";

import { revalidateTag } from "next/cache";

export default async function revalidateVideoFiles() {
  revalidateTag("uploaded_video_files");
}
