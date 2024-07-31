"use client";

import { Button } from "@nextui-org/button";
import { AiOutlineClear } from "react-icons/ai";
export default function MagicButtonClear({ transcriptionId }) {
  const onClick = () => {
    // TODO: send POST request to /clear endpoint
    console.log("TODO: send POST request to /clear endpoint");
  };

  return (
    <Button
      color="primary"
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineClear />
      CLEAR
    </Button>
  );
}
