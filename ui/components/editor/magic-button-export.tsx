"use client";

import { useState } from "react";
import { AiOutlineExport } from "react-icons/ai";
import { Button, ButtonGroup } from "@nextui-org/button";
import {
  Dropdown,
  DropdownTrigger,
  DropdownMenu,
  DropdownItem,
} from "@nextui-org/dropdown";

import { ChevronDownIcon } from "@/components/icons";

export default function MagicButtonExport({ transcriptionId }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedOption, setSelectedOption] = useState(new Set(["srt"]));

  const onClick = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/transcription/${transcriptionId}/export?format=${selectedOptionValue}`,
      );
      let filename = `${transcriptionId}-${selectedOptionValue}`;

      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");

        a.href = url;
        a.download = filename; // Set the file name
        document.body.appendChild(a);
        a.click();
        a.remove();
      } else {
        setError(result.error);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const descriptionsMap = {
    srt: "Export subtitles in srt format",
    stt: "Export subtitles in stt format",
  };

  const labelsMap = {
    srt: "srt",
    stt: "stt",
  };

  // Convert the Set to an Array and get the first value.
  const selectedOptionValue = Array.from(selectedOption)[0];

  return (
    <ButtonGroup>
      <Button color="primary" isLoading={loading} onClick={onClick}>
        <AiOutlineExport />
        EXPORT {labelsMap[selectedOptionValue]}
      </Button>
      <Dropdown placement="bottom-end">
        <DropdownTrigger>
          <Button isIconOnly color="primary">
            <ChevronDownIcon />
          </Button>
        </DropdownTrigger>
        <DropdownMenu
          disallowEmptySelection
          aria-label="Export options"
          className="max-w-[300px]"
          selectedKeys={selectedOption}
          selectionMode="single"
          onSelectionChange={setSelectedOption}
        >
          <DropdownItem key="srt" description={descriptionsMap["srt"]}>
            {labelsMap["srt"]}
          </DropdownItem>
          <DropdownItem key="stt" description={descriptionsMap["stt"]}>
            {labelsMap["stt"]}
          </DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </ButtonGroup>
  );
}
