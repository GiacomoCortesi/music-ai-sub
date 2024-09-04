"use client";

import React, { ChangeEvent } from "react";
import { useState, useEffect } from "react";
import { Button } from "@nextui-org/button";

import { ISegment, IWord } from "@/types/transcription";
import SubtitleSegment from "@/components/editor/subtitle-segment";
import { editTranscription } from "@/actions/transcription";

import MagicButtons from "./magic-buttons";

interface Props {
  language: string;
  defaultSegments: ISegment[];
  wordSegments: IWord[];
  transcriptionId: string;
}

export default function SubtitleEditor({
  language,
  defaultSegments,
  wordSegments,
  transcriptionId,
}: Props) {
  const [segments, setSegments] = useState<ISegment[]>(defaultSegments);

  // update subtitle segments everytime the defaultSegments props change (e.g. due to a Clear magic button click)
  useEffect(() => {
    const updateSegmentsOnPropsChange = () => {
      setSegments(defaultSegments);
    };

    updateSegmentsOnPropsChange();
  }, [defaultSegments]);

  const onTextHandler = (
    event: ChangeEvent<HTMLTextAreaElement>,
    index: number
  ) => {
    const newSegments = [...segments];

    newSegments[index].text = event.target.value;
    setSegments(newSegments);
  };
  const onStartHandler = (
    event: ChangeEvent<HTMLInputElement>,
    index: number
  ) => {
    const newSegments = [...segments];

    newSegments[index].start = Number(event.target.value);

    setSegments(newSegments);
  };
  const onEndHandler = (
    event: ChangeEvent<HTMLInputElement>,
    index: number
  ) => {
    const newSegments = [...segments];

    newSegments[index].end = Number(event.target.value);
    setSegments(newSegments);
  };
  const onDeleteHandler = (index: number) => {
    const newSegments = [...segments];

    newSegments.splice(index, 1);
    setSegments(newSegments);
  };

  return (
    <div className="flex flex-col gap-4">
      <Button
        className="my-2"
        color="secondary"
        onClick={editTranscription.bind(null, transcriptionId, {
          language: language,
          segments: segments,
          word_segments: wordSegments,
        })}
      >
        SAVE
      </Button>
      {<p className="text-lg">Language: {language}</p>}
      {segments.map((segment: ISegment, index: number) => {
        return (
          <SubtitleSegment
            key={index}
            end={segment.end}
            start={segment.start}
            text={segment.text}
            onDelete={() => onDeleteHandler(index)}
            onEnd={(event: ChangeEvent<HTMLInputElement>) =>
              onEndHandler(event, index)
            }
            onStart={(event: ChangeEvent<HTMLInputElement>) =>
              onStartHandler(event, index)
            }
            onText={(event: ChangeEvent<HTMLTextAreaElement>) =>
              onTextHandler(event, index)
            }
          />
        );
      })}
      <MagicButtons transcriptionId={transcriptionId} />
    </div>
  );
}
