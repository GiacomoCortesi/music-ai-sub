"use client";

import React from "react";
import { Input } from "@nextui-org/input";

export default function SubtitleSegmentCounter({ label, value, onChange }) {
  return (
    <Input
      endContent={
        <div className="pointer-events-none flex items-center">
          <span className="text-default-400 text-small">s</span>
        </div>
      }
      label={label}
      labelPlacement="outside"
      type="number"
      value={value}
      onChange={onChange}
    />
  );
}
