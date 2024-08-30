"use client";
import { Button, ButtonGroup } from "@nextui-org/button";
import { useState } from "react";

import JobStatus from "./job-status";
import SettingsDropdown from "./settings-dropdown";

import startJob from "@/actions/job";

export default function GenerateButton({ videoFile }) {
  const [jobId, setJobId] = useState(null);
  const [options, setOptions] = useState({
    speaker_detection: true,
    subtitles_frequency: 5,
    language: "it",
    model_size: "medium",
    hugging_face_token: "hugging_face_token",
  });

  const onStatusChange = (newStatus) => {
    if (newStatus === "finished") {
      setJobId(null);
    }
  };

  const onClick = async () => {
    const { job_id } = await startJob(videoFile, options);

    setJobId(job_id);
  };

  const updateOptions = (key, value) => {
    setOptions((prevParams) => ({
      ...prevParams,
      [key]: value,
    }));
  };

  return (
    <>
      <ButtonGroup>
        <Button
          className="m-4"
          isDisabled={videoFile ? false : true}
          isLoading={jobId ? true : false}
          onClick={() => onClick()}
        >
          {videoFile ? "Generate" : "Select video"}
        </Button>
        <SettingsDropdown
          options={options}
          updateParam={updateOptions}
          videoFile={videoFile}
        />
      </ButtonGroup>
      {jobId && <JobStatus jobId={jobId} onStatusChange={onStatusChange} />}
    </>
  );
}
