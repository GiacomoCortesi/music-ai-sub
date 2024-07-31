"use client";
// need to use client component because of: https://github.com/nextui-org/nextui/issues/1342
import { useRouter } from "next/navigation";
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  getKeyValue,
} from "@nextui-org/table";
import { Tooltip } from "@nextui-org/tooltip";
import { AiFillEdit, AiFillEye, AiFillDelete } from "react-icons/ai";
import { useCallback } from "react";
export default function TranscriptionTable({ transcriptions }) {
  let rows = [];
  const router = useRouter();

  transcriptions.forEach((transcription, index) => {
    rows.push({
      key: index,
      file: transcription["video_file"],
      language: transcription["data"]["language"],
      id: transcription["transcription_id"],
    });
  });

  const columns = [
    {
      key: "file",
      label: "File",
    },
    {
      key: "language",
      label: "Language",
    },
    {
      key: "id",
      label: "ID",
    },
    {
      key: "actions",
      label: "Actions",
    },
  ];

  const renderCell = useCallback((user, columnKey, index) => {
    const cellValue = user[columnKey];

    switch (columnKey) {
      case "actions":
        return (
          <div className="relative flex items-center gap-2">
            <Tooltip content="Details">
              <span className="text-lg text-default-400 cursor-pointer active:opacity-50">
                <AiFillEye />
              </span>
            </Tooltip>
            <Tooltip content="Edit transcription">
              <span className="text-lg text-default-400 cursor-pointer active:opacity-50">
                <AiFillEdit
                  onClick={() => {
                    router.push(
                      `/transcription/${transcriptions[index]?.transcription_id}`
                    );
                  }}
                />
              </span>
            </Tooltip>
            <Tooltip color="danger" content="Delete transcription">
              <span className="text-lg text-danger cursor-pointer active:opacity-50">
                <AiFillDelete />
              </span>
            </Tooltip>
          </div>
        );
      default:
        return cellValue;
    }
  }, []);

  return (
    <Table removeWrapper aria-label="Example static collection table">
      <TableHeader columns={columns}>
        {(column) => <TableColumn key={column.key}>{column.label}</TableColumn>}
      </TableHeader>
      <TableBody items={rows}>
        {(item) => (
          <TableRow key={item.key}>
            {(columnKey) => (
              <TableCell>{renderCell(item, columnKey, item.key)}</TableCell>
            )}
          </TableRow>
        )}
      </TableBody>
    </Table>
  );
}
