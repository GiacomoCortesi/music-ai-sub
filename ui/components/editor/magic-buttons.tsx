"use client";
import MagicButtonFit from "./magic-button-fit";
import MagicButtonFix from "./magic-button-fix";
import MagicButtonClear from "./magic-button-clear";
import MagicButtonExport from "./magic-button-export";

export default function MagicButtons({ transcriptionId }) {
  return (
    <div className="fixed inset-x-0 bottom-0 flex justify-around p-4 shadow-lg z-50">
      <MagicButtonFit transcriptionId={transcriptionId} />
      <MagicButtonFix transcriptionId={transcriptionId} />
      <MagicButtonClear transcriptionId={transcriptionId} />
      <MagicButtonExport />
    </div>
  );
}
