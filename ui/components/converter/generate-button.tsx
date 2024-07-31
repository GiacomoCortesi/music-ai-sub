"use client";
import { Button } from "@nextui-org/button";
import { useState } from "react";

import JobStatus from "./job-status";

import startJob from "@/actions/job";

export default function GenerateButton({ videoFile }) {
  const [jobId, setJobId] = useState(null);
  const onStatusChange = (newStatus) => {
    if (newStatus === "finished") {
      setJobId(null);
    }
  };

  const onClick = async () => {
    const { job_id } = await startJob(videoFile);

    setJobId(job_id);
  };

  return (
    <>
      <Button
        className="m-4"
        isDisabled={videoFile ? false : true}
        isLoading={jobId ? true : false}
        onClick={() => onClick()}
      >
        Generate
      </Button>
      {jobId && <JobStatus jobId={jobId} onStatusChange={onStatusChange} />}
    </>
  );
}
