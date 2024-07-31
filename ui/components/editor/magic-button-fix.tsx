"use client";
import { AiOutlineTool } from "react-icons/ai";
import { Button } from "@nextui-org/button";
export default function MagicButtonFix({ transcription_id }) {
  const onClick = () => {
    // TODO: send POST request to /fiX endpoint
    console.log("TODO: send POST request to /fiX endpoint");
  };

  return (
    <Button
      color="primary"
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineTool />
      FIX
    </Button>
  );
}
