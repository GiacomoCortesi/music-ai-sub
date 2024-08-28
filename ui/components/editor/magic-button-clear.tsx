"use client";

import { Button } from "@nextui-org/button";
import { AiOutlineClear } from "react-icons/ai";
import { useState } from "react";

import { clearTranscription } from "@/actions/transcription";

export default function MagicButtonClear({ transcriptionId }) {
  const [isLoading, setIsLoading] = useState(false);

  const onClick = async () => {
    setIsLoading(true);
    await clearTranscriptionWithId();
    setIsLoading(false);
  };
  const clearTranscriptionWithId = clearTranscription.bind(
    null,
    transcriptionId,
  );

  return (
    <Button color="primary" isLoading={isLoading} onClick={onClick}>
      <AiOutlineClear />
      CLEAR
    </Button>
  );
}
