"use client";
import { Button } from "@nextui-org/button";
import { AiOutlineAlignCenter } from "react-icons/ai";
import { useState } from "react";

import { fitTranscription } from "@/actions/transcription";

export default function MagicButtonFit({ transcriptionId }) {
  const [isLoading, setIsLoading] = useState(false);
  const onClick = async () => {
    setIsLoading(true);
    await fitTranscriptionWithId();
    setIsLoading(false);
  };

  const fitTranscriptionWithId = fitTranscription.bind(null, transcriptionId);

  return (
    <Button
      color="primary"
      isLoading={isLoading}
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineAlignCenter />
      FIT
    </Button>
  );
}
