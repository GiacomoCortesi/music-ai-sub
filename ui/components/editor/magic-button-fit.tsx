"use client";
import { Button } from "@nextui-org/button";
import { AiOutlineAlignCenter } from "react-icons/ai";
export default function MagicButtonFit({ transcription_id }) {
  const onClick = () => {
    // TODO: send POST request to /fit endpoint
    console.log("TODO: send POST request to /fit endpoint");
  };

  return (
    <Button
      color="primary"
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineAlignCenter />
      FIT
    </Button>
  );
}
