"use client";

import { ChangeEvent } from "react";

import { revalidateVideoFiles } from "@/actions/revalidateActions";

import { FileInput, Label } from "flowbite-react";

export default function FileUpload() {
  const handleFileChange = async (event: ChangeEvent<HTMLInputElement>) => {
    if (!event.target.files) return;

    const selectedFile = event.target.files[0];

    const data = new FormData();

    data.set("file", selectedFile);

    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/video`, {
      method: "POST",
      body: data,
    });

    if (!res.ok) throw new Error(await res.text());

    // Update the URL's search parameters
    const newSearchParams = new URLSearchParams();

    newSearchParams.set("selectedVideo", selectedFile.name);

    window.history.pushState(null, "", `?${newSearchParams.toString()}`);
    revalidateVideoFiles();
  };

  return (
    <div className="flex w-full items-center justify-center m-2">
      <Label
        htmlFor="dropzone-file"
        className="flex h-64 w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed border-amber-300 hover:bg-blue-500/20"
      >
        <div className="flex flex-col items-center justify-center pb-6 pt-5">
          <svg
            className="mb-4 h-8 w-8 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 16"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
            />
          </svg>
          <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
            <span className="font-semibold">Click to upload</span> or drag and
            drop
          </p>
          <p className="text-xs text-gray-500 dark:text-gray-400">
            MP4, AVI, MOV (MAX. 20Mb)
          </p>
        </div>
        <FileInput
          onChange={handleFileChange}
          id="dropzone-file"
          className="hidden"
        />
      </Label>
    </div>
  );
}
