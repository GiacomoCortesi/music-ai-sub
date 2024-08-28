"use client";
import { AiOutlineTool } from "react-icons/ai";
import { Button } from "@nextui-org/button";
import { useState } from "react";

import { fixTranscription } from "@/actions/transcription";

export default function MagicButtonFix({ transcriptionId }) {
  const [isLoading, setIsLoading] = useState(false);

  const onClick = async () => {
    setIsLoading(true);
    await fixTranscriptionWithId();
    setIsLoading(false);
  };

  const fixTranscriptionWithId = fixTranscription.bind(null, transcriptionId);

  return (
    <Button
      color="primary"
      isLoading={isLoading}
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineTool />
      FIX
    </Button>
  );
}
