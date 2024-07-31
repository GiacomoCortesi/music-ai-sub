"use client";

import React from "react";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Button } from "@nextui-org/button";
import { Textarea } from "@nextui-org/input";

import SubtitleSegmentCounter from "./subtitle-segment-counter";

interface Props {
  onStart: any;
  onEnd: any;
  onText: any;
  onDelete: any;
}
export default function SubtitleSegment({
  start,
  end,
  text,
  onStart,
  onEnd,
  onText,
  onDelete,
}) {
  return (
    <Card>
      <CardHeader className="flex gap-3">
        <Button onClick={() => onDelete()}>Delete</Button>
      </CardHeader>
      <CardBody className="flex-row gap-4">
        <div>
          <SubtitleSegmentCounter
            label={"Start"}
            placeholder={start}
            onChange={() => onStart(event?.target.value)}
          />
        </div>
        <Textarea
          defaultValue={text}
          onChange={() => onText(event?.target.value)}
        />
        <div>
          <SubtitleSegmentCounter
            label={"End"}
            placeholder={end}
            onChange={() => onEnd(event?.target.value)}
          />
        </div>
      </CardBody>
    </Card>
  );
}
