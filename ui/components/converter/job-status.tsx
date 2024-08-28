import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { createTranscription } from "@/actions/transcription";

export default function JobStatus({ jobId, onStatusChange }) {
  const router = useRouter();
  const [status, setStatus] = useState(null);
  const [jobInfo, setJobInfo] = useState({});
  const intervalId = null;

  async function poll() {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/job/${jobId}`,
    );
    const { status, config, data } = await response.json();

    setJobInfo(config);

    setStatus(status);
    onStatusChange(status);

    if (status === "finished") {
      clearInterval(intervalId);
      const { transcription_id: transcriptionId } = await createTranscription(
        data,
        jobId,
      );

      router.push(`/transcription/${transcriptionId}`);
    }
    if (status === "failed") {
      clearInterval(intervalId);
    }
  }
  useEffect((intervalId) => {
    // call polling function to retrieve status immediately
    poll();
    // call polling function with setInterval to periodically poll for the status
    intervalId = setInterval(poll, 5000); // Poll every 5 seconds

    return () => clearInterval(intervalId); // Clean up on unmount
  }, []);

  return (
    <div>
      {jobId && (
        <p>
          Generating subtitles for {jobInfo["video_file"]}
          <br /> Current status: {status} <br />
          It may take few minutes so be patient, it is worth it!
        </p>
      )}
    </div>
  );
}
