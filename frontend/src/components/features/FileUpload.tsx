"use client";

import { useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { cn } from "@/lib/utils";
import api from "@/lib/api";
import { UploadCloud } from "lucide-react";
import { Button } from "@/components/ui/Button";

export function FileUpload() {
  const [isDragging, setIsDragging] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const router = useRouter();

  const handleFileUpload = useCallback(async (file: File) => {
    if (file.type !== "application/pdf") {
      setError("Only PDF files are allowed.");
      return;
    }
    setError(null);
    setIsUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      await api.post("/parse/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      router.push("/dashboard/history");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Upload failed. Please try again.");
    } finally {
      setIsUploading(false);
    }
  }, [router]);

  const onDragEnter = (e: React.DragEvent<HTMLDivElement>) => { e.preventDefault(); e.stopPropagation(); setIsDragging(true); };
  const onDragLeave = (e: React.DragEvent<HTMLDivElement>) => { e.preventDefault(); e.stopPropagation(); setIsDragging(false); };
  const onDragOver = (e: React.DragEvent<HTMLDivElement>) => { e.preventDefault(); e.stopPropagation(); };
  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFileUpload(e.dataTransfer.files[0]);
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto text-center">
      <div
        onDragEnter={onDragEnter}
        onDragLeave={onDragLeave}
        onDragOver={onDragOver}
        onDrop={onDrop}
        className={cn(
          "relative block w-full rounded-aurora border-2 border-dashed border-gray-300 p-12 transition-colors",
          { "border-aurora-600 bg-aurora-50": isDragging }
        )}
      >
        <UploadCloud className="mx-auto h-12 w-12 text-gray-400" />
        <p className="mt-2 block text-sm font-medium text-gray-900">
          Drag & drop a PDF here
        </p>
        <p className="text-xs text-gray-500">Maximum file size: 10MB</p>
      </div>
      <div className="mt-4">
        <Button asChild>
          <label htmlFor="file-upload" className="cursor-pointer">
            {isUploading ? "Uploading..." : "Or choose a file"}
          </label>
        </Button>
        <input
          id="file-upload"
          type="file"
          className="sr-only"
          onChange={(e) => e.target.files && handleFileUpload(e.target.files[0])}
          accept="application/pdf"
          disabled={isUploading}
        />
      </div>
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
    </div>
  );
}
