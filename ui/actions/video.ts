import { revalidateVideoFiles } from "./revalidateActions";

export async function deleteVideo(filename: string) {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/video?filename=${filename}`,
    {
      method: "DELETE",
    }
  );

  if (!res.ok) throw new Error(await res.text());

  revalidateVideoFiles();
}

export async function uploadVideo(formData: FormData) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/video`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error(await res.text());

  revalidateVideoFiles();
}
