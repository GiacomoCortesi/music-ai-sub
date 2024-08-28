"use client";

import { Button } from "@nextui-org/button";
import { AiOutlineExport } from "react-icons/ai";

export default function MagicButtonExport() {
  const onClick = () => {
    // TODO: send POST request to /export endpoint
    // or we could do the export client side only? advantages/disadvantages?
    console.log("TODO: send POST request to /export endpoint");
  };

  return (
    <Button
      color="primary"
      onClick={() => {
        onClick();
      }}
    >
      <AiOutlineExport />
      EXPORT
    </Button>
  );
}
