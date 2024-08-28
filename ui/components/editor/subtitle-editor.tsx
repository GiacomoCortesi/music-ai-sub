"use client";

import React from "react";
import { useState, useEffect } from "react";
import { Button } from "@nextui-org/button";

import MagicButtons from "./magic-buttons";

import { ISegment, IWord } from "@/types/transcription";
import SubtitleSegment from "@/components/editor/subtitle-segment";
import { editTranscription } from "@/actions/transcription";

interface Props {
  language: string;
  segments: ISegment[];
  wordSegments: IWord[];
  transcriptionId: string;
  jobId: string;
}

export default function SubtitleEditor({
  language,
  defaultSegments,
  wordSegments,
  transcriptionId,
  jobId,
}: Props) {
  const [segments, setSegments] = useState<ISegment[]>(defaultSegments);
  const [isSaving, setIsSaving] = useState<boolean>(false);

  useEffect(() => {
    const timeoutId = setTimeout(async () => {
      setIsSaving(true);
      await editTranscription(transcriptionId, {
        language: language,
        segments: segments,
        word_segments: wordSegments,
      });
      setIsSaving(false);
    }, 5000); // Autosave after 5 seconds of inactivity

    return () => clearTimeout(timeoutId);
  }, [segments]);

  // update subtitle segments everytime the defaultSegments props change (e.g. due to a Clear magic button click)
  useEffect(() => {
    const updateSegmentsOnPropsChange = () => {
      setSegments(defaultSegments);
    };

    updateSegmentsOnPropsChange();
  }, [defaultSegments]);

  const onTextHandler = (text: string, index: number) => {
    const newSegments = [...segments];

    newSegments[index].text = text;
    setSegments(newSegments);
  };
  const onStartHandler = (start: number, index: number) => {
    const newSegments = [...segments];

    newSegments[index].start = Number(start);

    setSegments(newSegments);
  };
  const onEndHandler = (end: number, index: number) => {
    const newSegments = [...segments];

    newSegments[index].end = Number(end);
    setSegments(newSegments);
  };
  const onDeleteHandler = (index: number) => {
    const newSegments = [...segments];

    newSegments.splice(index, 1);
    setSegments(newSegments);
  };

  const onClearHandler = () => {
    // setSegments(defaultSegments);
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
            onEnd={(end: number) => onEndHandler(end, index)}
            onStart={(start: number) => onStartHandler(start, index)}
            onText={(text: string) => onTextHandler(text, index)}
          />
        );
      })}
      <MagicButtons
        transcriptionId={transcriptionId}
        onClear={onClearHandler}
      />
    </div>
  );
}
