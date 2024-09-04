"use client";
import { useState } from "react";
import { Button, ButtonGroup } from "@nextui-org/button";

import startJob from "@/actions/job";
import { ISubtitleJobOptions } from "@/types/job";

import JobStatus from "./job-status-card";
import SettingsDropdown from "./settings-dropdown";

export interface Props {
  videoFile: string;
}

export default function GenerateButton({ videoFile }: Props) {
  const [jobId, setJobId] = useState(null);
  const [options, setOptions] = useState<ISubtitleJobOptions>({
    speaker_detection: true,
    subtitles_frequency: 5,
    language: "it",
    model_size: "medium",
    hugging_face_token: "hugging_face_token",
  });

  const onStatusChange = (newStatus: string) => {
    if (newStatus === "finished") {
      setJobId(null);
    }
  };

  const onClick = async () => {
    const { job_id } = await startJob(videoFile, options);

    setJobId(job_id);
  };

  const updateOptions = (key: string, value: any) => {
    setOptions((prevParams) => ({
      ...prevParams,
      [key]: value,
    }));
  };

  return (
    <>
      <ButtonGroup>
        <Button
          isDisabled={videoFile ? false : true}
          isLoading={jobId ? true : false}
          onClick={() => onClick()}
        >
          {videoFile ? "Generate" : "Select video"}
        </Button>
        <SettingsDropdown
          isDisabled={jobId ? true : false}
          options={options}
          onOptionUpdate={updateOptions}
        />
      </ButtonGroup>
      {jobId && <JobStatus jobId={jobId} onStatusChange={onStatusChange} />}
    </>
  );
}
