import { revalidateVideoFiles } from "./revalidateActions";

export default async function deleteVideo(filename: string) {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/video?filename=${filename}`,
    {
      method: "DELETE",
    }
  );

  if (!res.ok) throw new Error(await res.text());

  revalidateVideoFiles();
}
