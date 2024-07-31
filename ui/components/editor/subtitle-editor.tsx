"use client";

import React from "react";
import { debounce } from "lodash";

import { ISegment, IWord } from "@/types/transcription";
import SubtitleSegment from "@/components/editor/subtitle-segment";

interface Props {
  language: string;
  segments: ISegment[];
  word_segments: IWord[];
  transcription_id: string;
  job_id: string;
}

export default function SubtitleEditor({
  language,
  segments,
  word_segments,
  transcription_id,
  job_id,
}: Props) {
  const onTextHandler = (text: string, index: number) => {
    const newSegments = [...segments];

    newSegments[index].text = text;
    console.log("updating segment text ", newSegments[index]);
  };
  const onStartHandler = (start: number, index: number) => {
    const newSegments = [...segments];

    newSegments[index].start = start;
    console.log("updating segment start time ", newSegments[index]);
  };
  const onEndHandler = (end: number, index: number) => {
    newSegments[index].end = end;
    console.log("updating segment end time ", newSegments[index]);
  };
  const onDeleteHandler = (index: number) => {
    const newSegments = [...segments];

    newSegments.splice(index, 1);
    console.log("deleting segment ", newSegments[index]);
  };

  const debouncedTextHandler = debounce(onTextHandler, 1000);
  const debouncedStartHandler = debounce(onStartHandler, 1000);
  const debouncedEndHandler = debounce(onEndHandler, 1000);

  return (
    <div className="flex flex-col gap-4">
      {<p className="text-lg">Language: {language}</p>}
      {segments.map((segment: ISegment, index: number) => {
        return (
          <SubtitleSegment
            key={index}
            end={segment.end}
            start={segment.start}
            text={segment.text}
            onDelete={() => onDeleteHandler(index)}
            onEnd={(end: number) => debouncedEndHandler(end, index)}
            onStart={(start: number) => debouncedStartHandler(start, index)}
            onText={(text: string) => debouncedTextHandler(text, index)}
          />
        );
      })}
    </div>
  );
}
