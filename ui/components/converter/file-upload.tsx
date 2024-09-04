"use client";

import { useState } from "react";

import { revalidateVideoFiles } from "@/actions/revalidateActions";

export default function FileUpload() {
  const [file, setFile] = useState<File>();

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!file) return;

    const data = new FormData();

    data.set("file", file);

    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/video`, {
      method: "POST",
      body: data,
    });

    revalidateVideoFiles();

    if (!res.ok) throw new Error(await res.text());
  };

  return (
    <div className="my-10">
      <form onSubmit={onSubmit}>
        <input
          name="file"
          type="file"
          onChange={(e) => setFile(e.target.files?.[0])}
        />
        <input type="submit" value="Upload" />
      </form>
    </div>
  );
}
