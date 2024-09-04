import React from "react";
import { Popover, PopoverTrigger, PopoverContent } from "@nextui-org/popover";
import { AiFillInfoCircle } from "react-icons/ai";
import { Button } from "@nextui-org/button";
import { ISubtitleJobOptions } from "@/types/job";

import { AiOutlineCheck } from "react-icons/ai";
import { AiOutlineClose } from "react-icons/ai";

export interface Props {
  options: ISubtitleJobOptions;
}

export default function JobInfoPopOver({ options }: Props) {
  return (
    <Popover
      showArrow
      backdrop="opaque"
      placement="right"
      classNames={{
        base: [
          // arrow color
          "before:bg-default-200",
        ],
        content: [
          "py-3 px-4 border border-default-200",
          "bg-gradient-to-br from-white to-default-300",
          "dark:from-default-100 dark:to-default-50",
        ],
      }}
    >
      <PopoverTrigger>
        <div>
          <AiFillInfoCircle />
        </div>
      </PopoverTrigger>
      <PopoverContent>
        {(titleProps) => (
          <div className="px-1 py-2">
            <h3 className="text-small font-bold" {...titleProps}>
              Subtitles generation options
            </h3>
            <div className="text-tiny">
              Language: {options.language ?? "Autodetect"} <br />
              Model size: {options.model_size} <br />
              <div className="flex items-center">
                Speaker detection:
                {options.speaker_detection ? (
                  <AiOutlineCheck className="mx-1" />
                ) : (
                  <AiOutlineClose className="mx-1" />
                )}
              </div>
              Subtitles frequency: {options.subtitles_frequency} <br />
            </div>
          </div>
        )}
      </PopoverContent>
    </Popover>
  );
}
