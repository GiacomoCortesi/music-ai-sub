// components/Snackbar.js
import React, { useEffect } from "react";

export interface Props {
  message: string;
  isOpen: boolean;
  onClose: () => void;
}

export default function Snackbar({ message, isOpen, onClose }: Props) {
  useEffect(() => {
    if (isOpen) {
      const timer = setTimeout(onClose, 3000); // Auto-close after 3 seconds

      return () => clearTimeout(timer);
    }
  }, [isOpen, onClose]);

  return (
    <div
      className={`fixed bottom-4 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white px-4 py-2 rounded shadow-lg transition-transform ${
        isOpen ? "translate-y-0" : "translate-y-20"
      }`}
    >
      {message}
    </div>
  );
}
